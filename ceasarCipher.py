"""
Ceasar cipher project
Date: 11/13/2022'yui
"""


# def encrypt(text, shift_amount):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter) #f ind the index of that letter in the list
#         new_position = position + shift_amount #update the position
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter #update the new string
#
#     print(f"The encoded text is: {cipher_text}")
#     return cipher_text

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction} text is {end_text}")
    print()


# def decrypt(cipher_text, shift_amount):
#     shift_amount = input("Please type in the shift code: ")
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"The decoded text is {plain_text}")


def main():

    global alphabet

    while True:

        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z']

        print("CeasarCipher App. V1.0")
        print("Encrypt and decode any word with a shift number.")
        print("***************************************************************************")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))

        caesar(text,shift, direction)

        choice = input("Would you like to encode or decore another text [y or n]: ").lower()
        if choice == "yes" or "y":
            return True
        elif choice == "no" or "n":
            return False
        else:
            print('Please type in a y or n please. Try again.')
            return False

    print("Thank you for making use of the caesarCipher application.")


if __name__ == '__main__':
    main()