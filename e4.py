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
