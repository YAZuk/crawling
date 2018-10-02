from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from . import settings


DeclarativeBase = declarative_base()


def db_connect():
    """
        Коннект к базе
    """
    return create_engine(URL(**settings.DATABASE))


def create_product_table(engine):
    """
        Создание таблиц
    :param engine:
    :return:
    """
    DeclarativeBase.metadata.create_all(engine)


class CategoryKomus(DeclarativeBase):
    """
        Описание таблицы Категории Комус
    """
    __tablename__ = "komus_categories"

    id = Column(Integer, primary_key=True)
    title = Column('title', Text)
    url = Column('url', Text, nullable=True, unique=True)


class CategoryYandexMarket(DeclarativeBase):
    """
        Описание таблицы Категории Яндекс-Маркет
    """
    __tablename__ = "yandex_market_categories"

    id = Column(Integer, primary_key=True)
    title = Column('title', Text)
    url = Column('url', Text, nullable=True)


class ProductKomus(DeclarativeBase):
    """
        Описание таблицы Продукты
    """
    __tablename__ = "komus_products"

    id = Column(Integer, primary_key=True)
    title = Column('title', Text)
    url = Column('url', Text, nullable=True)
    price = Column('price', Float, nullable=True)
    # category_id = Column('category_id', Integer,
    #                      ForeignKey("komus_categories.id"), nullable=False)