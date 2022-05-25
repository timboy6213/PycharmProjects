import time

import requests as req
from bs4 import BeautifulSoup
from openpyxl import Workbook

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}
for index in range(5):
    url = 'https://shopee.tw/api/v4/search/search_items?by=relevancy&keyword=%E8%80%81%E5%B9%B2%E5%AA%BD%E9%A6%99%E8%BE%A3%E8%84%86%E6%B2%B9%E8%BE%A3%E6%A4%92&limit=60&newest=60&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2&page='
    url = url + str(index)
    r = req.get(url, headers=header)
    root_json = r.json()
    print("-----------------test" + str(index ) + "--------")
    num = 1
    for data in root_json['items']:
        print(str(data['item_basic']['shopid']) + "，" + data['item_basic']['name'] + ":" + str(data['item_basic']['price']))

