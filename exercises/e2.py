# Program that prompts the user for hours and rate per hour to compute gorss
# pay

standard_hours = 40.0
overtime_rate = 1.5

# store user input for hours as string
hours = input("Enter Hours: ")
# convert input string for hours to float
_hours = float(hours)
# store user input for rate as string
rate = input("Enter Rate: " )
# convert intput string for rate to float
_rate = float(rate)
# calculate gross pay
gross_pay = _rate * _hours

# Calculate overtime rate
if(_hours > standard_hours):
  # calculate over time hours
  overtime_hours = _hours - standard_hours
  # calculate over time pay
  overtime_pay   = overtime_hours * (overtime_rate * _rate)
  gross_pay      = overtime_pay + (standard_hours * _rate)

# display gross pay on screen
print(gross_pay)
