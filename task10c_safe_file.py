def read_flight_log(filename):
  try:
    with open(filename,"r") as fp:
     s = fp.read()
    return s 
  except FileNotFoundError:
    return "the file not found"

print(read_flight_log(input("enter the file name")))