def text_len(len_text):
    x= len(len_text)
    return x

def text_average(average_text):
    xx= sum(average_text)/len(average_text)
    return xx

def text_max(max_text):
    xxx= max(max_text)
    return xxx

def text_min(min_text):
    xxx= min(min_text)
    return xxx

def text_mid(mid_text):
    mid_text.sort()
    xxxx= mid_text[len(mid_text)//2]
    return xxxx

def read_text(filename):
    with open(filename) as f:
        text= f.readline()
    return text

def main():
    input_text= read_text("numbers1.txt")
    num=[int(n) for n in input_text.split()]
    print(f"총 숫자는 {text_len(num)}개 입니다.")
    print(f"숫자의 평균은 {text_average(num):.1f}")
    print(f"최댓값은 {text_max(num)}")
    print(f"최솟값은 {text_min(num)}")
    print(f"중간값은 {text_mid(num)}")

if __name__=="__main__":
    main()