import string

alphabets = list(string.ascii_lowercase)

print(f'Alphabets: {alphabets}')

direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        if letter in alphabets:
            shifted_position = (alphabets.index(letter) + shift_amount) % 26
            cipher_text += alphabets[shifted_position]
        else:
            cipher_text += letter

    print(f"Encrypted text: {cipher_text}")


encrypt(text, shift)