print("Vi vill ha en ny OS gren!")
print("Svara ja eller nej på följande frågor:")

sport = input("Utövas det inomhus? \n")


if sport =="Ja":
    sport = input("Är du introvert? \n")
    if sport =="Ja":
       sport = input("Är du gamer? \n")
       if sport =="Ja":
            print("E-sport är grenen för dig!")
    else: 
        sport = input("Tycker du om vatten?\n")
        if sport =="Ja":
            print("Hej")

else:
    print("Glöm det!")
