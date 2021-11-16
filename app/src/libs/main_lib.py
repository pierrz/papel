import json

import requests


def fetch_json_from_url(url):
    """Fetch JSON data from given url"""
    r = requests.get(url)
    return r.json()


def load_json(filepath):
    """Load JSON into dict object"""
    json_str = open(filepath).read()
    return json.loads(json_str)
