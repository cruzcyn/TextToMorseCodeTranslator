from morse_code import morse_code

translating = True

while translating:
    should_continue = input("Do you want to translate a message? Type 'Y' or 'N': ").upper()

    if should_continue == "Y":
        message = input("What's the message? ")
        action = input("Do you want to encode or decode the message? ").lower()

        if action == "encode":
            # Split characters into a list so that we can search one by one in the dictionary:
            list_of_characters = list(message)

            # "Translate" the given input to morse code using the values from the morse_code dictionary:
            message_to_morse_code = [morse_code[char] for char in message]

            # Join the list into a string separating each character with a space to make decoding easier:
            message_to_morse_code = " ".join(message_to_morse_code)
            print(f"Here's your message. Keep it safe: {message_to_morse_code}")
        elif action == "decode":
            # Split characters into a list:
            list_of_characters = message.split(" ")

            # Search the dictionary by values so that we can get the letters (keys) for our translated message:
            message_to_eng = []
            for char in list_of_characters:
                for letter, code in morse_code.items():
                    if code == char:
                        message_to_eng.append(letter)

            # Join the translated message into a string:
            message_to_eng = "".join(message_to_eng)
            print(f"Here's your translated message: {message_to_eng}")
        else:
            print("Invalid input. Try again.")

    else:
        translating = False
        print("Bye!")
