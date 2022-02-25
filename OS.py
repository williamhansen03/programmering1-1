print("Vi vill ha en ny OS gren!")
print("Svara Ja eller Nej på följande frågor:")

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
            sport = input("Tycker du om fisk? \n")

            if sport == "Ja":
                print("OS-FISKE!")

                if sport == "Ja":
                    print("Grubbla över OS-grenar")
                elif sport == "Nej":
                    print("OS-DRUNKNING")

            elif sport == "Nej":
                sport = input("Tycker du om att simma? \n")
else:
    print("Glöm det!")
