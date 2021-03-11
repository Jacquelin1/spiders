
from lxml import etree
import requests
import json

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4328.0 Safari/537.36'
    }
    university_list=['505']
    url = 'https://www1.nm.zsks.cn/xxcx/gkcx/lqmaxmin_20.jsp'
    # page_text = requests.get(url=url, headers=headers).text
    # tree = etree.HTML(page_text)
    all_max=[]
    all_min=[]
    all_num=[]
    for uni in university_list:
        data={
            'm_yxdh':uni,
            'query':'提交',
            'pcdm':'1',
            'kldm':'B',
            'pxfs':'2',
        }
        page_text = requests.get(url=url, headers=headers,data=data,proxies={"https":'222.110.147.50:3128'}).text
        tree = etree.HTML(page_text)
        fp = open('./page_text.txt', 'w', encoding='utf-8')
        fp.write(page_text)
        print("success")
        first_fill_max = tree.xpath('/html/body/center/p[1]/table/tbody/tr[2]/td[2]/p/text()')
        first_fill_min = tree.xpath('/html/body/center/p[1]/table/tbody/tr[2]/td[3]/p/text()')
        num = tree.xpath('/html/body/center/p[1]/table/tbody/tr[2]/td[4]/p/text()')
        all_max.append(first_fill_max)
        all_min.append(first_fill_min)
        all_num.append(num)
    print(all_max)
    print(all_min)
    print(all_num)
