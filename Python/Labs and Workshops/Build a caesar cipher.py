"""
Caesar Cipher Encryption/Decryption Tool

This project implements a simple Caesar cipher in Python. A Caesar cipher is a
basic encryption technique that shifts each letter in a message by a fixed number
of positions in the alphabet.

Features:
- Supports both encryption and decryption
- Handles both lowercase and uppercase letters
- Validates input to ensure the shift value is an integer between 1 and 25
- Preserves non-alphabetic characters (e.g., spaces and punctuation)

Functions:
- caesar(text, shift, encrypt=True):
    Core function that applies the Caesar cipher. It shifts characters forward
    for encryption and backward for decryption.

- encrypt(text, shift):
    Wrapper function that encrypts the given text using the specified shift.

- decrypt(text, shift):
    Wrapper function that decrypts the given text using the specified shift.

Example:
    encrypt("Hello", 3) -> "Khoor"
    decrypt("Khoor", 3) -> "Hello"

This project demonstrates string manipulation, use of str.maketrans() and
str.translate(), and basic input validation in Python.


Built as part of FreeCodeCamp Python practice
"""



def caesar(text, shift, encrypt = True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    
    if shift < 1 or shift > 25 :
        return 'Shift must be an integer between 1 and 25.'
    if not encrypt:
        shift = -shift


    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)



def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, False)


# encrypted_text = encrypt('FreeCodeCamp.', 3)


encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(f"Encrypted text: {encrypted_text}")
print(f"Decrypted text: {decrypted_text}")