# _*- coding: utf-8 -*-
'''
从豆瓣网获得相关电影信息
'''

import urllib
import json
import time
import web

movie_ids=[]

# 地址由豆瓣API提供
# 用以获得豆瓣电影排行榜前250部电影列表
# 该地址也可直接在浏览器中查看

'''
API还有两个参数：（json串中可以看出来）
count: 每次请求的电影列表数，默认20
start: 从那条记录开始取值
'''
# 从 0 到 250（不包含250），间隔 50
for index in range(0, 250, 50):
    # print index
    response=urllib.urlopen('http://api.douban.com/v2/movie/top250?start=%d&count=50' %index)
    # 获得json格式的数据
    data=response.read()
    # print data

    # 将 json 串转换成 dict 对象
    data_json=json.loads(data)

    # subjects 节点代表电影列表
    movie_top250=data_json['subjects']

    for movie in movie_top250:
        movie_ids.append(movie['id'])
        # print movie['id'], movie['title']

    # 每次循环过后，停顿3秒
    time.sleep(3)

# print movie_ids

db=web.database(dbn='sqlite', db='MovieSite.db')

# 将数据插入表里
def add_movie(data):
    movie=json.loads(data)
    
    db.insert(
        'movie',
        id=int(movie['id']),
        title=movie['title'],
        origin=movie['original_title'],
        url=movie['alt'],
        rating=movie['rating']['average'],
        image=movie['images']['large'],
        directors=','.join([d['name'] for d in movie['directors']]),
        casts=','.join([c['name'] for c in movie['casts']]),
        year=movie['year'],
        genres=','.join(movie['genres']),
        countries=','.join(movie['countries']),
        summary=movie['summary'],
    )

count=0
for id in movie_ids:
    print count
    response=urllib.urlopen('http://api.douban.com/v2/movie/subject/%s' %id)
    data=response.read()
    add_movie(data)
    count+=1
    time.sleep(3)
