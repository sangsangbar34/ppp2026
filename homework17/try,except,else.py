def str2int(x):
    try:
        val = int(x)
    except ValueError:
        return None
    else:
        if val == -1:
            return -1
        elif val > 0:
            return val
        else:
            return None

def main():
    values = []
    while True:
        x= input("X=>?")
        x_value = str2int(x)
        if x_value == -1:
            break
        if x_value is not None:
            values.append(x_value)
    if len(values) > 0:
        avg = sum(values) / len(values)
        print(f"입력된 값은 {values} 입니다. 총 {len(values)}개의 자연수가 입력되었고, 평균은 {avg:.1f}입니다.")
    else:
        print("입력된 자연수가 없습니다.")

if __name__=="__main__":
    main()