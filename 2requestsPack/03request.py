

import requests
import json
if __name__ == "__main__":

    # 1.指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4328.0 Safari/537.36'
    }
    #3.post请求参数处理（同get请求一致）
    word = input('enter a word:')
    data = {
        'kw':word
    }
    response=requests.post(url=post_url,data=data,headers=headers)
    dict_obj=response.json()
    fileName=word+".json"
    fp=open(fileName,'w',encoding='utf-8')
    json.dump(dict_obj,fp=fp,ensure_ascii=False)
    print("success")
