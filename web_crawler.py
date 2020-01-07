import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import requests
import os

'''
html = urlopen("https://huggingface.co/transformers/").read()
html = html.decode('utf-8')
res = re.findall(r'<title>.*</title>', html)
print(res)
'''

''' 爬取百度百科
baike = 'https://baike.baidu.com'
item = ['/item/%E8%A7%82%E9%9F%B3%E6%B4%9E%E6%96%87%E5%8C%96']

for i in range(20):
    url = baike + item[-1]
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html)

    sub_item = soup.find_all('a', {'target': '_blank', 'href': re.compile("^(/item/)(%.{2})+$")})
    print(sub_item)
    if len(sub_item) != 0:
        item.append(random.sample(sub_item, 1)[0]['href'])

    print(i, 'url:', soup.find('h1').get_text())
'''

index = 0

def save_art(url):
    global index
    file_dir = 'D:\\files\defuli\\img\\web_crawler\\'
    html = requests.get(url).text
    soup = BeautifulSoup(html)
    next_tag = soup.find_all('a', {'class': 'f-buttons'})
    next_url = ''
    # 获取next的url
    for tag in next_tag:
        if tag.find('span') == None:
            continue
        p_text = tag.find('span').get_text()
        if p_text == 'Next':
            next_url = tag.get('href')
            break

    # 获取img的url
    img_tag = soup.find_all('img')
    img_url = []
    for tag in img_tag:
        img_url.append(tag.get('data-pin-media'))

    for item_url in img_url:
        try:
            r = requests.get(item_url, stream=True)
        except:
            break
        img_name = index
        index += 1

        with open(file_dir + str(img_name) + '.jpg', 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Save', file_dir + str(img_name) + '.jpg')

    save_art(next_url)

if __name__ == '__main__':
    url = 'https://www.artic.edu/collection'


    save_art(url)
