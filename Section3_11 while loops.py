
count = 1

while count <= 100:
    print(count)

    user_input = input("enter 'exit' to end ")

    if user_input.lower() == "exit":
        print("Exiting the program. See You")
        break

    count = count + 10