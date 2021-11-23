"""
Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
"""

# prompt user for file name
fname = input("Enter file name: ")

try:
  fhandle = open(fname, 'r')
  # print("file opened for reading:", fname, "\n")
except:
  print("file could not be opened:", fname, "\n")
  quit()

# list of words in the text file
words = list()
for line in fhandle:
  words += line.split()

# second list comprised of all unique words
_words = list()
for word in words:
  if word not in _words:
    _words.append(word)

_words.sort()

print(_words)
