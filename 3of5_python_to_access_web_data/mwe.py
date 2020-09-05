# minimal working example
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore potential SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# XML data from string
stringdata = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

stringtree = ET.fromstring(stringdata)
print('Name:', stringtree.find('name').text)
# this print statement works and outputs "Chuck" from line 14

# XML data from url
url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
urlhandle = urllib.request.urlopen(url, context=ctx)
urldata = urlhandle.read()
urltree = ET.fromstring(urldata)
print('Name:', urltree.find('name').text)
# Why does this print statement fail even though urldata
# *does* have more than one XML element with the tag 'name'


