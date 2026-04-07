def is_leap_year(y):
    if y%4 ==0 and y%100 != 0:
        print("윤년입니다.(True)")
    else:
        print("윤년이 아닙니다.(False)")

def main():
    x=int(input("연도를 입력하세요"))
    is_leap_year(x)
if __name__=="__main__":
    main()