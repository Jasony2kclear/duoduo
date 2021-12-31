import requests
from http import cookiejar
data=[
    ('ctl00$PlaceHolderMain$txtUsername','lapbong_china'),
    ('ctl00$PlaceHolderMain$txtPd','BOCmacau@70')
    ]
url = 'https://www.visaonline.com/'
r1=requests.post(url, data)
print(r1.status_code)

cookieJar=cookiejar.CookieJar()
opener=requests.build_opener(requests.HTTPCookieProcessor(cookieJar))