
# 药监局化妆品生产许可
import requests
import json

if __name__ == "__main__":

# 网站往下拉URL没变化就是ajx,看xhr

    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4328.0 Safari/537.36'
    }
    id_list=[]
    all_data_list=[]
    url_id = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

# 1.指定获取单个ID的url
    for page in range(1,6):
        data={
            'on':' true',
            'page':page,
            'pageSize':' 15',
            'productName':'',
            'conditionType':' 1',
            'applyname':'',
            'applysn':'',
        }
        json_ids=requests.post(url=url_id,headers=headers,data=data).json()
        for dic in json_ids["list"]:
            id_list.append(dic["ID"])

#获取企业详情数据
    url_detail='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data={
            'id':id
        }
        detail_json=requests.post(url=url_detail,headers=headers,data=data).json()
        all_data_list.append(detail_json)

#持久化存储all_data_list
    fp=open('./all.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)
    print("success")







