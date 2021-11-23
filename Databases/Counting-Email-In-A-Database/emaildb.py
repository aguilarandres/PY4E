"""

Counting Organizations

This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)

"""

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
fh = open(fname)
for line in fh:
  # Only include "From: username@domain" part of message
  if not line.startswith('From: '): continue
  from_line = line.split() # From: username@domain
  email = from_line[1] # username@domain
  index = email.find('@') # index of @ sign
  org = email[index + 1 : len(email)] # domain substring of email address

  cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
  row = cur.fetchone()
  if row is None:
    cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
  else:
    cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
  print(str(row[0]), row[1])

cur.close()
