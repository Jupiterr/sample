# coding=utf-8

import re
import json

body = """{"date":"20150315","stories":[{"images":["http:\/\/pic3.zhimg.com\/a2f08422750b5a7d40bf748adcf6cb82.jpg"],"type":0,"id":4593332,"ga_prefix":"031517","title":"随便分析一下，发现当年的人类简直就是动物界王思聪"},{"images":["http:\/\/pic4.zhimg.com\/9e4f6bb4b1c4c18aa28d9839b1b1da67.jpg"],"type":0,"id":4581220,"ga_prefix":"031516","title":"描述香水的味道，可以用到这些术语"},{"title":"你好，你长得也太神了吧，你是谁设计的！（多图）","ga_prefix":"031515","images":["http:\/\/pic3.zhimg.com\/a222c2b4e3e3672dcbc40152502bff46.jpg"],"multipic":true,"type":0,"id":4593600},{"images":["http:\/\/pic1.zhimg.com\/9be4108aa080d4df8cf6e884e3b0f010.jpg"],"type":0,"id":4593141,"ga_prefix":"031514","title":"字写得丑可能是一种病吗？"},{"images":["http:\/\/pic3.zhimg.com\/bcda42b627f0ff6e34b9d7d933a41906.jpg"],"type":0,"id":4593713,"ga_prefix":"031513","title":"作为同龄人，董方卓和 C 罗的距离曾经如此之近"},{"images":["http:\/\/pic2.zhimg.com\/a61524b566ecdde57e613f6d6788fb35.jpg"],"type":0,"id":4593668,"ga_prefix":"031512","title":"牛奶包装上常见的「UHT 瞬间高温灭菌技术」是个什么技术？"},{"title":"解决好这个问题，电动车的未来会光明很多（多图）","ga_prefix":"031511","images":["http:\/\/pic1.zhimg.com\/25833b7faf4d7c7e5cc12593f65dfc88.jpg"],"multipic":true,"type":0,"id":4592845},{"images":["http:\/\/pic2.zhimg.com\/c68ecae3feaf513d4c0a62c0c4edc49d.jpg"],"type":0,"id":4593365,"ga_prefix":"031510","title":"怎样评价新垣结衣？"},{"title":"你一定想飞出地球，去别的星球随便看看吧？（多图）","ga_prefix":"031509","images":["http:\/\/pic3.zhimg.com\/7fbec01ce8a62987105cde5887988002.jpg"],"multipic":true,"type":0,"id":4592864},{"images":["http:\/\/pic4.zhimg.com\/a5f31e2ba3871b6187ee52c73bd9a647.jpg"],"type":0,"id":4584681,"ga_prefix":"031508","title":"丰田精彩的发家史，可以看作是日本汽车发展史的一个缩影"},{"images":["http:\/\/pic1.zhimg.com\/935f000243d02d3d3a6db45f7a95ef60.jpg"],"type":0,"id":4579957,"ga_prefix":"031507","title":"为什么越小心翼翼越容易出错？"},{"images":["http:\/\/pic1.zhimg.com\/d658fed72b5f22cc48bada7965fb2bdc.jpg"],"type":0,"id":4593100,"ga_prefix":"031507","title":"房地产业内人士浅见：房价下跌前半年会有什么前奏？"},{"images":["http:\/\/pic1.zhimg.com\/6938f3928f5baf4bab8e0426df293e94.jpg"],"type":0,"id":4591875,"ga_prefix":"031506","title":"瞎扯 · 如何正确地吐槽"}],"top_stories":[{"image":"http:\/\/pic4.zhimg.com\/cc954156eda63b2d7acc08ef4a936037.jpg","type":0,"id":4593600,"ga_prefix":"031515","title":"你好，你长得也太神了吧，你是谁设计的！（多图）"},{"image":"http:\/\/pic2.zhimg.com\/f6889cb09afdd68560c7a79576e82d9d.jpg","type":0,"id":4579957,"ga_prefix":"031507","title":"为什么越小心翼翼越容易出错？"},{"image":"http:\/\/pic2.zhimg.com\/b59b953f9225188e1177ce85a3ae99a5.jpg","type":0,"id":4592864,"ga_prefix":"031509","title":"你一定想飞出地球，去别的星球随便看看吧？（多图）"},{"image":"http:\/\/pic1.zhimg.com\/431cb79754b1ac26d0dcb2edb49508d4.jpg","type":0,"id":4584681,"ga_prefix":"031508","title":"丰田精彩的发家史，可以看作是日本汽车发展史的一个缩影"},{"image":"http:\/\/pic3.zhimg.com\/caf95688750846b68686f5cb55cecc16.jpg","type":0,"id":4592113,"ga_prefix":"031418","title":"一觉醒来发现少了一个肾？医生偷肾没那么容易"}]}
"""
title = '\xe6\x88\xbf\xe5\x9c\xb0\xe4\xba\xa7\xe4\xb8\x9a\xe5\x86\x85\xe4\xba\xba\xe5\xa3\xab\xe6\xb5\x85\xe8\xa7\x81\xef\xbc\x9a\xe6\x88\xbf\xe4\xbb\xb7\xe4\xb8\x8b\xe8\xb7\x8c\xe5\x89\x8d\xe5\x8d\x8a\xe5\xb9\xb4\xe4\xbc\x9a\xe6\x9c\x89\xe4\xbb\x80\xe4\xb9\x88\xe5\x89\x8d\xe5\xa5\x8f\xef\xbc\x9f'
print title.decode('utf-8')

"""
def trim(quote):
	if isinstance(quote, str):
		quote.replace('\\\'', '')
	else:
		return quote
pattern = re.compile(r'[\S]*"date":"([\d]{8})[\S]*"stories":(\[.*\])[\S]*')
pattern_item = re.compile(r'[\S]*"images":\["([\S]*)"\],"type":([\d]+),"id":([\d]*),"ga_prefix":"([\d]*)","title":"([\S]*)"\}')
# pattern_item = re.compile(r'[\S]*"type":(.*)')
match = pattern.match(body)

if match:
	# j = json.dumps(match_item.group(), indent=4)
	arr = match.group(2)
	print arr
	print match.group(1)
	match_item = pattern_item.findall(arr)
	for i in match_item:
		print i[0]
import time
from zhihu.utils import db
# b.connection()
db.init('mysql', 'giraffeDB', 'localhost', '3306')
print db.select('select * from scrapy_zhihu')
u1 = dict(nid=2011, body='dasse4r5t6y7u8i9o', title='bob@test.org', date='20150305', time=time.localtime(time.time()))
db.insert('scrapy_zhihu', **u1)
"""