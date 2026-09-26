fleet = {
    "Drone-A": "active",
    "Drone-B": "maintenance",
    "Drone-C": "active",
    "Drone-D": "grounded"
}

Count_active = 0
Count_inactive = 0
for key,value in fleet.items():
   print(f"{key}:{value}")
   if value=="active":
    Count_active += 1
   else:
    Count_inactive +=1 

print(f"the count of active is {Count_active} \nthe count of innacticve is {Count_inactive}")

