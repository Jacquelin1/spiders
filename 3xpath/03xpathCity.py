

#项目需求：解析出所有城市名称https://www.aqistudy.cn/historydata/
from lxml import etree
import requests
import json

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4328.0 Safari/537.36'
    }
    url='https://www.aqistudy.cn/historydata/'
    page_text=requests.get(url=url,headers=headers).text
    tree=etree.HTML(page_text)

    a_list=tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city=[]
    for a in a_list:
        city_name=a.xpath('./text()')[0]
        all_city.append(city_name)
    print(all_city, len(all_city))
