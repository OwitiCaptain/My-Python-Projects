

print("********************************")
print("\nDial *254# below to access main menu")
dial = input("Enter *254# to continue\n: ")
if dial == "*254#":
    print(
        "\n Welcome to Nyota Project 254 where \n Governemnt empowers young people through \n non-refundable loan.\n Select:")
    print("\n 1. Register"
          "\n 2. Sign-in"
          "\n 3. Apply for loan"
          "\n 4. Repay your loan")
    print("********************************")
    answer1 = input("Selection: ")

    if answer1 == "1":
        year = int(input("Confirm your year of birth: "))
        if year < 2007:
            name = input("Enter your full name: ")
            year_of_birth = int(input("Year of birth: "))
            if year_of_birth > 2007:
                print("You are NOT eligible for the loan")
            amount_request = (input("Amount requesting: "))
            print(f"\n Hello {name}, your loan amount of Kshs {amount_request}\n is being processed")
        else:
            print("Loan NOT available for under 18 years old")
    elif answer1 == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        print(f"{username} logged in successfully!")
    elif answer1 == "3":
        amount_to_apply = int(input("Enter amount to apply: "))
        amount_to_apply = amount_to_apply / 1.16
        print(f"You qualify for Kshs {amount_to_apply} loan.")
    elif answer1 == "4":
        list_of_borrowers = ["Kennedy", "Brian", "Chris", "Pamela"]

        name = input("Enter your name: ")
        if name.lower() not in list_of_borrowers:
            print("You don't have a loan with us!")
            print("Bye!")
        else:
            amount_borrowed = int(input("Amount borrowed: "))
            to_pay = amount_borrowed *20/100
            new_pay = to_pay + amount_borrowed
            print(f"Pay {new_pay} before end of this year.")
    else:
        print("Invalid option")
else:
    print("That's an INVALID option")





