
# UA伪装

import requests
if __name__ == "__main__":
    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'https://www.sogou.com/web'
    # 处理url携带的参数：封装到字典中
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    response=requests.get(url=url,params=param,headers=headers)
    page_text=response.text
    fileName=kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,"success")