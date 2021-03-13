import requests

r = requests.get('https://xkcd.com/353/')

print(r.text)

r = requests.get('https://imgs.xkcd.com/comics/python.png')

print(r.content)

with open('comic.png', 'wb') as f:
    f.write(r.content)
print(r.status_code, r.ok)

print(r.headers)

payload = {'page': 2, 'count': 25 }
r = requests.get('https://httpbin.org/get', params=payload)

print(r.text, r.url)

payload = {'username': 'ambar', 'password': 'testing' }
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text, r.url, r.json())

r_dict = r.json()

print(r_dict['form'])


r = requests.get('https://httpbin.org/basic-auth/john/testing', auth=('john', 'testing'))
print(r.text)

r = requests.get('https://httpbin.org/basic-auth/john/testing', auth=('johntest', 'testing'))
print(r)

r = requests.get('https://httpbin.org/delay/1', timeout=3)
print(r)

r = requests.get('https://httpbin.org/delay/6', timeout=3)
print(r)
