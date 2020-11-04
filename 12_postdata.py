import requests

url = 'http://ea4b5b22.ngrok.io/hello_post'

res_get = requests.get(url)
print(res_get.text)

print('----------------------------')
data = {'username':'Allen'}
res_post = requests.post(url,data=data)
print(res_post.text)