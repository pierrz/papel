import json
import os
import shutil
from pathlib import Path, PurePath

import requests
from worker import logger


def fetch_json_from_url(url):
    """Fetch JSON data from given url"""
    r = requests.get(url)
    return r.json()


def load_json(filepath):
    """Load JSON into dict object"""
    jsonFile = open(filepath)
    jsonStr = jsonFile.read()
    data_dict = json.loads(jsonStr)
    return data_dict
