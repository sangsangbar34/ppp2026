import random

def gugudan_correct():
    a = random.randint(2,9)
    b = random.randint(1,9)
    ans = input(f"{a} X {b} ==> ")
    return int(ans) ==a*b

def main():
    score = 0
    for r in range(10):
        if gugudan_correct():
            score += 10
    print(f"총 점수는 {score}점입니다.")

if __name__=="__main__":
    main()