"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
"""

max = 0
min = None
sentinel = "done"

while True:
  number = input("Enter a number: ")

  if number == sentinel:
    break # exit loop
  try:
      # determine if input is a valid integer
    _number = int(number)
    if min is None:
      # assign the first integer to min
      min = _number
    elif _number < min:
      min = _number
  except ValueError:
    print("Invalid input")

  if _number > max:
    max = _number

print("Maximum is", max)
print("Minimum is", min)
