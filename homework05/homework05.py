print("변환하고 싶은 번호를 입력하세요")
Q=int(input("1.화씨(℃)->섭씨(℉), 2.섭씨(℉)->화씨(℃), 3.피트(ft)->cm, 4.cm->피트(ft)"))
if Q==1 :
    temp_f=float(input("온도℉를 입력하세요."))
    temp_c=(temp_f-32)*(5/9)
    print("{}℉ => {:.1f}℃입니다.".format(temp_f,temp_c))
elif Q==2 :
    temp_c = float(input("온도℃를 입력하세요"))
    temp_f = (temp_c * 9 / 5) + 32
    print("{}℃ => {:.1f}℉입니다.".format(temp_c, temp_f))
elif Q==3 :
    FT= float(input("길이(ft)를 입력하세요."))
    CM= FT*30.48
    print("{}(ft) => {:.1f}(cm)입니다.".format(FT, CM))
elif Q==4 :
    CM= float(input("길이(cm)를 입력하세요."))
    FT= CM/30.48
    print("{}(cm) => {:.1f}(ft)입니다.".format(CM, FT))
else :
    print("잘 못 된 값입니다")
