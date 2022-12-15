# My shopping list for the party
meat = 10000
cake = 20000
cup_cakes = 10000
orange_juice = 5000
lemon_juice = 5000

if cake > meat:
    print("It's really expensive.")
if cup_cakes < meat:
    print("It's not that bad")
elif cup_cakes == meat:
    print("Let's buy both.")
elif lemon_juice != orange_juice:
    print("They are both juice?")
if orange_juice >= cake:
    print("Oh!")
else:
    print("Ofc cake is more expensive.")
if lemon_juice <= cup_cakes:
    print("Cup cakes win.")
