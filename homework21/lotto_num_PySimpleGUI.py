import random
import PySimpleGUI as sg


def get_lotto():
    num_list = random.sample(range(1, 46), 6)
    num_list.sort()
    return num_list

def main():
    while True:
        layout = [[sg.Text("로또 번호를 몇 번 추출할까요?")],
            [sg.InputText(key='cnt')],
            [sg.Button('추첨 시작'), sg.Button('Cancel')]]
        window = sg.Window('로또 번호 생성기', layout)
        event, values = window.read()
        window.close()

        if event in (sg.WIN_CLOSED, 'Cancel'):
            return

        if values['cnt'] and values['cnt'].isdigit():
            x = int(values['cnt'])
            break

        sg.popup("올바른 숫자만 입력해 주세요")

    total_result = ""

    for i in range(x):
        lotto_res = get_lotto()
        total_result += f"{i + 1}번째 추첨: {lotto_res}\n"

    sg.popup_scrolled(total_result, title="로또 추첨 결과", size=(40, 15))

if __name__ == "__main__":
    main()