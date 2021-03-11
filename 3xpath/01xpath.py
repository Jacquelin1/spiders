
from lxml import etree
import requests
import json

if __name__ == "__main__":
    tree=etree.parse('test.html')
    # - /: 表示的是从根节点开始定位。表示的是一个层级。
    # r=tree.xpath('/html/body/div')

    # //:表示的是多个层级。可以表示从任意位置开始定位。
    # r=tree.xpath('/html//div')
    # r=tree.xpath('//div')
    

    # 属性定位： // div[ @ class ='song'] tag[@ attrName="attrValue"]
    # r=tree.xpath('//div[@class="song"]')

    # 索引定位： // div[ @ class ="song"] / p[3] 索引是从1开始的。
    # r=tree.xpath('//div[@class="tang"]/ul/li[5]/a/text()')[0]
    # r=tree.xpath('//div[@class="tang"]//li[5]//text()')[0]  # 等同上式

    # - / text() 获取的是标签中直系的文本内容
    # - // text() 标签中非直系的文本内容（所有的文本内容）
    # r=tree.xpath('//li[7]/i/text()')
    # r=tree.xpath('//li[7]//text()')  # 等同上式
    # r=tree.xpath('//div[@class="tang"]//text()')

    # 取属性：/@attrName == > img / src
    r=tree.xpath('//div[@class="song"]/img/@src')




    print(r)
