import urllib.request
import urllib
import re

url = "http://www.tuling123.com/openapi/api"
q_data = {
    'key': "716290f57aa64f5782958d6c9451f4ed",
    'info': "上海科技大学好不好啊",
    'userid': "12345678"
}

q_data = urllib.parse.urlencode(q_data)
print(q_data)
q_data = q_data.encode('utf-8')

f = urllib.request.urlopen(url,q_data)
a_data = f.read()
print(a_data)
a_data = a_data.decode('UTF-8')
print(a_data)
