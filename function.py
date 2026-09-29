altitudes = [10, 25, 40, 35, 50, 20, 5, 0]

def max_altitudes(numbers):
   max = numbers[0]
   for items in numbers:
      if max<items:
         max = items
   return max

def min_altitudes(numbers):
   min = numbers[0]
   for items in numbers:
       if items<min:
          min = items

   return min 
  
def sum_altitudes(numbers):
   sum_altitude = 0
   for item in numbers:
      sum_altitude += item 
   return sum_altitude


def status_altitude(altitude):
   for item in altitude:
      if item>30:
         print(f"HIGH: {item}")
      elif item<10:
         print(f"LOW: {item}")
      else:
         print(f"NORMAL: {item}")

  
status_altitude(altitudes)

print(f"The maximum altitude:{max_altitudes(altitudes)}\nThe minimum altitude:{min_altitudes(altitudes)}\nthe sum of altitude:{sum_altitudes(altitudes)}")
