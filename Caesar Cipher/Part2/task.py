alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift:\n"))

def encrypt(originalText, shiftAmount):
    cipherText = ""

    for letter in originalText:
        shiftedPosition = alphabet.index(letter) + shiftAmount
        shiftedPosition = shiftedPosition % len(alphabet)
        cipherText+= alphabet[shiftedPosition]

    print(f"Here is the encoded result: {cipherText}")

# TODO 1 : Create a function called 'decrypt()' that takes 'originalText' and 'shiftAmount' as 2 inputs
# TODO 2 : Inside the decrypt() function, shift each letter of the originalText forward in the alphabet backwards by the shiftAmount and print the decrypted text
def decrypt(originalText, shiftAmount):
    outputText = ""
    for letter in originalText:
        shiftedPosition = alphabet.index(letter) - shiftAmount
        shiftedPosition = shiftedPosition % len(alphabet)
        outputText += alphabet[shiftedPosition]

    print(f"Here is the decoded result: {outputText}")

# TODO 3 : Combine the 'encrypt()' and decrypt() functions into one function called caesar(). Use the value of the user chosen direction variable to determine which functionality to use


#encrypt(originalText=text, shiftAmount=shift)
#decrypt(originalText=text, shiftAmount=shift)

def caesar(originalText, shiftAmount, encodeORdecode):
    outputText = ""
    for letter in originalText:
        if encodeORdecode == "decode":
            shiftAmount *= -1

        shiftedPosition = alphabet.index(letter) + shiftAmount
        shiftedPosition = shiftedPosition % len(alphabet)
        outputText += alphabet[shiftedPosition]

    print(f"Here is the {encodeORdecode}d result: {outputText}")

caesar(text, shift, direction)