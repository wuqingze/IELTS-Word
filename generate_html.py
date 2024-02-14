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

def generate_page(words):
    word_html_list = []
    audio_prefix_url = "https://api.frdic.com/api/v2/speech/speakweb?"
    word_prefix_url = "https://beta_dict.eudic.net/dicts/en/"
    for word in words:
        word_url = word_prefix_url+word
        chinese_defenition = ""
        audio_url = ""

        # 发送HTTP请求
        response = requests.get(word_url)

        # 检查响应状态码
        if response.status_code == 200:
            # 使用BeautifulSoup解析HTML文档
            soup = BeautifulSoup(response.text, 'html.parser')

            # 使用CSS选择器定位元素
            audio_element = soup.select_one("#exp-head > div > span.phonitic-line > a:nth-child(2)")
            chinese_defenition_element = soup.select_one("#tabs--11")
            
            # 检查元素是否存在
            if audio_element is not None and chinese_defenition_element is not None:
                # 获取data-rel属性值
                data_rel_value = audio_element.get("data-rel")
                audio_url = audio_prefix_url + data_rel_value

            if chinese_defenition_element is not None:
                # 找到要删除的目标元素
                target_div = chinese_defenition_element.find('a')

                # 删除目标元素
                if target_div:
                    target_div.decompose()

                chinese_defenition = chinese_defenition_element.prettify()
        word_html_list.append(word_template.format(word, audio_url, chinese_defenition))

    return html_template.format("".join(word_html_list))
