import requests
import pytest

@pytest.fixture
def fixture():
    return requests.get('https://stepik.org/lesson/25969/step/1?unit=196192')

def test_status(fixture):
    assert fixture.status_code == 200

def test_headers(fixture):
    assert fixture.headers['Server'] == 'QRATOR'
