import base64
import binascii
import sys

def c_xor_p(c, p):
    return map(lambda x: x[0] ^ x[1], zip(map(ord, c), map(ord, p)))

def k_xor_c(k, c):
    string = ''
    for i in xrange(len(c)):
        if i >= len(k):
            break
        else:
            string += chr(c[i] ^ k[i])
    return string

def a_xor_b(a, b):
    arr = []
    for i in range(len(a)):
        arr.append(str(int(a[i]) ^ int(b[i])))
    bin_string = ''.join(arr)
    return bin_string

def get_lines(filename):
    f_in = open(filename, "r")
    arr_lines = []
    for line in f_in.read().split("\n"):
        arr_lines.append(line)
    return arr_lines

def hex_to_bin(string):
    return bin(int(base64.b64decode(string).encode("hex"), 16)).replace("b", "")

def generate_key_size_of_ciphertext(line, bin_key):
    arr = []
    bin_line = hex_to_bin(line)[1:]
    len_bin_line = len(bin_line) / 128
    for i in range(len_bin_line+ 1):
        arr.append(bin_key)
    result = ''.join(arr)
    return result[:len(bin_line)]

def hash_to_bin_char(string, chunk_size):
    return [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]

def main(argv):
    # Help formula
    # (plaintext) xor (ciphertext) = (key)

    if len(argv) < 2:
        sys.stderr.write("Usage: %s" % (argv[0]))

    filename = sys.argv[1]
    b64_lines = get_lines(filename)

    print "[ chosen text ]"
    chosen_plain_text = 'The Jargon File '
    print chosen_plain_text
    raw_chosen_cipher_text = b64_lines[0]
    chosen_cipher_text = base64.b64decode(raw_chosen_cipher_text)
    print "\n"

    xored_c_p = c_xor_p(chosen_cipher_text, chosen_plain_text)
    raw_cipher_text = b64_lines[1]
    cipher_text = base64.b64decode(raw_cipher_text)

    print "[ plain text ]"
    raw_plain_text = k_xor_c(xored_c_p, map(ord, cipher_text))
    print raw_plain_text
    print "\n"

    print "[ plain text bin ]", "->", raw_plain_text
    bin_plain_text = bin(int(binascii.hexlify(raw_plain_text),16)).replace('b', '')
    print [len(bin_plain_text), "bits"], bin_plain_text
    print "\n"

    print "[ cipher text bin ]", "->", b64_lines[0]
    bin_cipher_text = hex_to_bin(b64_lines[0])[1:129]
    print [len(bin_cipher_text), "bits"], bin_cipher_text
    print "\n"

    print "[ key ]", "->", "key_bin = plaintext_bin xor ciphertext_bin"
    bin_key = a_xor_b(bin_plain_text, bin_cipher_text)
    print [len(bin_key), "bits"], bin_key
    print '\n'

    print "[ clear Text ]"
    for i in range(len(b64_lines)):
        a = hex_to_bin(b64_lines[i])[1:]
        b = generate_key_size_of_ciphertext(b64_lines[i], bin_key)
        xored_bin_result = a_xor_b(a, b)
        bin_array_of_char = hash_to_bin_char(xored_bin_result, 8)
        final_result = []
        for i in range(len(bin_array_of_char)):
            final_result.append(chr(int(bin_array_of_char[i], 2)))
        print ''.join(final_result)
    print '\n'

if __name__ == "__main__":
    sys.exit(main(sys.argv))
