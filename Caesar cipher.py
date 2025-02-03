import string 
alpha = string.ascii_lowercase
ALPHA = string.ascii_uppercase

def encrypt_text(plain_text, key):
    encrypted_text = ""
    for char in plain_text:
        if char in alpha:
            index = alpha.index(char)
            new_index = (index + key) % 26
            encrypted_text += alpha[new_index]
        elif char in ALPHA:
            index = ALPHA.index(char)
            new_index = (index + key) % 26
            encrypted_text += ALPHA[new_index]
        else:
            encrypted_text += char   
    print(encrypted_text)     

def decrypt_text(key, cipher_text):
    decrypted_text = ""  
    for char in cipher_text:
        if char in alpha:
            index = alpha.index(char)
            new_index = (index - key) % 26
            decrypted_text += alpha[new_index]
        elif char in ALPHA:
            index = ALPHA.index(char)
            new_index = (index - key) % 26
            decrypted_text += ALPHA[new_index]
        else:
            decrypted_text += char
    print(decrypted_text)

yes = input("Do you want to encrypt (0) or decrypt (1)? ")
if yes == '0' or yes.lower() == 'yes':
    inppha = input("Enter the text to be encrypted:\n")
    key = int(input("Enter the encryption key:\n"))
    encrypt_text(inppha, key)
elif yes == '1' or yes.lower() == 'no':
    message = input("Type the text to be decrypted:\n")
    key = int(input("Enter the decryption key:\n"))
    decrypt_text(key, message)
else:
    print("Bro, reply to the request, it's easy!\n")
