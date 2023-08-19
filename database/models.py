from sqlalchemy import Float, Integer, String
from sqlalchemy.schema import Column, Table

from database.database import engine, metadata_obj

geoname = Table(
    "geoname",
    metadata_obj,
    Column("geonameid", Integer, primary_key=True),
    Column("name", String),
    Column("asciiname", String),
    Column("alternatenames", String),
    Column("latitude", Float),
    Column("longitude", Float),
    Column("feature_class", String),
    Column("feature_code", String),
    Column("country_code", String),
    Column("cc2", String),
    Column("admin1_code", String),
    Column("admin2_code", String),
    Column("admin3_code", String),
    Column("admin4_code", String),
    Column("population", Integer),
    Column("elevation", Integer),
    Column("dem", Integer),
    Column("timezone", String),
    Column("modification_date", String),
    autoload_with=engine,
)
