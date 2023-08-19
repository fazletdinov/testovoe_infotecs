from typing import Optional, Union

from pydantic import BaseModel


class GeonameModel(BaseModel):
    geonameid: Optional[int]
    name: Optional[str]
    asciiname: Optional[str]
    alternatenames: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    feature_class: Optional[str]
    feature_code: Optional[str]
    country_code: Optional[str]
    cc2: Optional[str]
    admin1_code: Optional[str]
    admin2_code: Optional[str]
    admin3_code: Optional[str]
    admin4_code: Optional[str]
    population: Optional[int]
    elevation: Union[int, str]
    dem: Optional[int]
    timezone: Optional[str]
    modification_date: Optional[str]
