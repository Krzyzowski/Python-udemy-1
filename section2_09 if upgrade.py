user = input("Enter Your name: ")

if user.lower().startswith("karl") and user[1:].islower():
  print("Welcome back " + user)
else:
  print("Incorrect")