from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData

sqlite_database = "sqlite:///database/database.db"

engine = create_engine(sqlite_database)

metadata_obj = MetaData()

Session = sessionmaker(engine, expire_on_commit=False)


def get_db() -> Generator:
    try:
        session = Session()
        yield session
    finally:
        session.close()
