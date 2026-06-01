import random

def get_initial(word):
    initial_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    result = ""
    for i in word:
        num = ord(i) - 44032
        chosung = num // 588
        result += initial_list[chosung]
    return result

def initial_list():
    word_list=["사과", "바나나", "파이썬", "노트북", "학교"]
    select_word = random.choice(word_list)
    select_chosung = get_initial(select_word)
    print(f" 제시된 초성({select_chosung})을 보고 단어를 맞추세요.")
    ans= input()
    if ans == select_word:
        return True
    else:
        return False

def main():
    score = 0
    for r in range(2):
        if initial_list():
            score += 50
    print(f"총 점수는 {score}점입니다.")

if __name__=="__main__":
    main()