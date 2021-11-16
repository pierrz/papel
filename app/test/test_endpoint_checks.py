from config import app_config
from fastapi.testclient import TestClient
from src.db.database import close_db_connection, init_db_connection
from src.libs.test_lib import get_expected_results_dict
import pytest
import shutil
from pathlib import Path


class EndpointTestBase:
    """
    Base test class to check whether all the endpoints are up and running
    """

    test_name: str

    def __init__(self, client, test_name: str):
        self.test_name = test_name
        self._check_endpoint(client)

    def _get_test_parts(self, client):
        url = f"http://api_test/test/{self.test_name}"
        print(f"TEST: {self.test_name}")
        print(f"=> url: {url}")
        expected_response = get_expected_results_dict(f"{self.test_name}")
        response = client.get(url)
        return response, expected_response

    def _check_endpoint(self, client):
        response, expected_response = self._get_test_parts(client)
        assert response.status_code == 200
        assert response.json() == expected_response


def test_endpoint_check_api_live(client: TestClient):
    EndpointTestBase(client, "api_live")


def test_endpoint_check_load_db(client: TestClient):
    EndpointTestBase(client, "load_db")


def test_endpoint_check_read_db(client: TestClient):
    EndpointTestBase(client, "read_db")

    # clean db after load/reads
    conn, cur = init_db_connection()
    cur.execute("DROP TABLE test;")
    conn.commit()
    close_db_connection(cur, conn)


def test_endpoint_check_celery(client: TestClient):
    EndpointTestBase(client, "check_celery")
