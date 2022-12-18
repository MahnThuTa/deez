traffic_light = str(input("Put your traffic light, Green, Yellow or Red?"))

if traffic_light == "Green" or "green":
    print("Vehicles can go.")
    print("People must stop.")
elif traffic_light == "Yellow" or "yellow":
    print("Vehicles must slow down")
    print("People must stop.")
elif traffic_light == "Red" or "red":
    print("Vehicles must stop.")
    print("People can go.")