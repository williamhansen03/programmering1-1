import random

lastnumber = 0
firstnumber = 0


for i in range(100):
    
    first = ["Captain", "Spider", "Thor", "Iron", "Black", "Doctor", "Bat", "Wonder", "Aqua", "Flash", "Super", "Green", "JARVIS", "Star", "Scare", "Hawkeye", "Falcon"]
    last = ["America", "Man", "Panther", "Widow", "Strange", "Vision", "Man", "Woman", "Joker", "Lantern", "Bane", "Atom", "Thanos", "Lord", "Venom", "Octopus", "Crow"]


    firstnumber = random.randint(0, 15)
    lastnumber = random.randint(0, 15)

    print(first[firstnumber], last[lastnumber])


