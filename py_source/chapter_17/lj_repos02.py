import requests
# Make an API call, and store the response.
url = 'https://www.visaonline.com/'
auth=('lapbong_china', 'BOCmacau@70')
r = requests.get(url, auth=auth)
print("Status code:", r.status_code)
print("Header:",r.headers['content-type'])
print("Encoding: ", r.encoding)
print("Url you are connecting: ", r.url)
"""print("Text : ", r.text)"""

data=[
    ('ctl00$PlaceHolderMain$txtUsername','lapbong_china'),
    ('ctl00$PlaceHolderMain$txtPd','BOCmacau@70')
    ]
r1=requests.post(url, data)
print("Status code: ", r.status_code)
#print(r1.text)
r2=requests.get('https://vrm-ext.visaonline.com/secure/admin/v1/user/start',data)
print(r2.status_code)
r3=requests.get('https://vrm-ext.visaonline.com/secure/app/reports',data)
print(r3.status_code)
print(r3.text)