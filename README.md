# Web-Crawler-Art-Prints

## 爬取的网站
本次爬取的内容主要是艺术画，选取了一个比较有名的[艺术画网站](https://www.artic.edu/collection?page=1)，可以打开看一看这个网站网页结构，这样有利于我们编写爬虫的代码。<br>
使用F12查看该网页的源代码，发现所有的图片都在img标签的data-pin-media属性值里，就是一串以https开头、.jpg结尾的网址。我们的目的是获取这串网址然后下载它。<br>

