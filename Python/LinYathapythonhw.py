traffic_light = str(input("What do you want know about traffic light?"))

if traffic_light == "red":
    print("Stop all vehicles but people can go")
elif traffic_light == "green":
    print("All vehicles can go but people can't go")
elif traffic_light == "yellow":
    print("All vehicles must slow down and people must stop too")
