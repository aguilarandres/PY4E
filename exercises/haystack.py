"""
Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
"""

import re

fname = "regex_sum_1385432.txt"
regex = '[0-9]+'

# list comprehension is the simplest way of creating lists. The simple formula is [expression + contxt]
print( sum( [ int(x) for x in re.findall(regex, open(fname).read()) ] ) )
