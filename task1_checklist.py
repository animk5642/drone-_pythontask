checklist = ["battery","gps","compass","motors","propellers"]

for items in checklist:
  print(f"{items} CHECKED")

checklist.append("camera")

for items in checklist:
  print(f"{items} CHECKED")

print(f"the total number of the item :{len(checklist)}")