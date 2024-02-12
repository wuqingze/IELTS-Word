# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


html_template = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>英语单词页面</title>
</head>
<body>
    <div>
        <div display="flex">
            <div><h3>{}</h3></div>
            <div><audio controls><source src="{}" type="audio/mp3"></audio></div>
        </div>
        <div>{}</div>
    </div>
</body>
</html>
'''

page_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>英语单词页面</title>
</head>
<body>
    {}
</body>
</html>
'''

word_template = '''
    <div>
        <div display="flex">
            <div><h3>{}</h3></div>
            <div><audio controls><source src="{}" type="audio/mp3"></audio></div>
        </div>
        <div>{}</div>
    </div>
'''

words = ["Academic", "Endorsement"]

for word in words:
    audio_url = "https://api.frdic.com/api/v2/speech/speakweb?"
    chinese_defenition = ""

    url = "https://beta_dict.eudic.net/dicts/en/"+word

    # 发送HTTP请求
    response = requests.get(url)

    # 检查响应状态码
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML文档
        soup = BeautifulSoup(response.text, 'html.parser')

        # 使用CSS选择器定位元素
        target_element = soup.select_one("#exp-head > div > span.phonitic-line > a:nth-child(2)")

        chinese_defenition_element = soup.select_one("#ExpFCChild")

        # 检查元素是否存在
        if target_element:
            # 获取data-rel属性值
            data_rel_value = target_element.get("data-rel")
        else:
            print("未找到目标元素")

        if chinese_defenition_element.find("hr") is None:
            chinese_defenition_element.append(soup.new_tag("hr"))
        print(page_template.format(word_template.format(word, audio_url+data_rel_value, chinese_defenition_element.prettify())))
    else:
        print("请求失败，状态码:", response.status_code)


