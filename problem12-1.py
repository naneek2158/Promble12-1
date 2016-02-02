# Problem 12-1 The Speed Limit

print("Problem 12-1")

speed_limit = input("Enter the speed limit: ")
recorded_speed = input("Enter the recorded speed of the car: ")

speed_difference = recorded_speed - speed_limit

if speed_difference > 31:
    print("You are speeding and your fine is $500")
elif speed_difference > 21:
    print("You are speeding and your fine is $270")
elif speed_difference > 1:
    print("You are speeding and your fine is $100")
else:
    print("Congratulations. You are within the speed limit!")
