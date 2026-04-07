def gugudan(dan):
    for i in range(1, 10):
        print(f"{dan}*{i}={dan * i}")

def main():
    dan = int(input("몇 단을 계산할까요?"))
    gugudan(dan)

if __name__=="__main__":
    main()