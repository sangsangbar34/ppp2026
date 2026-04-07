def average(nums):
    result = sum(nums) / len(nums)
    return result

def main():
    x=[3, 7, 5]
    print(f"평균은 {average(x):.1f}입니다.")

if __name__=="__main__":
    main()