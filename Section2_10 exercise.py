while True:
  try:
    user_age = int(input("How old are You?: "))
    break  # exit the loop if conversion is successful
  except ValueError:
    print("Please enter a valid whole number for Your age.")

if user_age >= 18 and user_age <= 45:
    print("Enjoy the ride ")
elif user_age < 18:
    print("too young")
elif user_age > 45:
    print("too old")

else:
    print("Hi Mojżesz")


print(user_age)
print(type(user_age))
