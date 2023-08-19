from http import HTTPStatus
from typing import Union

from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page
from sqlalchemy.orm import Session

from database.database import get_db
from database.schema import GeonameModel
from src.source import _get_geoname, _get_list_cities, _get_two_cities

router_v1 = APIRouter()


@router_v1.get("/list_cities", response_model=Page[GeonameModel])
def get_list_cities_(db: Session = Depends(get_db)):
    list_cities = _get_list_cities(db)
    return list_cities


@router_v1.get("/cities/", response_model=Union[dict[str,
                                                     Union[float,
                                                           bool,
                                                           str,
                                                           list[GeonameModel]
                                                           ]],
                                                str])
def get_two_cities(city_1: str, city_2: str, db: Session = Depends(get_db)):
    two_cities = _get_two_cities(city_1, city_2, db)
    return two_cities


@router_v1.get("/cities/{geoname_id}", response_model=GeonameModel)
def get_geoname(geoname_id: int, db: Session = Depends(get_db)):
    geoname = _get_geoname(geoname_id, db)
    if geoname is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail=f"Город с id {geoname_id} не существует")
    return geoname
