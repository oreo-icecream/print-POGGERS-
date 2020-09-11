poggers = "POGGERS!"
# End of Variables
# CLI
print("What do you want to do?")
print("")
print("")
print("1. POGGERS")
print("2. Copypastas")
print("")
cli_choice = input("Please select a option: ")
if cli_choice == 1:
    choice = input("How many time do you want to POG????: ")
    choice_number = int(choice)
    #Variables ^
    if choice_number > 0:
        for i in range(int(choice)):
            print(poggers)
    elif choice_number == 0:
        print("You're a dumbass. I'm tired of dumbasss like who think I can print 0 POGGERS. Fuck off")

    input('Press "Enter" to stop: ')
elif cli_choice == 2:
    print("Sorry! This isn't ready yet. :>")
else:
    print("What are you doimg?? You druggo!")

