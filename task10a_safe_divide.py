def safe_divide(a, b):
  try:
    c = a/b

    return f"the result is {c}"
  except ZeroDivisionError:
    return "cannot devided by 0"



a = int(input("enter the number a here"))
b = int(input("enter the number b here"))

print(safe_divide(a,b))
