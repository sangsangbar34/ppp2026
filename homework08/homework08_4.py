def sum_n(n):
    total=0
    for i in range(1,n+1):
        total += i
    return total

def main():
    n = int(input("정수를 입력하세요"))
    print(sum_n(n))

if __name__=="__main__":
    main()