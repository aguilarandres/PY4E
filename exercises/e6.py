"""
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form: X-DSPAM-Confidence:    0.8475 Use the file name mbox-short.txt as the file name
"""

target = "X-DSPAM-Confidence:"
total = 0
value = 0

file = input("Enter file name: ")
try:
  handle = open(file)
except:
  print("file could not be opened:", file)
  quit()
for line in handle:
    if not line.startswith(target):
        continue
    total += 1
    value += float ( line[line.find('0') : ] )

print("Average spam confidence:", value / total)
