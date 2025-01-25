print("Welcome to ATM")

balance = 1000

user_pin = '1234'

entered_pin = input("Please enter Your PIN: ")

if entered_pin != user_pin:
    print("Invalid PIN. Ciao Bambino")
    atm_on = False

else:
    atm_on = True

while atm_on:
    print("Main Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter Your choice")

    if choice == "1":
        print("Your current balance is $" + str(balance))

    elif choice == "2":
        amount = float(input("Enter the amoount to deposit: $"))
        balance += amount
        print("$" + str(amount) + " deposited succesfully." )

    elif choice == "3":
        amount = float(input("Enter the amount to withdraw: $"))
        if amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print("$" + str(amount) +" withdrawn succesfully.")

    elif choice == "4":
        print("Thank You for using the ATM. CIAO!")
        atm_on = False

    else:
        print("Invalid choice. Please try again.")