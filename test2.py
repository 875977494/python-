import re
import requests
from bs4 import BeautifulSoup
import lxml
import time

def request_dangdang(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def get_response(page):
    url = 'http://category.dangdang.com/pg' + str(page) + '-cp01.03.38.00.00.00.html'
    html = request_dangdang(url)
    soup = BeautifulSoup(html, 'lxml')
    for item in range(60):
        book_itme = 'line'+str(item + 1)
        name = soup.find_all(class_=book_itme)
        get_info(name[0])
    # print(name[0])

def get_info(name):
    book_title = name.find(class_="pic").get("title")
    comment_count = name.find(class_="search_comment_num").string
    book_price = name.find(class_="price").span.string
    book_intr = name.find(class_="name").string
    print(book_title + '|' + comment_count + '|' + book_price + '|' + book_intr)

for page in range(1, 100):
    get_response(page)





