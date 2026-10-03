flight_times = [12, 25, 18, 30, 22]
total_time=0
try:
  with open("flight_log.txt","w") as fp:
    for item in flight_times:
      item = str(item)
      fp.write(item)
      fp.write("\n")

  with open("flight_log.txt","r") as fp:
      for item in fp:
        s = item.strip()
        #  print(s)
        b = int(s)
        print(b)
        total_time= total_time + b
  print(F"the total time is {total_time}")
except FileNotFoundError:
  print("the file not found")


# print(f"the sum of the time is {total_time}")


  



