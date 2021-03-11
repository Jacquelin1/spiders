
#需求：爬取58二手房中的房源信息
from lxml import etree
import requests
import json

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4328.0 Safari/537.36'
    }
    url='https://sh.58.com/ershoufang/'
    page_text=requests.get(url=url,headers=headers).text

    tree=etree.HTML(page_text)

    li_list=tree.xpath('//ul[@class="house-list-wrap"]/li')
    fp=open('58.txt','w',encoding='utf-8')
    for li in li_list:
        title=li.xpath('./div[2]/h2/a/text()')[0]
        print(title)
        fp.write(title+'\n')