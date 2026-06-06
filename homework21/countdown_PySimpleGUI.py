import time
import PySimpleGUI as sg

def main():
    while True:
        layout = [[sg.Text("카운트다운 할 초를 입력하세요:")],
            [sg.InputText(key='sec')],
            [sg.Button('Ok'), sg.Button('Cancel')]]

        window = sg.Window('입력창', layout)
        event, values = window.read()
        window.close()

        if event in (sg.WIN_CLOSED, 'Cancel'):
            return

        if values['sec'] and values['sec'].isdigit():
            start_num = int(values['sec'])
            break

        sg.popup("숫자만 입력해 하세요")

    for i in range(start_num, 0, -1):
        sg.popup_no_buttons(f"{i:3d}초 남았습니다...", title="카운트다운", non_blocking=True, auto_close_duration=1,
                            auto_close=True)
        time.sleep(1)


if __name__ == "__main__":
    main()