question = "How old are you?"
question += "\nEnter 'quit' when you are finished. "

while True:
    age = input(question)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")