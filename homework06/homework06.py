dan=int(input("몇 단을 계산할까요?"))
for i in range(1, 10):
    print(f"{dan}*{i}={dan*i}")

star=int(input("별을 몇 개 그릴까요?"))
for i in range(1,star+1):
    print('*' * i)

import math
print("라디안:1번, sin:2번, cos:3번, tan:4번")
Q=int(input("무슨 삼각함수표를 만들까요?"))
for i in range(11):
    radian=i*math.pi/180
    if Q==1:
        print(f"{i}˚= {radian:.4f}")
    elif Q==2:
        sin=math.sin(radian)
        print(f"{i}˚= {sin:.4f}")
    elif Q==3:
        cos=math.cos(radian)
        print(f"{i}˚= {cos:.4f}")
    elif Q==4:
        tan=math.tan(radian)
        print(f"{i}˚= {tan:.4f}")
    else:
        X = "올바른 숫자를 입력해주세요"
        print(X)