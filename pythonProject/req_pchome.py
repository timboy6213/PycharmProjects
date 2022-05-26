import requests as req

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}
for index in range(1, 20):
    url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=ssd&page='
    urls = url + str(index)+'&sort=sale/dc'
    print(urls)
    r = req.get(urls, headers=header)
    root_json = r.json()
    # print("-------------------------test------------")
    # num = 1
    for data in root_json['prods']:
         print(str(data['Id'])+"，"+data['name']+":"+str(data['price']))
