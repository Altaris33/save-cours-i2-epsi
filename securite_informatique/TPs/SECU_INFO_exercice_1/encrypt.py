import sys
import base64
from Crypto.Cipher import AES
from Crypto import Random


class Nonce(object):
    def __init__(self):
        self.value = Random.new().read(AES.block_size)
    def __call__(self):
        return self.value

def encrypt_line(cipher, line):
    return base64.b64encode(cipher.encrypt(line))

def encrypt_file(filename):
    key = Random.new().read(16)
    nonce = Nonce()
    
    f_in = open(filename, "r")
    f_out = open(filename + ".crypt", "w")
    
    for line in f_in.read().split("\n"):
        if len(line) > 1:
            cipher = AES.new(key, AES.MODE_CTR, counter=nonce)
            line_enc = encrypt_line(cipher, line)
            f_out.write(line_enc + "\n")
        
    
def main(argv):
    if len(argv) < 2:
        sys.stderr.write("Usage : %s <file>\n" % (argv[0]))
        return 1
    
    encrypt_file(argv[1])
    print "File encrypted : " + argv[1] + ".crypt"
    
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))


    
