#!./venv/bin/python3
from hapi import Haven
from pprint import pprint
import json


def main():
    print("# Simple Random Image scrapper.")
    haven_instance = Haven()
    haven_instance.set_min_resolution(); # Setup min resolution, the default is 1080p
    # haven_instance.set_min_resolution(1920, 1200); for a different resolution 1920x1200
    haven_instance.set_resolution(); # Setup resolution, the default is 1080p but the differnce between this and the other set_min_resolution.
    # this one makes it so any resolution that is less than whatever resolution u set wont be send back.



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
    # haven_instance.accept_all_purities() # Alll the above
    images = haven_instance.search()
    for im in images: print(json.dumps(im, indent=4))
    print("# download latest search results")
    haven_instance.download_latest_result()

if __name__ == "__main__": main()
