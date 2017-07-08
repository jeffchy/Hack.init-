#coding = utf-8
import urllib.request
import urllib
import re
import json
url = "http://www.tuling123.com/openapi/api"

MEANING = {"好吃":"好吃","HI":"你好","HELLO":"你好","你好":"你好","WHO ARE YOU":"你是谁","WHO":"你是谁","WHO R U":"你是谁","你是谁":"你是谁","你是？":"你是谁"}


CHATLOG = {"旺旺QQ可乐软糖":{"你好":"我是旺仔QQ糖，可乐味！哦！我的宝贝！","你是谁":"人见人爱的吃的，记住了吧～","好吃":"废话当然好吃辣"}
			,"上好佳嗲得薯片":{"你好":"你好-上呀么上好佳呀、味呀嘛味道佳、 oishi","你是谁":"我是薯片！-上呀么上好佳呀、味呀嘛味道佳、 oishi","好吃":"废话当然好吃辣"}
			,"上好佳汉堡球":{"你好":"你好-上呀么上好佳呀、味呀嘛味道佳、 oishi","你是谁":"我是汉堡球呀，上呀么上好佳呀、味呀嘛味道佳、 oishi","好吃":"废话当然好吃辣"}
			,"上好佳牛奶小饼":{"你好":"你好-上呀么上好佳呀、味呀嘛味道佳、 oishi","你是谁":"我是饼干牛奶味！-上呀么上好佳呀、味呀嘛味道佳、 oishi","好吃":"废话当然好吃辣"}
			,"上好佳玉米卷":{"你好":"你好-上呀么上好佳呀、味呀嘛味道佳、 oishi","你是谁":"我是玉米卷！-上呀么上好佳呀、味呀嘛味道佳、 oishi","好吃":"废话当然好吃辣"}
			,"上好佳水果硬糖":{"你好":"上呀么上好佳呀、味呀嘛味道佳、","你是谁":"我是水果糖-oishi","好吃":"废话当然好吃辣"}
			,"上好佳鲜虾条":{"你好":"你好-上呀么上好佳呀、味呀嘛味道佳、 oishi","你是谁":"我是虾条，来一条么？","好吃":"废话当然好吃辣"}
			,"上好佳鲜虾片":{"你好":"要不要试试我哥鲜虾条？","你是谁":"我是虾片，吃吃吃","好吃":"废话当然好吃辣"}
			,"咪咪虾条":{"你好":"侬好，阿拉咪咪虾条，不知道比上好佳高到哪里去了","你是谁":"阿拉咪咪虾条，来吃？","好吃":"废话当然好吃辣"}
			,"奇多干杯脆":{"你好":"干杯！","你是谁":"我是奇多干杯脆！","好吃":"废话当然好吃辣"}
			,"旺仔QQ糖":{"你好":"你好呀！旺仔QQ糖！果味无穷，哦！我的宝贝！","你是谁":"我是旺仔QQ糖，哦！我的宝贝！","好吃":"废话当然好吃辣"}
			,"旺旺雪饼":{"你好":"你好呀！来片雪饼?","你是谁":"我是旺旺雪饼，好吃够味！","好吃":"废话当然好吃辣"}
			,"星球杯":{"你好":"你好呀！星球杯超好吃的！","你是谁":"我是星球杯，来吃嗨吧!","好吃":"废话当然好吃辣"}
			,"喜之郎果冻":{"你好":"你好呀！我是喜之郎，长大后我想当太空人！","你是谁":"我是喜之郎，爸爸妈妈可开心了，给我爱吃的喜之郎！","好吃":"废话当然好吃辣，果味无限！"}
			,"香蕉":{"你好":"粑粑，娜娜，粑粑娜娜！","你是谁":"粑娜娜，补充矿物元素必备哦！","好吃":"废话当然好吃辣，补充维生素诶！"}
			,"雪碧":{"你好":"雪碧！透心凉，心飞扬！","你是谁":"雪碧！透心凉，心飞扬！","好吃":"我明明是好喝？但不要贪杯哦"}
			,"亲嘴烧":{"你好":"卫龙亲嘴烧，民族品牌绝不卖给韩国人","你是谁":"我是卫龙亲嘴烧，含有高碳水化合物，少吃点！","好吃":"废话当然好吃辣"}
			,"hackinit":{"你好":"Hello, Hackers!","你是谁":"我是hackinit，全国最大的hackathon之一!","好吃":"我怎么能吃呢？"}
			}

def changeMeaning(greeting):
	greetingArrs = list(MEANING.keys())
	for i in range(len(MEANING)):
		if (list(MEANING.keys())[i] in greeting):
			return	MEANING[list(MEANING.keys())[i]]
	return greeting



def getResponse(obj,greeting):
	greeting = changeMeaning(greeting.upper())
	greetingArr = list(CHATLOG[obj].keys())
	for i in range(len(CHATLOG["旺旺QQ可乐软糖"])):
		if greetingArr[i] in greeting:
			return CHATLOG[obj][greetingArr[i]]
		else:
			continue
	q_data = {
		'key': "716290f57aa64f5782958d6c9451f4ed",
		'info': greeting,
		'userid': "12345678"
	}
	q_data = urllib.parse.urlencode(q_data)
	q_data = q_data.encode('utf-8')
	f = urllib.request.urlopen(url,q_data)
	a_data = f.read()
	a_data = a_data.decode('UTF-8')
	dictJson = json.loads(a_data)
	return dictJson["text"]


# print (getResponse("雪碧","你好吃吗？"))
