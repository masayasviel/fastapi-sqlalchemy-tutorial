import os
from typing import Annotated, Generator

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


def create_db_url(
    *,
    engine: str,
    user: str,
    password: str,
    host: str,
    db_name: str,
    init_command: str,
    port: str = "3306",
    charset: str = "utf8mb4",
) -> str:
    return f"{engine}://{user}:{password}@{host}:{port}/{db_name}?charset={charset}&init_command={init_command}"


SQLALCHEMY_DATABASE_URL = create_db_url(
    engine='mysql',
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    host=os.environ['MYSQL_HOST'],
    db_name=os.environ['MYSQL_DATABASE'],
    init_command="SET sql_mode='STRICT_TRANS_TABLES'",
    port=os.environ.get('MYSQL_PORT', 3306),
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SessionDep = Annotated[Session, Depends(get_session)]
