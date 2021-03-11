
import requests
import json
if __name__ == "__main__":

    # 1.指定url
    url = 'https://movie.douban.com/j/chart/top_list'
    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    # cookie={
    #     douban-fav-remind=1; ll="108296"; bid=z4J5mrlL03Q; dbcl2="182531807:GJ+NyVan3oM";
    # push_noty_num=0; push_doumail_num=0; __yadk_uid=BQG2ICIitzwTJiZTeKloWxZhhh5Ep41J;
    # _vwo_uuid_v2=DCC0A19F3AF1C9F45761BEE3F30FB1A07|423fb71672dfce125d9d5c3c0853b45b;
    # ck=P-s-; __utma=30149280.2120116193.1605698521.1605698521.1605754722.2;
    # __utmc=30149280; __utmz=30149280.1605754722.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic;
    # __utmv=30149280.18253; __utmb=30149280.4.10.1605754722;
    # _pk_ref.100001.4cf6=["","",1605754747,"https://www.douban.com/"];
    # _pk_ses.100001.4cf6=*; __utmc=223695111; __gads=ID=806a1fe3915ca909-22a47f3bd5c40027:T=1605754795:RT=1605754795:S=ALNI_MaeIhqICMz0v_xeaidjUe8d2Tg3Aw; __utma=223695111.1097241276.1605698555.1605754747.1605755723.3; __utmb=223695111.0.10.1605755723; __utmz=223695111.1605755723.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_id.100001.4cf6=e78d63c6e3877204.1605698555.2.1605756346.1605698714.}
    param={
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',  # 从库中的第几部电影去取
        'limit': '20',  # 一次取出的个数
    }
    response = requests.get(url=url, params=param, headers=headers)

    # list_data = response.json()
    list_data=response.text

    # fp = open('./douban.json', 'w', encoding='utf-8')
    # json.dump(list_data, fp=fp, ensure_ascii=False)
    fileName='./douban.json'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(list_data)
    print(fileName,"success")

    # print("success")


    