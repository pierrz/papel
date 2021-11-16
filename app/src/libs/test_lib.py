import json
import os
from pathlib import Path


def get_test_fixtures_path():
    return [os.sep, "opt", "app", "tests", "fixtures"]


fixtures_path_array = get_test_fixtures_path()


def get_expected_results_dict(test_name):
    expected_results_path = Path(
        *fixtures_path_array, f"test_{test_name}_expected_results.json"
    )
    return json.load(open(expected_results_path, "r"))


def get_expected_results_dict_for_specific_file(filename):
    expected_results_path = Path(*fixtures_path_array, f"test_{filename}.json")
    return json.load(open(expected_results_path, "r"))
