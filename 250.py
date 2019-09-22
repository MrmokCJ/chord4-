from urllib import request
from lxml import etree
import requests


class crawler():
    
    url = "https://movie.douban.com/top250"

    headers = {
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "d453accf-1d2e-4164-b55f-8a97dbb94d00,0cf6a9bd-6ffa-4384-b839-0a7588149a16",
        'Host': "movie.douban.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    def craw(self,i):
        movie_inform = {}
        self.i = i
        a = 0
        url = self.url
        headers = self.headers
        querystring = {"start":str(i*25),"filter":""}
        response = requests.request("GET", url, headers=headers, params=querystring)
        tree = etree.HTML(response.text)
        
        datas = tree.xpath('//ol[@class="grid_view"]/li')

        for data in datas:
            movie_inform['data_title']=data.xpath('div/div[2]/div[@class="hd"]/a/span[1]/text()')
            movie_inform['data_director']=data.xpath('div/div[2]/div[@class="bd"]/p[1]/text()')
            movie_inform['data_stars']=data.xpath('div/div[2]/div[@class="bd"]/div/span[2]/text()')
            movie_inform['data_num']=data.xpath('div/div[2]/div[@class="bd"]/div/span[4]/text()')
            movie_inform['data_url']=data.xpath('div[1]/div[1]/a/img/@src')
            pic_name = r'C:\Users\承建\Downloads\Compressed\junior_spider-master\08-BBS\img\ '+str(i*25+a+1)+'.jpg'
            with open('movie.txt','a',encoding='utf-8') as f:
                f.write('No:'+str(i*25+a+1)+movie_inform['data_title'][0]+'\n')
                f.write('电影信息:'+movie_inform['data_director'][0]+'\n')
                f.write('评分:'+movie_inform['data_stars'][0]+'\n')
                f.write('评价人数:'+movie_inform['data_num'][0]+'\n'*2)
            # request.urlretrieve(movie_inform['data_url'][0],pic_name)
            # print("No."+str(25*i+a+1))
            # print("电影名称:",movie_inform['data_title'])
            # print("电影信息:",movie_inform['data_director'])
            # print('评分：', movie_inform['data_stars'])
            # print("评价人数:",movie_inform['data_num'])
            # print(movie_inform['data_url'])
            
            a+=1
            
       


if __name__ == '__main__':
    crawlers=crawler()
    for i in range(0,10):
        crawlers.craw(i)

