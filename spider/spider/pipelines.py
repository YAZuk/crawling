# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
import sqlalchemy.exc
from .models import ProductKomus, CategoryKomus,db_connect, create_product_table


class CategoryKomusPipeline(object):
    """"""
    def __init__(self):
        """
        """
        engine = db_connect()
        create_product_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
            Обработка item
        """
        session = self.Session()
        category = CategoryKomus(**item)

        try:
            session.add(category)
            session.commit()
        except sqlalchemy.exc.IntegrityError:
            pass

        return item


class ProductPipeline(object):
    """"""
    def __init__(self):
        """
        """
        engine = db_connect()
        create_product_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        """
        session = self.Session()
        product = ProductKomus(**item)

        try:
            session.add(product)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item