checks = {
    "battery": 5,
    "gps_satellites": 5,
    "compass":0,
    "motors": True,
    "wind_speed": 70
}

status = "fail"

failed =[]
Bonus = 0


print(failed)


for key,value in checks.items():
    if key == "battery" :
      if value > 60:
           Bonus +=  1
      else:
        
        failed.append(key)

        
       
    if key ==  "gps_satellites":
       if value > 6:
         Bonus +=  1
       else:
        failed.append(key)
    if key == "compass" :
      if value == True:
         Bonus +=  1
      else:
        failed.append(key)
    if key == "motors":     
     if value == True:
      Bonus +=  1
     else:
       failed.append(key)

    if key == "wind_speed": 
       if value<20:
        Bonus +=  1
       else:
        failed.append(key)
if(Bonus == 5):
    # print(Bonus)
  print("ALL CHECKS PASSED - READY FOR TAKEOFF")
    # 
else:
    # print(Bonus) 
    print("CHECK FAILED - DO NOT FLY")
    # print(f"Failed checks: {failed}")
    print(f"Failed checks: {failed}")git 