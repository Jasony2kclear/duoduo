import qrcode
url1 = qrcode.make('http://mp.weixin.qq.com/s?__biz=MzA3NTI2NTg1Nw==&mid=2455517930&idx=1&sn=a0736d86fd5a9e02f112b8cfba3b53ea&chksm=88dbb8c4bfac31d28cad17ecb8d9863b1cc09fb39ad93c5f4917f1502e7bb011a58c89bc9204#rd')
with open('test.png','wb') as f:
    img1 = url1.save(f)