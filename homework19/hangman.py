import random

def get_initial():
    word_list = ['apple', 'banana']
    select_word = random.choice(word_list)
    word_split = list(select_word)
    blank_list = []
    blank_list += '_' * len(word_split)
    return select_word, word_split, blank_list

def main():
    print("Game Start")
    select_word, word_split, blank_list = get_initial()
    trial = 7
    while True:
        if trial == 0:
            print("You Lose")
            break
        if not '_' in blank_list:
            print(f"[{"".join(blank_list)}] You Win")
            break

        ans = input(f"[{"".join(blank_list)}] trial: {trial} => ")
        if ans in word_split:
            for i in range(len(word_split)):
                if word_split[i] == ans:
                    blank_list[i] = ans
        else:
            print("틀렸습니다")
            trial -= 1

if __name__=="__main__":
    main()