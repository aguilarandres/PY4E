# prompt user for score and store string in variable
score = input("Enter Score: ")
# convert string to float
_score = float(score)

# check if score is between 0.0 and 1.0
if _score < 0.0 or _score > 1.0:
  print("Error, socre is out of range")
  exit()
elif _score >= 0.9:
  print("A")
elif _score >= 0.8:
  print("B")
elif _score >= 0.7:
  print("C")
elif _score >= 0.6:
  print("D")
elif _score < 0.6:
  print("F")
