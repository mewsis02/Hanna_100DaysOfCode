alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
print("")


def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        new_letter_location = alphabet.index(letter) + shift_amount
        if new_letter_location >= 26:
            new_letter_location -= 26
        the_new_letter = alphabet[new_letter_location]
        encrypted_text += the_new_letter
    print(f"Your encoded text is: {encrypted_text}")


encrypt(original_text=text, shift_amount=shift)
