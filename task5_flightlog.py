altitudes = [10, 25, 40, 35, 50, 20, 5, 0]

max = -1
min =1000

# max = max(altitudes)
# min =min(altitudes)
sum_altitude = 0

for item in altitudes:
  if item>30:
    print(f"HIGH: {item}")
  elif item<10:
    print(f"LOW: {item}")
  else:
    print(f"NORMAL: {item}")

  if max<item:
    max = item
  if(item<min):
    min = item
  sum_altitude += item 

  


print(f"The maximum altitude:{max}\nThe minimum altitude:{min}\nthe sum of altitude:{sum_altitude}")
