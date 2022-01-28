import random

hero = 0
villain = 0


superhero_list = ["Captain America", "Thor", "Spiderman", "Hulk", "Iron Man", "Batman", "Superman", "Wonder Woman", "Ant Man"]
villain_list = ["Loki", "Thanos", "Ultron", "Venom", "Joker", "Bane", "Green Goblin", "Riddler", "Darkseid", "Dr Octopus"] 

while True:
    hero = random.randint(0,8)
    villain = random.randint(0, 9)

    print(superhero_list[hero],"vs", villain_list[villain],"\n")

    vilken_du_vill_ha = input("vilken tror du kommer att vinna?")

    if(vilken_du_vill_ha == superhero_list[hero]):
        print("Du hade rätt!", "\n")
    elif(vilken_du_vill_ha == villain_list[villain]):
        print("Tyvärr du förlorade","\n")
    else:
        print("Varför är du dum i huvudet?!", "\n")
    


