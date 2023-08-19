from datetime import datetime
from http import HTTPStatus

import pytils
from dateutil.relativedelta import relativedelta
from fastapi import HTTPException
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from pytz import timezone
from sqlalchemy import select, union_all
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from database.models import geoname
from database.schema import GeonameModel


def _get_geoname(geoname_id: int, db: Session) -> GeonameModel:
    with db as session:
        with session.begin():
            query = select(geoname).where(geoname.c.geonameid == geoname_id)
            result = session.execute(query)
            return result.fetchone()


def _get_list_cities(db: Session) -> Page[GeonameModel]:
    with db as session:
        with session.begin():
            result = paginate(db, select(geoname))
            return result


def _get_translate(city1, city2):
    city_us_1 = pytils.translit.translify(city1)
    city_us_2 = pytils.translit.translify(city2)
    return city_us_1, city_us_2


def _get_two_cities(city_ru_1, city_ru_2, db):
    with db as session:
        with session.begin():
            city_us_1, city_us_2 = _get_translate(city_ru_1, city_ru_2)
            query = union_all(select(geoname, func.max(geoname.c.population)).where(geoname.c.name == city_us_1).group_by(geoname.c.name),
                              select(geoname, func.max(geoname.c.population)).where(geoname.c.name == city_us_2).group_by(geoname.c.name))

            result = session.execute(query)
            two_cities = result.fetchall()
            data = _get_bool_value(two_cities)
            return data


def _get_bool_value(list_cities):
    if list_cities == []:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail="Города не найдены")
    data = {"cities": list_cities}
    if len(list_cities) > 1:
        name_city_1 = list_cities[0][1]
        name_city_2 = list_cities[1][1]
        timezone_1 = list_cities[0][17]
        timezone_2 = list_cities[1][17]
        latitude_1 = list_cities[0][5]
        latitude_2 = list_cities[1][5]
        if latitude_1 and latitude_2:
            if latitude_1 >= latitude_2:
                data["to_the_north"] = name_city_1
            else:
                data["to_the_north"] = name_city_2
        if timezone_1 and timezone_2:
            if timezone_1 == timezone_2:
                data["equal_timezone"] = True
            else:
                data["equal_timezone"] = False
                diff_timezone = _diff_timezone(timezone_1, timezone_2)
                data["difference_timezone"] = diff_timezone
    return data


def _diff_timezone(home, away):
    utcnow = timezone('utc').localize(datetime.utcnow())
    here = utcnow.astimezone(timezone(home)).replace(tzinfo=None)
    there = utcnow.astimezone(timezone(away)).replace(tzinfo=None)
    offset = relativedelta(here, there)
    return float(offset.hours)
