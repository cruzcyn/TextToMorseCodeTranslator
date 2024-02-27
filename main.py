from morse_code import morse_code

translating = True

while translating:
    should_continue = input("Do you want to translate a message? Type 'Y' or 'N': ").upper()

    if should_continue == "Y":
        message = input("What's the message? ")
        action = input("Do you want to encode or decode the message? ").lower()

        if action == "encode":
            # TODO: write logic
        elif action == "decode":
            # TODO: write logic
        else:
            print("Invalid input. Try again.")

    else:
        translating = False
        print("Bye!")