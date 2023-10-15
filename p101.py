import random
response = input("Press y to roll and n to exit")
response="y"
while response == "y":
    no = random.randint(1, 6)

    if no == 1:
        print(" ------- ")
        print("|       |")
        print("|   •   |")
        print("|       |")
        print(" ------- ")
    elif no == 2:
        print(" ------- ")
        print("| •     |")
        print("|       |")
        print("|     • |")
        print(" ------- ")
    elif no == 3:
        print(" ------- ")
        print("| •     |")
        print("|   •   |")
        print("|     • |")
        print(" ------- ")
    elif no == 4:
        print(" ------- ")
        print("| •   • |")
        print("|       |")
        print("| •   • |")
        print(" ------- ")
    elif no == 5:
        print(" ------- ")
        print("| •   • |")
        print("|   •   |")
        print("| •   • |")
        print(" ------- ")
    elif no == 6:
        print(" ------- ")
        print("| • • • |")
        print("|       |")
        print("| • • • |")
        print(" ------- ")

    response = input("Roll again? (y/n): ")