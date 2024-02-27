from morse_code import morse_code

translating = True

while translating:
    should_continue = input("Do you want to translate a message? Type 'Y' or 'N': ").upper()

    if should_continue == "Y":
        message = input("What's the message? ")
        action = input("Do you want to encode or decode the message? ").lower()

        list_of_characters = list(message)

        if action == "encode":
            # "Translate" the given input to morse code using the values from the morse_code dictionary:
            message_to_morse_code = [morse_code[char] for char in message]

            # Join the list into a string separating each character with a space to make decoding easier:
            message_to_morse_code = " ".join(message_to_morse_code)
            print(f"Here's your message. Keep it safe: {message_to_morse_code}")
        elif action == "decode":
            pass
        else:
            print("Invalid input. Try again.")

    else:
        translating = False
        print("Bye!")
