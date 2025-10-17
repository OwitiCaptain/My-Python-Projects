import random
import sys
import time


bet1 = random.choice(["Kenya", "Tanzania", "Uganda","Somalia","Rwanda"]).upper()
bet2 = random.choice(["England", "Barcelona", "Spain","Russia","Sweden"]).upper()
bet3 = random.choice(["USA", "Canada", "Australia","Djibouti","South Africa"]).upper()
bet4 = random.choice(["Egypt", "Libya", "Nigeria","Ghana","Ivory Coast"]).upper()
bet5 = random.choice(["Mozambique", "Zambia", "Zimbabwe","Congo","Austria"]).upper()
bet6 = random.choice(["Botswana", "Eritrea", "Guinnea","Malawi","Seycheles"]).upper()


print("\n********** WARNING! **********")
print("\nBetting is not allowed for kids under the age of\n18 years. Please bet responsibly!")
def chose_bet():
    answer = input("\nDo you want to place bet?: ")
    if answer.lower() == "yes" or answer.lower() == "y":
        print("\nSelect a game below to bet:")
        print(f"1. {bet1} vs {bet2}")
        print(f"2. {bet3} vs {bet4}")
        print(f"3. {bet5} vs {bet6}")
        print(f"4. {bet4} vs {bet2}")
    elif answer.lower() == "no" or answer.lower() == "n":
        sys.exit("Goodbye 👋👋")
    else:
        print("Invalid selection!")
        chose_bet()

chose_bet()
while True:
    my_selection = input("\nChoose a team between 1-4: ")

    if my_selection == "1":
        my_bet = input("Which team do you predict to win in the selection?: ")
        print(f"\n{bet1} vs {bet2} is playing. Wait for 5 seconds ........")
        time.sleep(5)
        print("Please wait.......")
        time.sleep(3)
        print("Please wait.......")
        time.sleep(2)
        winner = random.choice([bet1, bet2])
        if my_bet.upper() == winner.upper():
            print(f"Congratulations, {my_bet} WON 🎉🎊🎉🎊")
            break
        else:
            print("SORRY, you Lost!")
            print(f"{winner} Won")
            continue
    elif my_selection == "2":
        my_bet = input("Which team do you predict to win?: ")
        print(f"\n{bet3} vs {bet4} is playing. Wait Wait for 5 seconds ........")
        time.sleep(5)
        print("Please wait.......")
        time.sleep(3)
        print("Please wait.......")
        time.sleep(2)
        winner = random.choice([bet3,bet4])
        if my_bet.upper() == winner.upper():
            print(f"Congratulations, {my_bet} WON 🎉🎊🎉🎊")
            break
        else:
            print("SORRY, you Lost!")
            print(f"{winner} Won")
            continue
    elif my_selection == "3":
        my_bet = input("Which team do you predict to win?: ")
        print(f"\n{bet5} vs {bet6} is playing. Wait Wait for 5 seconds ........")
        time.sleep(5)
        print("Please wait.......")
        time.sleep(3)
        print("Please wait.......")
        time.sleep(2)
        winner = random.choice([bet5,bet6])
        if my_bet.upper() == winner.upper():
            print(f"Congratulations, {my_bet} WON 🎉🎊🎉🎊")
            break
        else:
            print("SORRY, you Lost!")
            print(f"{winner} Won")
            continue
    elif my_selection == "4":
        my_bet = input("Which team do you predict to win?: ")
        print(f"\n{bet4} vs {bet2} is playing. Wait Wait for 5 seconds ........")
        time.sleep(5)
        print("Please wait.......")
        time.sleep(3)
        print("Please wait.......")
        time.sleep(2)
        winner = random.choice([bet4,bet2])
        if my_bet.upper() == winner.upper():
            print(f"Congratulations, {my_bet} WON 🎉🎊🎉🎊")
            break
        else:
            print("SORRY, you Lost!")
            print(f"{winner} Won")
            continue
    else:
        print("Invalid team!")
        continue




