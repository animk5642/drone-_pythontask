
weight_total = input("enter the total weight of the drone in grams")

motor_thrust = input("enter the thrust produced by on motor in grams")
'''this is multi line command'''
total_motor_thrust = int(motor_thrust) * 4

# print("the weight ratio is ",round(total_motor_thrust/int(weight_total),2))

ratio = total_motor_thrust/int(weight_total)


print(f"the ratio is {ratio:.2f}")
