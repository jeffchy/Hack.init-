#########################################

# this script has to be rewrite into a python function !

# our training set   https://www.customvision.ai


########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64,json
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Prediction-key': 'bd951cae1d794f1f97ee74e2246b0b24',#api-key,   don't modify
}
params = urllib.parse.urlencode({
    # Request parameters
    # 'projectId':
    'iterationId': '8098081f-674a-4dbe-82e8-caed5c5df534',#iterationId, a uuid number, may be changed later
})
#it is a function para in fact
def detect(url_dir):
    body={'url':url_dir}
    try:
        conn = http.client.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/customvision/v1.0/Prediction/e6fcc6c2-e443-49be-9e87-ccf2441a1204/url?%s" % params,str(body), headers)
        response = conn.getresponse()
        data = response.read()
        data=str(data, encoding = "utf-8")
        data=json.loads(data)
        print(data)# not print but as a return
        array=data['Predictions']
        conn.close()
        pe=array[0]['Probability']
        if pe<0.5:
            return ""
        else:
            return array[0]['Tag']
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
