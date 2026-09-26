cell_volatage = [3.8, 3.7, 3.4, 3.9]

for i in cell_volatage:
   print(f"the cell voltage is {i}")
   if(i<3.5):
      print("error")
      break
   