flight_telemetry = [
    {"waypoint": 1, "status": "Success", "battery": 92},
    {"waypoint": 2, "status": "Error", "battery": 78},
    {"waypoint": 3, "status": "Success", "battery": 64},
    {"waypoint": 4, "status": "Error", "battery": 45}
]

error_count = 0

for item in flight_telemetry:
  if(item["status"]=="Error"):
    print("there is a error in the way point")
    error_count += 1

print(f"the total error is{error_count}")

