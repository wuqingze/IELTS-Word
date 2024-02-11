# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

print("hello")

#html_template = '''
#<!DOCTYPE html>
#<html>
#<head>
#    <title>英语单词页面</title>
#</head>
#<body>
#    <div>
#        <div display="flex">
#            <div><h3>{}</h3></div>
#            <div><audio controls><source src="{}" type="audio/mp3"></audio></div>
#        </div>
#        <div>{}</div>
#    </div>
#</body>
#</html>
#'''
#
#value1 = "参数1"
#value2 = "参数2"
#value3 = "参数3"
#
#html_result = html_template.format(value1, value2, value3)
#print(html_result)
#
#words = ["Academic"]
#
#for word in words:
#    print(word)
#    url = "https://beta_dict.eudic.net/dicts/en/"+word
#
#    # 发送HTTP请求
#    response = requests.get(url)
#
#    # 检查响应状态码
#    if response.status_code == 200:
#        # 使用BeautifulSoup解析HTML文档
#        soup = BeautifulSoup(response.text, 'html.parser')
#
#        # 使用CSS选择器定位元素
#        target_element = soup.select_one("#exp-head > div > span.phonitic-line > a:nth-child(2)")
#
#        # 检查元素是否存在
#        if target_element:
#            # 获取data-rel属性值
#            data_rel_value = target_element.get("data-rel")
#
#            print("data-rel属性值:", data_rel_value)
#        else:
#            print("未找到目标元素")
#    else:
#        print("请求失败，状态码:", response.status_code)
#
#
