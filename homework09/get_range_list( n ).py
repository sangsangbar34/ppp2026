def get_range_list(n):
    range_list=[]
    for i in range(1,n+1):
        range_list.append(i)
    return range_list

def main():
    x=int(input("어떤 숫자까지 리스트를 돌릴까요?"))
    print(get_range_list(x))

if __name__=="__main__":
    main()