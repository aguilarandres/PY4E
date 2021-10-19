
filter = 'From:'
file_name = input("Enter file name: ")

if len(file_name) < 1:
  file_name = "mbox-short.txt"

file_handle = open(file_name)
count = 0

for line in file_handle:
  line = line.rstrip()
  if line.startswith(filter):
    data = line.split()
    count += 1
    print(data[1])

print("There were", count, "lines in the file with From as the first word")
