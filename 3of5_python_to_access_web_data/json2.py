import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1:
  url = 'http://py4e-data.dr-chuck.net/comments_42.json'
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
js = json.loads(data)
sum = 0
counts = len(js['comments'])
print('Count:', counts)
for i in range(counts):
  sum += js['comments'][i]['count']
print('Sum:', sum)

