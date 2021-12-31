import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
data={
    'ctl00$PlaceHolderMain$txtUsername':'lapbong_china',
    'ctl00$PlaceHolderMain$txtPd':'BOCmacau@70',
    'submit':'btnLogin'
    }
s=requests.session()
url = 'https://www.visaonline.com/'
r1=s.get(url)
print(r1.status_code)
#print(r1.text)
r11=urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj=BeautifulSoup(r11.read(),features="html.parser")
print(bsObj.text)

#bsObj=BeautifulSoup(requests.get('http://www.pythonscraping.com/pages/page1.html'))

r2=s.post(url,data)
print(r2.status_code)
r3=s.get('https://secure.visaonline.com/SitePages/GVOLHome.aspx')
#print(r3.text)
print(r3.status_code)