# Program that prompts the user for hours and rate per hour to compute gorss
# pay. Calculate gross pay with a function called computepay()

standard_hours = 40.0
overtime_rate = 1.5

def computepay(hours, rate):

  hours = float(hours)
  rate  = float(rate)

  gross_pay = hours * rate
  # Calculate overtime rate
  if(hours > standard_hours):
    # calculate over time hours
    overtime_hours = hours - standard_hours
    # calculate over time pay
    overtime_pay   = overtime_hours * (overtime_rate * rate)
    gross_pay      = overtime_pay + (standard_hours * rate)

  return gross_pay

# store user input for hours as string
hours = input("Enter Hours: ")
# store user input for rate as string
rate = input("Enter Rate: " )

