#########################################

# this script has to be rewrite into a python function !

# our training set   https://www.customvision.ai


########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
import uuid
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Prediction-key': 'bd951cae1d794f1f97ee74e2246b0b24',#api-key,   don't modify
}

params = urllib.parse.urlencode({
    # Request parameters
    # 'projectId':
    'iterationId': 'c884d78e-b174-455a-b277-ad47ff175f51',#iterationId, a uuid number, may be changed later
})

#it is a function para in fact
body='{"url":"http://i4.piimg.com/600084/69b7292bebca1cc1.jpg"}'# our image url!!!!!!!!
try:
    conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/customvision/v1.0/Prediction/e6fcc6c2-e443-49be-9e87-ccf2441a1204/url?%s" % params,body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)# not print but as a return
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
