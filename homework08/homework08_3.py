def c2f(temp_c):
    temp_f = (temp_c * 9 / 5) + 32
    return temp_f

def main():
    temp_c = float(input("온도℃를 입력하세요"))
    print(f"{temp_c}℃ => {c2f(temp_c):.1f}℉입니다.")

if __name__=="__main__":
    main()