
try:
  print("Enter a number between 1 and 10:")
  number = int(input())
except ValueError:
  print("You must enter a number between 1 and 10:")
  number = int(input())
