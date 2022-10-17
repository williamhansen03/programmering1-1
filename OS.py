print("Vi vill ha en ny OS gren!")
print("Svara Ja eller Nej på följande frågor:")


sport = input("Är det en sport?\n")

if sport == "Ja":
    sport = input("Är det en lagsport?\n")
    if sport == "Nej":
        sport = input("Är det en bollsport?\n")
        if sport == "Ja":
            print("Synd, alla är upptagna!\n")
        elif sport == "Nej": 
            sport = input("Tycker du om vatten?\n")

            if sport == "Nej":
                sport = input("Är du gamer? \n")
                if sport =="Ja":
                        print("E-sport är grenen för dig!")
            elif sport == "Ja":
                sport = input("Tycker du om fisk? \n")
                if sport == "Ja":
                    print("OS-FISKE!") 
                elif sport == "Nej":
                    sport = input("Tycker du om att simma? \n")
                    if sport == "Ja":
                        print("Grubbla över OS-grenar")
                    elif sport == "Nej":
                        print("OS-DRUNKNING")
    elif sport == "Ja":
        sport = input("Utövas det inomhus? \n")
        if sport =="Ja":
            sport = input("Är du introvert? \n")
            if sport =="Ja":
                sport = input("Är du gamer? \n")
                if sport =="Ja":
                    print("E-sport är grenen för dig!")
            elif sport == "Nej": 
                sport = input("Tycker du om vatten?\n")

                if sport == "Nej":
                    sport = input("Är du gamer? \n")

                    if sport =="Ja":
                        print("E-sport är grenen för dig!")
                elif sport == "Ja":
                    sport = input("Tycker du om fisk? \n")
                    if sport == "Ja":
                        print("OS-FISKE!")
                    elif sport == "Nej":
                        sport = input("Tycker du om att simma? \n")
                        if sport == "Ja":
                            print("Grubbla över OS-grenar")
                        elif sport == "Nej":
                            print("OS-DRUNKNING")
        elif sport == "Nej":
            sport = input("Är det en bollsport?\n")
            if sport == "Ja":
                print("Synd, alla är upptagna!\n")
            elif sport == "Nej": 
                sport = input("Tycker du om vatten?\n")

                if sport == "Nej":
                    sport = input("Är du gamer? \n")
                    if sport =="Ja":
                            print("E-sport är grenen för dig!")
                elif sport == "Ja":
                    sport = input("Tycker du om fisk? \n")
                    if sport == "Ja":
                        print("OS-FISKE!") 
                    elif sport == "Nej":
                        sport = input("Tycker du om att simma? \n")
                        if sport == "Ja":
                            print("Grubbla över OS-grenar")
                        elif sport == "Nej":
                            print("OS-DRUNKNING")
else:
    print("Glöm det!")
