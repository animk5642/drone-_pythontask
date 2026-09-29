altitudes = [10, 25, 40, 35, 50, 20, 5]

max = altitudes[0]
min =altitudes[0]

def find_max(numbers,max):
    for items in numbers:
     if max<items:
       max = items  
  
    return max

def find_min(numbers,min):
   for items in numbers:
    # print(items)
    if(items<min):
      min = items
   return min

def sum_items(sum,item):
     sum = sum + item

     return sum
  


sum_altitude = 0

for item in altitudes:
  if item>30:
    print(f"HIGH: {item}")
  elif item<10:
    print(f"LOW: {item}")
  else:
    print(f"NORMAL: {item}")
  sum_altitude = (sum_items(sum_altitude,item))

  

print(f"The maximum altitude:{find_max(altitudes,max)}\nThe minimum altitude:{find_min(altitudes,min)}\nthe sum of altitude:{sum_altitude}")
