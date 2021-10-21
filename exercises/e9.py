"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

filter = 'From:'
file_name = input("Enter file name: ")

if len(file_name) < 1 :
  file_name = "mbox-short.txt"

file_handle = open(file_name)

counts = dict()
names = list()

for line in file_handle :
  if line.startswith(filter) :
    data = line.split()
    names.append(data[1])

for name in names:
  counts[name] = counts.get(name, 0) + 1

prolific = None
maximum = 0

for name, count in counts.items() :
  if count is None or count > maximum :
    prolific = name
    maximum = count

print(prolific, maximum)
