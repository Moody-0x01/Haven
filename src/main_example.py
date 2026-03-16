#!./venv/bin/python3
from hapi import Haven
from pprint import pprint
import json


def main():
    print("# Simple Random Image scrapper.")
    haven_instance = Haven()
    images = haven_instance.search()
    for im in images: print(json.dumps(im, indent=4))
    print("# Simple Random Image scrapper Multiple pages.")
    images = haven_instance.bulk_search("", 10) # Default is 4
    for im in images: print(json.dumps(im, indent=4))

    print("# categorized search")
    haven_instance.anime_only() # For anime
    # haven_instance.people_only() # For people images
    # haven_instance.generale_only() # For Generale search
    # haven_instance.accept_all() # All the above
    images = haven_instance.search()
    for im in images: print(json.dumps(im, indent=4))
    
    print("# purity change search")
    haven_instance.sfw_only() # SFW
    # haven_instance.nsfw_only() # NSWF
    # haven_instance.sketchy_only() # Sketchy content
    images = haven_instance.search()
    for im in images: print(json.dumps(im, indent=4))

if __name__ == "__main__": main()
