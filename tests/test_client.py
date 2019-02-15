import pytest

from pyincore import IncoreClient


@pytest.fixture
def cred():
    c = []
    try:
        with open(".incorepw", 'r') as f:
            c = f.read().splitlines()
        return c
    except EnvironmentError:
        return None


def test_client_success(cred):
    """
    testing successful login
    """
    if cred is None:
        assert False, ".incorepw does not exist!"
    client = IncoreClient("http://incore2-services-dev.ncsa.illinois.edu:8888", cred[0], cred[1])
    assert client.status is "success"


def test_client_fail():
    """
    testing failed login
    """
    client = IncoreClient("http://incore2-services-dev.ncsa.illinois.edu:8888", "xxx", "xxxx")
    assert client.status is "fail"

