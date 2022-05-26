import requests as req
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

title = ['課名', '作者', '價格', '預購駕', '販售數']
ws.append(title)
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}
for index in range(28):
    url = 'https://api.hahow.in/api/courses?limit=24&page='
    url = url + str(index)
    print(url)
    r = req.get(url, headers=header)
    print(r)
    root_json = r.json()
    for data in root_json['data']:
        coures = []
        coures.append(data['title'])
        coures.append(data['owner']['name'])
        coures.append(data['price'])
        coures.append(data['preOrderedPrice'])
        coures.append(data['numSoldTickets'])

        ws.append(coures)

wb.save('data.xlsx')
