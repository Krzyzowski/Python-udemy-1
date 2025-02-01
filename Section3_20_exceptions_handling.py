#print(5/0) ZeroDivisionError: division by zero

try:
    print(5/2)
except ZeroDivisionError:
    print("You can't divide by zero")

#another

print("Give 2 numbers, and I'll divide them")
print("Enter 'q' to quit")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
        print(answer)
    except ZeroDivisionError:
        print("You can't divide by 0")

    except ValueError:
        print("Please, use numbers only.")

    
