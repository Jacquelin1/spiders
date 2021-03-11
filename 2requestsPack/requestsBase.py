
import requests
if __name__ == "__main__":

    url = 'https://www.sogou.com/'
    #step_2:发起请求
    #get方法会返回一个响应对象
    response = requests.get(url=url)
    #step_3:获取响应数据.text返回的是字符串形式的响应数据
    page_text = response.text
    print(page_text)