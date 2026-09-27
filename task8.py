waypoints = [(0, 0), (10, 5), (20, 15), (30, 10), (40, 0)]

max_x = waypoints[0][0]
max_y = waypoints[0][1]

waypoint_count = 0

for item in waypoints:
    waypoint_count += 1
    if item[0] > max_x:
        max_x = item[0]
    if item[1] > max_y:
            max_y = item[1]
    if item[0] >25:
        status = "DISTANCE"
    else:
         status = "NEAR"

            

    print(f"Waypoint{waypoint_count} :({item[0]}, {item[1]})-->{status}\n")

print(f"MAX X{max_x}\nMAX Y{max_y}")
