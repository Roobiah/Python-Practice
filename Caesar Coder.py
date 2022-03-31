from caesar_coder_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceasar(message, no_of_shift, your_direction):
    new_message = ""
    if your_direction == "decode":
        no_of_shift *= -1
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + no_of_shift
            new_message = new_message + alphabet[new_position]
        else:
            new_message += char
    print(f"The {your_direction}d text is {new_message}")


print(logo)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    if shift == 0:
        shift -= 1
    ceasar(your_direction=direction, message=text, no_of_shift=shift)
    re_run = input("Type yes if you want to go again. Otherwise type no:\n").lower()
    if re_run == 'no':
        should_continue = False
        print("Goodbye")
