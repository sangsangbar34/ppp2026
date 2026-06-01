def caesar_encode(alphabet, cae=3):
    if ord(alphabet) >= 65 and ord(alphabet) <= 90-cae:
        return chr(ord(alphabet) + cae)
    elif 91-cae<= ord(alphabet) <=90:
        return chr(ord(alphabet) - 26 + cae)
    elif ord(alphabet) >= 97 and ord(alphabet) <= 122-cae:
        return chr(ord(alphabet) + cae)
    elif 123-cae<= ord(alphabet) <=122:
        return chr(ord(alphabet) - 26 + cae)
    return alphabet

def caesar_decode(alphabet, cae=3):
    if ord(alphabet) >= 65 + cae and ord(alphabet) <= 90:
        return chr(ord(alphabet) - cae)
    elif 65<= ord(alphabet) <=64+cae:
        return chr(ord(alphabet) + 26 - cae)
    elif ord(alphabet) >= 97+cae and ord(alphabet) <= 122:
        return chr(ord(alphabet) - cae)
    elif 97<= ord(alphabet) <=96+cae:
        return chr(ord(alphabet) + 26-cae)
    return alphabet

def main():
    print(caesar_encode("a"))
    print(caesar_encode("A"))
    print(caesar_decode("d"))
    print(caesar_decode("D"))

if __name__=="__main__":
    main()