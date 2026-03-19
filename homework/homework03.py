temp_c=int(input("온도℃를 입력하세요"))
temp_f=(temp_c*9/5)+32
print(f"{temp_c}℃ => {temp_f}℉")

w=float(input("몸무게(kg)를 입력하세요"))
h=float(input("키(m)를 입력하세요"))
BMI= f"BMI는 {w / (h**2)}입니다."
print(BMI)

import math
r=int(input("반지름(cm)을 입력하세요"))
area=f"원의 넓이는 {r**2*math.pi}입니다."
print(area)

밑변=int(input("밑변(cm)을 입력하세요"))
윗변=int(input("윗변(cm)을 입력하세요"))
높이=int(input("높이(cm)를 입력하세요"))
사다리꼴=f"사다리꼴의 넓이는 {(밑변+윗변)*높이/2}입니다."
print(사다리꼴)

import math
x1=int(input("x1좌표를 입력하세요"))
x2=int(input("x2좌표를 입력하세요"))
y1=int(input("y1좌표를 입력하세요"))
y2=int(input("y2좌표를 입력하세요"))
distance= math.sqrt((x2-x1)**2+(y2-y1)**2)
print(f"두점사이의 거리는 {distance} 입니다.")

Hanrabong=int(input("한라봉 무게(g)를 입력하세요"))
Hkcal=f"한라봉은 {Hanrabong/2}kcal 입니다."
print(Hkcal)
Strawberry=int(input("딸기 무게(g)를 입력하세요"))
Skcal=f"딸기는 {Strawberry*0.34}kcal 입니다."
print(Skcal)
Banana=int(input("바나나 무게(g)를 입력하세요"))
Bkcal=f"바나나는 {Banana*0.77}kcal 입니다."
print(Bkcal)
