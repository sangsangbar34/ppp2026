import random
import PySimpleGUI as sg


def gugudan_correct():
    a = random.randint(2, 9)
    b = random.randint(1, 9)

    while True:
        layout = [[sg.Text(f"문제: {a} X {b} = ?")],
            [sg.InputText(key='user_ans')],
            [sg.Button('Ok'), sg.Button('Cancel')]]

        window = sg.Window('구구단 퀴즈', layout)
        event, values = window.read()
        window.close()

        if event in (sg.WIN_CLOSED, 'Cancel'):
            return False

        if values['user_ans'] and values['user_ans'].isdigit():
            ans = int(values['user_ans'])
            break

        sg.popup("숫자로 정답을 입력하세요")

    return ans == a * b

def main():
    score = 0
    for r in range(10):
        if gugudan_correct():
            score += 10
            sg.popup("정답입니다 (+10점)", title="결과")
        else:
            sg.popup("틀렸습니다", title="결과")

    sg.popup(f"시험 종료!\n총 점수는 {score}점입니다.", title="최종 점수")

if __name__ == "__main__":
    main()