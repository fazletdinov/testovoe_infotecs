from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from script import app

geoname: dict = {"geonameid": 12537084, "name": "Urochishche Krestovyy Kust",
                 "asciiname": "Urochishche Krestovyy Kust",
                 "alternatenames": "Urochishche Krestovyy Kust,Urochishhe Krestovyj Kust,Урочище Крестовый Куст",
                 "latitude": 51.48569, "longitude": 40.0862, "feature_class": "L", "feature_code": "AREA",
                 "country_code": "RU", "cc2": "", "admin1_code": "86", "admin2_code": "", "admin3_code": "", "admin4_code": "",
                 "population": 0, "elevation": "", "dem": 166, "timezone": "Europe/Moscow", "modification_date": "2023-06-16"}

geoname_fail: dict = {'detail': 'Город с id 123 не существует'}

client: TestClient = TestClient(app)


@pytest.mark.parametrize("geoname_id", [(12537084), (12537160),
                                        (12537399), (451747)])
def test_get_geoname_status_code(geoname_id):
    url = f'http://127.0.0.1/api/v1/cities/{geoname_id}'
    response = client.get(url=url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize("geoname_id", [(12), (123), (67),
                                        (89), (77)])
def test_geoname_fail_status_code(geoname_id):
    url = f'http://127.0.0.1/api/v1/cities/{geoname_id}'
    response = client.get(url=url)
    print(response.status_code)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_geoname_body():
    geoname_id = 12537084
    url = f'http://127.0.0.1/api/v1/cities/{geoname_id}'
    response = client.get(url=url)
    assert response.json() == geoname


def test_geoname_fail_body():
    geoname_id = 123
    url = f'http://127.0.0.1/api/v1/cities/{geoname_id}'
    response = client.get(url=url)
    assert response.json() == geoname_fail
