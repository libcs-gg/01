# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# 微博热搜代码，复制到我们作业运行框，点击运行就可以啦。（最后两行报错可检查是否缩进四个空格）
import requests
from lxml import etree
import time

url = 'https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr='
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/80.0.3987.132 Safari/537.36',
    'Cookie':'SUB=_2AkMV7Mtnf8NxqwJRmPERz2vlbIV_zwHEieKjsDq8JRMxHRl-yj8XqmIetRB6PmzliA8kf-bjLxSPsQEi8fJFc1Da4-hk; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWTHHdJ5CQD05s3Pb1zeIcy; _s_tentry=passport.weibo.com; Apache=7885029914706.894.1655718993251; SINAGLOBAL=7885029914706.894.1655718993251; ULV=1655718993283:1:1:1:7885029914706.894.1655718993251:'}
resp = requests.get(url, headers=header)
resp1 = resp.content.decode(encoding='utf-8', errors='ignore')
resp2 = etree.HTML(resp1)

title = resp2.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr/td/a/text()')
print(time.strftime("%F,%R") + '微博热搜\n')
# print(title)
# input("ok?")
for i in range(15):
    print('  '.join([title[i]]), '\n')
    time.sleep(3)


input('next is the second ')



import requests
res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
sanguo=res.text
print(sanguo[:100])
