# TODO 1 : Import and print the logo from art.py when the program starts
from art import logo
print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# TODO 2 : What happens if the user enters a number/symbol/space

def caesar(originalText, shiftAmount, encodeORdecode):
    outputText = ""
    if encodeORdecode == "decode":
        shiftAmount *= -1
    for letter in originalText:
        if letter not in alphabet:
            outputText += letter
        else:

            shiftedPosition = alphabet.index(letter) + shiftAmount
            shiftedPosition = shiftedPosition % len(alphabet)
            outputText += alphabet[shiftedPosition]

    print(f"Here is the {encodeORdecode}d result: {outputText}")


# TODO 3 : Can you figure out a way to restart the cipher program?

shouldContinue = True
while shouldContinue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift:\n"))

    caesar(originalText= text,shiftAmount= shift,encodeORdecode= direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        shouldContinue = False
        print("Good Bye.")

