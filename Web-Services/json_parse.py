"""
Extracting Data from JSON

The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum
"""

import ssl
import json
import urllib.parse
import urllib.request

url = input('Enter location: ')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

parsed_url = urllib.request.urlopen(url, context=ctx).read()

json_data = json.loads(parsed_url)
list_comments = json_data['comments']

print('Retrieving', url)
print('Retrieved ', len(parsed_url.decode()), ' characters')
print( 'Count: ', len(list_comments) )
print( 'Sum: ', sum( [comment['count'] for comment in list_comments] ) )
