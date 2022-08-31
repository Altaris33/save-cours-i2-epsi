# python crypto test for simple files
# using symetric algorithm so the same key will crypt and decrypt
# unique key, so we will load it to have it on demand
# python 3 required

from cryptography.fernet import Fernet

def write_key():
    """
    Generates a key and write it to a file
    """
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named 'key.key'
    """        
    return open('key.key', 'rb').read()

# generating and writing the key
write_key()
key = load_key()
a_message_to_encrypt = "Yoshi has won against Mario in SSBM".encode()    

# crypt by first converting a string to bytes
# Initializing the Fernet class
f = Fernet(key)

# encrypt the message
# ecnrypt the data (string) passed as a Ferent token
encrypted_message = f.encrypt(a_message_to_encrypt)  

print(f'Encrypted data looks like this: {encrypted_message}')

# decrypting the crypted data
# decrypt() decrypts a Fernet token
decrypted_message = f.decrypt(encrypted_message)

print(f'Decrypted data looks like this: {decrypted_message}')

#---------------- FILE ENCRYPTION--------------------------

def encrypt_file(filename, key):
    """
    Generate a crypted file based on a plain text file
    """
    f = Fernet(key)

    with open(filename, 'rb') as file: 
        # read all file data
        file_data = file.read()

    encrypted_data_from_file = f.encrypt(file_data)

    with open(filename, 'wb') as file:
        file.write(encrypted_data_from_file)

# ---------------- FILE DESCRYPTION-----------------------
def decrypt_file(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)    

key = load_key()

input_file = "data.txt"
encrypt_file(input_file, key)
print('\n')
decrypt_file(input_file, key)
