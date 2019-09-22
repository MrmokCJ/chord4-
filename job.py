# import requests
# import json

# url = "http://202.118.65.2/app/portals/newslist.html?newsColumn=08"



# headers = {
#     'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
#     'Accept-Encoding': "gzip, deflate",
#     'Accept-Language': "zh-CN,zh;q=0.9",
#     'Cache-Control': "max-age=0",
#     'Connection': "keep-alive",
#     'Cookie': "UM_distinctid=16ac4931385883-016498b99be17d-e323069-144000-16ac4931386852; CNZZDATA1274898983=477025760-1558072322-http%253A%252F%252Fcareer.dlut.edu.cn%252F%7C1567342980",
#     'Host': "202.118.65.2",
#     'Referer': "http://202.118.65.2/app/portals/newslist.html?newsColumn=09",
#     'Upgrade-Insecure-Requests': "1",
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
#     'Postman-Token': "0685e059-7211-41bd-ad8e-0a53e6cdf590,3d9b6464-4994-496f-8aaa-d8317bdafed6",
#     'cache-control': "no-cache"
#     }
# # for i in range(0,6):
# response = requests.request("GET", url, headers=headers)
# print(response.text)

# #     datas = json.loads(response.text)
# #     for data in datas["newsDTOS"]:
# #         with open('job.txt','a',encoding='utf-8')as f:
# #             f.write(data['title'])
# #             f.write('\n')
# #             f.write(data["recruiterDate"])
# #             f.write('\n'*2)
for i in range(1,2):
    with open('dlut/dlut'+str(i)+'.html','r',encoding = 'utf-8')as f:
        c = f.read()
        print(c)