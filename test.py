user_input = int(input("Put your mark."))

if user_input >= 80 and user_input <= 100:
    print("Grade-A.")
elif user_input >= 60 and user_input <= 79:
    print("Grade-B")
elif user_input >= 40 and user_input <= 59:
    print("Grade-C")
elif user_input < 40:
    print("Sorry you failed the test.")