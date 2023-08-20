from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from script import app

client = TestClient(app)

two_cities = {"cities": [{
    "geonameid": 461698,
    "name": "Sosnovka",
    "asciiname": "Sosnovka",
    "alternatenames": "Sosnovka,Sosnovo,Сосновка",
    "latitude": 60.01667,
    "longitude": 30.35,
    "feature_class": "P",
    "feature_code": "PPLX",
    "country_code": "RU",
    "cc2": "",
    "admin1_code": "66",
    "admin2_code": "",
    "admin3_code": "",
    "admin4_code": "",
    "population": 66227,
    "elevation": "",
    "dem": 23,
    "timezone": "Europe/Moscow",
    "modification_date": "2013-03-29"
},
    {
    "geonameid": 1507332,
    "name": "Dobrovka",
    "asciiname": "Dobrovka",
    "alternatenames": "Dobrovka,Dobrovskiy,Dobryy,Добровка",
    "latitude": 53.3079,
    "longitude": 79.5179,
    "feature_class": "P",
    "feature_code": "PPL",
    "country_code": "RU",
    "cc2": "",
    "admin1_code": "04",
    "admin2_code": "",
    "admin3_code": "",
    "admin4_code": "",
    "population": 0,
    "elevation": "",
    "dem": 171,
    "timezone": "Asia/Barnaul",
    "modification_date": "2012-01-17"
}
],
    "to_the_north": "Dobrovka",
    "equal_timezone": False,
    "difference_timezone": -4
}

two_cities_fail = {
    "detail": "Города не найдены"
}


@pytest.mark.parametrize("city_1, city_2", [("Сосновка", "Добровка"),
                                            ("Прусово", "Рашкино")])
def test_get_two_cities_status_code_good(city_1, city_2):
    url = f'http://127.0.0.1/api/v1/cities?city_1={city_1}&city_2={city_2}'
    response = client.get(url=url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.parametrize("city_1, city_2", [("город_1", "город_2"),
                                            ("город_3", "город_4")])
def test_get_two_cities_status_code_fail(city_1, city_2):
    url = f'http://127.0.0.1/api/v1/cities?city_1={city_1}&city_2={city_2}'
    response = client.get(url=url)
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.parametrize("city_1, city_2", [("Сосновка", "Добровка")])
def test_get_two_cities_body_good(city_1, city_2):
    url = f'http://127.0.0.1/api/v1/cities?city_1={city_1}&city_2={city_2}'
    response = client.get(url=url)
    assert response.json() == two_cities


@pytest.mark.parametrize("city_1, city_2", [("город_1", "город_2")])
def test_get_two_cities_body_good(city_1, city_2):
    url = f'http://127.0.0.1/api/v1/cities?city_1={city_1}&city_2={city_2}'
    response = client.get(url=url)
    assert response.json() == two_cities_fail
