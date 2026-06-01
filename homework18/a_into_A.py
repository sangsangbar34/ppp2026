def toggle_ch(alphabet):
    if ord(alphabet) >= 65 and ord(alphabet) <= 90:
        return chr(ord(alphabet) + 32)
    elif ord(alphabet) >= 97 and ord(alphabet) <= 122:
        return chr(ord(alphabet) - 32)
    return alphabet

def toggle_text(text):
    result= ""
    for c in text:
        result += toggle_ch(c)
    return result

def main():
    print(toggle_ch("a"))
    print(toggle_text("hOME wORK 18"))

if __name__=="__main__":
    main()