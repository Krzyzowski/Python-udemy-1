


print("give two numbers and I'll divide them")
print("Enter 'q' to quit")

while True:
    first_number = input("first number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
        print(answer)
    except ZeroDivisionError:
        print("You can't divide by zero")
print( )