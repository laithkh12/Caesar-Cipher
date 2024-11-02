alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift:\n"))

# TODO 1 : Create a function called 'encrypt()' that takes 'originalText' and 'shiftAmount' as 2 inputs
# TODO 2 : Inside the 'encrypt()' function, shift each letter of the 'originalText' forwards in the alphabet by the 'shiftAmount' and print the encrypted text
def encrypt(originalText, shiftAmount):
    cipherText = ""

    # TODO 4 : What happens if you try to shift z forwards by 9? Can you fix the code?

    for letter in originalText:
        shiftedPosition = alphabet.index(letter) + shiftAmount
        shiftedPosition = shiftedPosition % len(alphabet)
        cipherText+= alphabet[shiftedPosition]

    print(f"Here is the encoded result: {cipherText}")


# TODO 3 : Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a message

encrypt(originalText=text, shiftAmount=shift)