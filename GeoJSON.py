import urllib.request, urllib.parse, urllib.error
import json
import ssl


api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js=json.loads(data)

print(js["results"][0]["geometry"]["location"])
