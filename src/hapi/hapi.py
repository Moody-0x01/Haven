#!/usr/bin/env python3
from json import loads
import os
from posix import mkdir
from random import randint
import requests
from urllib.parse import quote

class Haven:

    def __init__(self) -> None:
        self.__base   = "https://wallhaven.cc/api/v1"
        self.__api_key = os.environ["WALLHAVEN_API_KEY"]
        if not self.__api_key:
            raise RuntimeError("Did not find the api key.")
        self.__resolution = ""
        self.__categories = "111" # GENERAL|ANIME|PEOPLE
        self.__purity = "100" # SFW|SKETCHY|NSFW
        self.__min_height = 0
        self.__min_width = 0
        self.__latest_result = []

    @classmethod
    def download_images(cls, images: list[dict], download_path: str):
        total = len(images)
        if not os.path.exists(download_path): mkdir(download_path)
        for i, img in enumerate(images):
            iurl = img['path']
            filename = iurl.split('/')[-1]
            path_ = f"{download_path}/{filename}"
            response = requests.get(iurl)
            ibytes = response.content
            with open(path_, "wb+") as fp:
                fp.write(ibytes)
                print(f"{i}/{total}[*] {iurl} -> {path_}")
    @classmethod
    def generate_seed(cls):
        possible ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        return ''.join([possible[randint(0, len(possible)-1)] for _ in range(6)])

    # category methods
    def anime_only(self):         self.__categories = "010"
    def people_only(self):        self.__categories = "001"
    def generale_only(self):      self.__categories = "100"
    def accept_all(self):         self.__categories = "111"

    # purity methods
    def nsfw_only(self):           self.__purity = "001"
    def sfw_only(self):            self.__purity = "100"
    def sketchy_only(self):        self.__purity = "010"
    def accept_all_purities(self): self.__purity = "111"

    def set_min_resolution(self, w: int = 1920, h: int = 1080):
        self.__min_height = h
        self.__min_width = w
    def set_resolution(self, w: int = 1920, h: int = 1080):
        self.__resolution = f"{w}x{h}"

    def search(self, query: str = "", page: int = 1) -> list[dict]:
        search_url = f"{self.__base}/search"
        if query:
            query = quote(query)
            search_url += f"?q={query}&apikey={self.__api_key}&categories={self.__categories}&atleast=1920x1080&page={page}&purity={self.__purity}"
        else:
            seed = Haven.generate_seed()
            search_url += f"?seed={seed}&apikey={self.__api_key}&categories={self.__categories}&atleast=1920x1080&page={page}&purity={self.__purity}"
        if self.__resolution: search_url += f"&resolutions={self.__resolution}"
        request = requests.get(search_url)
        assert request.status_code == 200 and "Well the search failed:)"
        images = [ img for img in loads(request.content)['data'] if img['dimension_x'] >= self.__min_width and img['dimension_y'] >= self.__min_height ]
        self.__latest_result = images
        return images

    def bulk_search(self, query: str = "", pages: int = 4) -> list[dict]:
        images = []
        if pages <= 0:
            return [{}]
        for i in range(pages):
            imgs = self.search(query, i+1)
            if len(imgs): images.extend(imgs)
        self.__latest_result = images
        return images
    def search_trending(self, q: str = "", page: int = 1, top_range: str = "1M") -> list[dict]:
        search_url = f"{self.__base}/search"
        search_url += f"?sorting=toplist&topRange={top_range}&apikey={self.__api_key}&categories={self.__categories}&atleast=1920x1080&page={page}&purity={self.__purity}"
        if q:
            search_url += f"&q={quote(q)}"
        if self.__resolution:
            search_url += f"&resolutions={self.__resolution}"
        request = requests.get(search_url)
        if request.status_code != 200:
            print(request)
            assert 0
        images = [img for img in loads(request.content)['data'] if img['dimension_x'] >= self.__min_width and img['dimension_y'] >= self.__min_height]
        self.__latest_result = images
        return images

    def bulk_search_trending(self, q: str = "", pages: int = 4, top_range: str = "1M") -> list[dict]:
        images = []
        if pages <= 0:
            return [{}]
        for i in range(pages):
            imgs = self.search_trending(q, i + 1, top_range)
            if imgs:
                images.extend(imgs)
        self.__latest_result = images
        return images

    def download_latest_result(self, download_path: str = "./haven"):
        Haven.download_images(self.__latest_result, download_path);
        self.__latest_result = []
