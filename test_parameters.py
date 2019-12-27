"""
Autore : andreabisello at 27/12/2019

"""

import pytest
import requests


@pytest.mark.parametrize('endpoint', [
    "https://www.google.it",
    "https://www.google.com"
])
def test_parametrized(endpoint):
    """
    this will create two tests, one for every value of the endpoint parameter
    :param endpoints:
    :return:
    """
    print("checking : " + endpoint)
    assert requests.get(endpoint).status_code == 200

@pytest.fixture(scope="session")
def get_endpoints():
    return [
        "https://www.google.it",
        "https://www.google.com"
    ]

def test_using_fixture(get_endpoints):
    """
    this will assert the result of the fixture
    :param get_endpoints:
    :return:
    """
    assert get_endpoints == [
        "https://www.google.it",
        "https://www.google.com"
    ]

@pytest.mark.parametrize('endpoint', get_endpoints)
def test_parametrizing_using_fixture(endpoint):
    """
    this should load data from get_endpoints fixture and pass every values of get_endpoints as endpoint value
    :param endpoint:
    :return:
    """
    print("checking : " + endpoint)
    assert requests.get(endpoint).status_code == 200

