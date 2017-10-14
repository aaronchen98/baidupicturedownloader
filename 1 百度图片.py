#-*- coding:utf-8 -*-
import re
import requests
import os

key = str(input('请输入想要找的图片的关键词: '))
page = int(input('请输入要下载的页数: '))
path = str(input('请输入要保存的文件夹: '))

if path[-1] != r'/':
    path += '/'

def download_pic(url, num, path):
    html = requests.get(url).text
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    for each in pic_url:
        print('正在下载: ' + each)
        try:
            pic = requests.get(each, timeout=5).content
        except:
            print('【错误】当前图片无法下载')
            continue
        string = path + str(num) + '.jpg'
        fp = open(string, 'wb')
        fp.write(pic)
        fp.close()
        num += 1

for i in range(page):
    num = len(os.listdir(path))
    url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + key + '&pn=' + str(i*20)
    download_pic(url, num, path)

print('\n')
print('Done!')