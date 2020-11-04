#P.25
from  urllib import request
url = 'http://ea4b5b22.ngrok.io/hello_get?name=Allen'

res = request.urlopen(url)

#將html轉換成字串
bstr =res.read()
html =bstr.decode('utf-8')
print(html)