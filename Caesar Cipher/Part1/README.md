
### README for Part 1

```markdown
# Part 1 - Encryption

In this part of the project, we implement the basic functionality to encrypt a message using a Caesar cipher.

## Code Overview

- **Input**: The user inputs a message and a shift value.
- **Functionality**: The `encrypt` function takes the original text and shifts each letter by the specified amount.
```
### Code Snippet

```python
alphabet = [ ... ]  # full alphabet list

def encrypt(originalText, shiftAmount):
    cipherText = ""
    for letter in originalText:
        shiftedPosition = alphabet.index(letter) + shiftAmount
        shiftedPosition = shiftedPosition % len(alphabet)
        cipherText += alphabet[shiftedPosition]
    print(f"Here is the encoded result: {cipherText}")
```
