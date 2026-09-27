currents = [13, 0, 0, 12,14]
warning = 0

max_current =currents[0]
motor_number = 0
for item in currents:
  motor_number = motor_number + 1
  if item > max_current:
           max_current = item

  if item > 15:
      print(f"M{motor_number}- critical temperature\n")
      warning += 1
     
      
  elif item > 10:
      warning += 1
      print(f"M{motor_number}-Motor is over heating\n")
  else:
       print(f"M{motor_number}- Motor is normal\n")

print(f"Max Current {max_current}A\n")

print(f"Warnings:{warning}\n")