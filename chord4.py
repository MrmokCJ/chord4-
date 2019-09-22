# from urllib.request import urlopen
from lxml import etree
from bs4 import BeautifulSoup
# html = urlopen('https://chord4.com/main/hot100')
# bs = BeautifulSoup(html.read,'html.parser')
import requests
import re


#定义一个获取目标url里HTML内容的一个方法
def get_url(url):
    

    headers = {'User-Agent':'Mozilla/5.0 3578.98 Safari/537.36'}

    response = requests.request("GET", url, headers=headers)
#为了解决脑人的中文编码问题
    response.encoding = 'utf-8'
    return response
    


# nameList = bs.find_all('ol')


if __name__ == '__main__':
    url = "https://chord4.com/main/hot100"
    response = get_url(url)
    tree = etree.HTML(response.text)
    nameList = tree.xpath('//*[@id="search_result"]/ol/li')
    # #将歌曲名、作者、网址一一选区出来
    # tree_1= etree.HTML(tab_url.text)
    # tab = tree_1.xpath('//*[@id="tabs"]/div[4]/div[1]/pre/text()')
    # print(tab)
    for i in nameList:
        name = i.xpath('a[1]/text()')
        author = i.xpath('a[2]/@title')
        url_1 = i.xpath('a[1]/@href')
        tab_url = get_url(url_1[0])
        tree_1 = etree.HTML(tab_url.text)
        tab = tree_1.xpath('//*[@id="tabs"]/div[4]/div[1]/pre/text()')
        domain = r'C:\Users\承建\Downloads\Compressed\junior_spider-master\08-BBS\.vscode\chord4'
        filename = domain +'/'+ str(name[0])+'_' +str(author[0]) +'tab.txt'
        try:
            with open(filename,'w',encoding='utf-8')as f:
                f.writelines(str(tab))
        except:
            continue
