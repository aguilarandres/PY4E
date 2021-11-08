"""
Extract Data from XML

The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
"""

import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')

str_comments = urllib.request.urlopen(url, context=ctx).read()

root = ET.fromstring(str_comments)

counts = root.findall('.//count')

print('Retrieving', url)
# print('Retrieved ', , ' characters')
print( 'Count: ', len(counts) )
print( 'Sum: ', sum([int(c.text) for c in counts]) )
