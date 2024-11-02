
### README for Part 2

```markdown
# Part 2 - Decryption

In this part, we enhance the project to include decryption functionality. This allows users to decode previously encrypted messages.

## Code Overview

- **Input**: The user inputs a message, a shift value, and chooses to encode or decode.
- **Functionality**: The `decrypt` function reverses the shift applied during encryption.
```
### Code Snippet

```python
def decrypt(originalText, shiftAmount):
    outputText = ""
    for letter in originalText:
        shiftedPosition = alphabet.index(letter) - shiftAmount
        shiftedPosition = shiftedPosition % len(alphabet)
        outputText += alphabet[shiftedPosition]
    print(f"Here is the decoded result: {outputText}")
```
