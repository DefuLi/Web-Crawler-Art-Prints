# Web-Crawler-Art-Prints

## 1 爬取的网站
本次爬取的内容主要是艺术画，选取了一个比较有名的[艺术画网站](https://www.artic.edu/collection?page=1)，可以打开看一看这个网站网页结构，这样有利于我们编写爬虫的代码。<br>

## 2 网页结构
使用F12查看该网页的源代码，发现所有的图片都在img标签的data-pin-media属性值里，就是一串以https开头、.jpg结尾的网址。我们的目的是获取这串网址然后下载它。<br>

<p align="center">
  <img src="https://github.com/DefuLi/Web-Crawler-Art-Prints/blob/master/img1.png" width="1000" height="500">
  <p align="center">
    <em>网页图片位置</em>
  </p>
</p>
<br>

```python
    # 获取img的url
    img_tag = soup.find_all('img')
    img_url = []
    for tag in img_tag:
        img_url.append(tag.get('data-pin-media'))
```

接着我们还要获取到的一个内容是通往下一页的链接，因为当本页的图片全都爬取完毕后，程序需要接着对下一页进行爬取。通过观察该网页，发现了Next按钮。Next按钮位于a标签的href属性值中，但是一个网页上有很多a标签，要想唯一确定Next按钮的a标签，还需要使用a标签下的span标签的文本内容为Next来确定。<br>

<p align="center">
  <img src="https://github.com/DefuLi/Web-Crawler-Art-Prints/blob/master/img2.png" width="1000" height="500">
  <p align="center">
    <em>网页Next位置</em>
  </p>
</p>
<br>

```python
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
```

## 3 保存爬取图片
file_dir是自定义的保存图片的路径，爬取到每一张图片后将其写入到文件中。<br>
<p align="center">
  <img src="https://github.com/DefuLi/Web-Crawler-Art-Prints/blob/master/img3.png" width="1000" height="500">
  <p align="center">
    <em>爬取到的图片</em>
  </p>
</p>
<br>

```python
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
```

## 4 所用环境
本次使用的是BeautifulSoup、requests两个关键库，BeautifulSoup库提供了解析网页的功能，requests库提供了根据url链接访问并获取html对象的功能。<br>

```python
# requirement.txt
beautifulsoup4==4.8.2
certifi==2019.11.28
chardet==3.0.4
idna==2.8
requests==2.22.0
soupsieve==1.9.5
urllib3==1.25.7
```

注：本程序采用的循环递归的方式进行爬虫，没有设置递归的出口，所以如果不想爬虫了，手动中断程序即可。
