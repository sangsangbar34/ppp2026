import random
import PySimpleGUI as sg

def get_Environment():
    Environment_list = ['want_water', 'want_fertilizer', 'want_LED']
    select_Environment = random.choice(Environment_list)
    return select_Environment

def main():
    current_state = get_Environment()
    trial = 3
    day = 1
    growth_rate = 60
    penalty_count = 0
    threat_count = 0

    if current_state == 'want_water':
        weather = "건조"
    elif current_state == 'want_fertilizer':
        weather = "맑음"
    elif current_state == 'want_LED':
        weather = "흐림"

    layout = [
        [sg.Text(f"날짜: xx월 {day}일", key='-DAY-', font=('Arial', 20)),
         sg.Text(f"남은 생명: {trial}", key='-TRIAL-', font=('Arial', 20))],
        [sg.Image(filename='0.png', key='-IMAGE-')],
        [sg.Text(f"오늘 날씨: {weather}", key='-WEATHER-', font=('Arial', 20))],
        [sg.Text(f"성장률: {growth_rate}%", key='-GROWTH-', font=('Arial', 20))],
        [sg.Button('물 주기', size=(12, 2), font=('Arial', 20)),
         sg.Button('비료 주기', size=(12, 2), font=('Arial', 20)),
         sg.Button('LED조명 쬐기', size=(12, 2), font=('Arial', 20))],
        [sg.Button('Exit', size=(8, 1), font=('Arial', 20))]
    ]
    window = sg.Window('식물 키우기', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            return

        if current_state == 'want_water':
            correct_button = '물 주기'
        elif current_state == 'want_fertilizer':
            correct_button = '비료 주기'
        elif current_state == 'want_LED':
            correct_button = 'LED조명 쬐기'

        if event == correct_button:
            growth_rate += 10
        else:
            trial -= 1
            sg.popup("잘못된 조치입니다.")

        if growth_rate<100 and trial>0:
            day +=1
            if growth_rate >= 80:
                fifty_dice_two = random.randint(1,2)
                if fifty_dice_two == 1:
                    threat_count += 1
                    trial -= 1
                    sg.popup("[돌발 상황]\n열과 현상 발생\n 목숨 -1")
                else:
                    pass

            if growth_rate >= 80:
                fifty_dice = random.randint(1, 3)
                if fifty_dice == 1:
                    before_growth = growth_rate
                    penalty_count += 1
                    growth_rate -= 10
                    sg.popup(f"[돌발 위협!]\n토마토 뿔나방 발생\n 성장률 변동: {before_growth}% → {growth_rate}% (-10%)")
                else:
                    pass
            current_state = get_Environment()
            if current_state == 'want_water':
                weather = "건조"
            elif current_state == 'want_fertilizer':
                weather = "맑음"
            elif current_state == 'want_LED':
                weather = "흐림"

        if trial <=0:
            img_file = 'dead.png'
        elif growth_rate >= 100:
            img_file = '100.png'
        elif growth_rate >= 80:
            img_file = '90.png'
        elif growth_rate >= 60:
            img_file = '60.png'
        elif growth_rate >= 30:
            img_file = '30.png'
        else:
            img_file = '0.png'

        window['-DAY-'].update(f"날짜: xx월 {day}일")
        window['-WEATHER-'].update(f"오늘 날씨: {weather}")
        window['-IMAGE-'].update(filename=img_file)
        window['-GROWTH-'].update(f"성장률: {growth_rate}%")
        window['-TRIAL-'].update(f"남은 생명: {trial}")

        if trial <= 0:
            if threat_count ==3:
                window['-WEATHER-'].update("자연재해를 받아들이세요.", font=('Arial', 28), text_color='#ff0000')
                window['-DAY-'].update(f"(생존 {day}일)", text_color='#dee2e6')
                window['-TRIAL-'].update("남은 생명: 0 (천재지변)", text_color='#ff0000')
                window['-GROWTH-'].update("운이 없으시군요", text_color='#ff0000')
                window['-IMAGE-'].update(filename='dead2.png')
                sg.popup("[HIDDEN ENDING]\n\n\"자연재해를 받아들이세요.\"")
            else:
                window['-TRIAL-'].update("남은 생명: 0 (죽음)")
                window['-WEATHER-'].update(f"{day}일 만에 시들어 죽음", text_color='#70e000')
                window['-DAY-'].update(f"나방 횟수: {penalty_count}번", text_color='#dee2e6')
                window['-GROWTH-'].update(f"종료 당시 성장률: {growth_rate}%", text_color='#ffff00')
                sg.popup("식물이 죽었습니다.")
            break

        elif growth_rate >= 100:
            window['-GROWTH-'].update("성장률: 100% (재배 완료!)")
            window['-WEATHER-'].update(f"총 소요 기간: {day}일 걸림!", text_color='#ffb703')
            window['-DAY-'].update(f"위협 당한 횟수: 총 {penalty_count}번")
            window['-TRIAL-'].update(f" 남은 목숨: {trial}", text_color='#00ff00')
            sg.popup("토마토 재배 성공!")
            break

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

    window.close()

if __name__ == "__main__": main()