
voltages = [4.2, 3.7, 3.4, 3.0, 4.5]

for item in voltages:
  if 4.5>item >= 4.2:
    print("fully charged")
  elif(3.5<=item<4.2):
    print("SAFE - OK TO FLY")
  elif(3.3<=item<3.5):
     print("LOW - LAND SOON")
  elif(item<3.3):
      print("critical-Do NOT FLY")
  else:
      print("OVERCHARGE - DANGER")
  