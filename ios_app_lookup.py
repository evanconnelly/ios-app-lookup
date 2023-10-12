#!/usr/bin/env python3

import requests
import argparse

API_LOOKUP_URL = "http://itunes.apple.com/lookup"

def lookup_app_by_bundle(bundle_id, country="us"):
    params = {
        "bundleId": bundle_id,
        "country": country
    }
    return _lookup_app(params)

def lookup_app_by_id(app_id, country="us"):
    params = {
        "id": app_id,
        "country": country
    }
    return _lookup_app(params)

def _lookup_app(params):
    response = requests.get(API_LOOKUP_URL, params=params)
    data = response.json()

    if data["resultCount"] == 0:
        print("No results found.")
        return None

    return data["results"][0]

def main():
    parser = argparse.ArgumentParser(description="Lookup iOS apps on the App Store.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-b", "--bundle", help="Lookup by app bundle ID.")
    group.add_argument("-i", "--id", help="Lookup by app ID.", type=int)

    args = parser.parse_args()

    if args.bundle:
        app_data = lookup_app_by_bundle(args.bundle)
    else:
        app_data = lookup_app_by_id(args.id)

    if app_data:
        print("Name:", app_data.get("trackName", "Unknown"))
        print("Bundle ID:", app_data.get("bundleId", "Unknown"))
        print("App ID:", app_data.get("trackId", "Unknown"))
        print("URL:", app_data.get("trackViewUrl", "Unknown"))

if __name__ == "__main__":
    main()
