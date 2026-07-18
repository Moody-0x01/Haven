#!./venv/bin/python3
from hapi import Haven
from pprint import pprint
import json


def main():
    haven_instance = Haven()
    haven_instance.set_min_resolution(); # Setup min resolution, the default is 1080print
    haven_instance.anime_only()
    haven_instance.sfw_only()
    haven_instance.set_min_resolution()

    haven_instance.bulk_search("", 20)
    haven_instance.download_latest_result("../../../wallpapers/")

if __name__ == "__main__": main()
