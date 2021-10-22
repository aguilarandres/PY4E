"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
  From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

# this function returns a list of lines in a file that start with the filter parameter
def file_to_list(filename, filter):
  _list = list()
  try:
    handle = open(filename)
  except:
    print("file could not be opened:", filename)
    quit()
  for line in handle:
    line = line.rstrip()
    if line.startswith(filter):
      _list.append(line)

  return _list
# file_to_list function END

filter = "From "
target = ':'

file_name = input("Enter file name: ")

if len(file_name) < 1:
  file_name = "mbox-short.txt"

messages = file_to_list(file_name, filter)
hours = dict()

for message in messages:
  # find the index of the first colon in the time signature e.i. 09:14:16
  index_of_target = message.find(target)
  value = message[index_of_target - 2 : index_of_target]
  hours[value] = hours.get(value, 0) + 1

for k, v in sorted( hours.items() ):
  print(k, v)
