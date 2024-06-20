from baseparser import BaseParser
from database import DataBase
from mixins import ProductDetailMixin
from time import time


class TexnomartParser(BaseParser, ProductDetailMixin, DataBase):
    def __init__(self):
        BaseParser.__init__(self)
        ProductDetailMixin.__init__(self)
        DataBase.__init__(self)
        self.create_categories_table()
        self.create_products_table()


    def get_data(self):
        soup = self.get_soup(self.get_html())
        aside = soup.find('ul', class_='first-list')
        categories = aside.find_all('li', class_='h-12')
        for category in categories:
            category_title = category.find('div',class_='d-flex').get_text()
            print(category_title)
            # self.save_category(category_title)
            category_link = self.host + category.find('div',class_='d-flex').get('src')
            print(category_link)
            # self.products_page_parser(category_link, category_title)


def start_parsing():
    parser = TexnomartParser()
    start = time()
    parser.get_data()
    finish = time()
    print(f'Парсер отработал за {finish - start} секунд')

start_parsing()