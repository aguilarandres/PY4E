"""
In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

count    = 0;
position = 0;

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

msg_invalid_integer_value = 'Invalid value; enter positive integer value'

url = input('Enter - ')

while True:
  try:
    count = int( input('Enter count: ') )
  except ValueError:
    print(msg_invalid_integer_value)
    continue
  else:
    break

while True:
  try:
    position = int( input('Enter position: ') ) - 1
  except ValueError:
    print(msg_invalid_integer_value)
    continue
  else:
    break

while count >= 0:
  html  = urllib.request.urlopen(url, context=ctx).read()
  soup  = BeautifulSoup(html, 'html.parser')
  tags  = soup('a')
  print('Retreiving: ', url)
  url   = tags[position].get('href', None)
  count -= 1
