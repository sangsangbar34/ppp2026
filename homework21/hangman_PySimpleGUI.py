import random
import PySimpleGUI as sg

def get_initial():
    word_list = ['apple', 'banana', 'smartfarm', 'python']
    select_word = random.choice(word_list)
    return select_word, list(select_word), ['_'] * len(select_word)

def main():
    select_word, word_split, blank_list = get_initial()
    trial = 7
    layout = [[sg.Text(" ".join(blank_list), key='-WORD-', font=('Arial', 20))],
              [sg.Text(f"남은 기회: {trial}", key='-TRIAL-')],
              [sg.InputText(key='-INPUT-', size=(5,1)), sg.Button('Guess')],
              [sg.Button('Exit')]]
    window = sg.Window('Hangman GUI', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'): break
        ans = values['-INPUT-'].lower()
        window['-INPUT-'].update('')

        if ans in word_split:
            for i in range(len(word_split)):
                if word_split[i] == ans: blank_list[i] = ans
            window['-WORD-'].update(" ".join(blank_list))
        else:
            trial -= 1
            window['-TRIAL-'].update(f"남은 기회: {trial}")

        if '_' not in blank_list:
            sg.popup(f"Win! 정답: {select_word}"); break
        if trial == 0:
            sg.popup(f"Lose... 정답: {select_word}"); break
    window.close()

if __name__ == "__main__": main()