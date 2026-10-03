def safe_int(value):
  try:
    a = int(value)
    return a

  except ValueError:
     return "cannot converted to interger"


print(safe_int(input("enter the value")))