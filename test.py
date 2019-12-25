import re
import requests
from bs4 import BeautifulSoup
import lxml
def request_dandan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def main(page):
    url = 'http://category.dangdang.com/pg'+ str(page + 1) +'-cp01.03.38.00.00.00'
    html = request_dandan(url)
    items = parse_result(html)

    for item in items:
        write_item_to_file(item)





