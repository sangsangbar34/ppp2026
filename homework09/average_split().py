def average(nums):
    result = sum(nums) / len(nums)
    return result

def main():
    input_text=input("평균을 구할 숫자들을 입력하세요(쉼표를 넣어주세요)")
    x=[int(n) for n in input_text.split(",")]
    print(f"평균은 {average(x):.1f}입니다.")

if __name__=="__main__":
    main()