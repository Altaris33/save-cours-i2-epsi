# decryption file
# decrypted file
# lecture de la première ligne
import sys
import base64
from Crypto.Cipher import AES
from Crypto import Random

def decrypt_line(cipher, line):
    first_line = 'h1vQUSwOaAwW/YGeohomhO8='
    first_line
    return base64.b64encode(cipher.decrypt(line))

def decrypt_file(filename):
    """This functions will decrypt a file, using end of line as
    separator

    Args:
        filename (file): name of file to pass as argument

    Returns:
        no return: no specific return (void-like logic)
    """
    
    # use the retrieved key from Chosen text attack
    # key = value

    f_in = open(filename, "rb")
    f_out = open(filename + ".decrypted", "w")

    for line in f_in.read().split("\n"):
        pass
        # base64
        # 

    return "some thing to return"

def main(argv):
    pass

def add_func(num1, num2):
    


# if the script is directly launched
if __name__ == "__main__":
    sys.exit(main(sys.argv))