temp_c=int(input("온도를 입력하세요"))
temp_f=(temp_c*9/5)+32
print(f"{temp_c}℃ => {temp_f}F")

w=float(input("몸무게를 입력하세요"))
h=float(input("키를 입력하세요"))
BMI= f"{w / (h**2)}"
print(BMI)

import math
r=int(input("반지름을 입력하세요"))
area=f"{r**2*math.pi}"
print(area)

밑변=int(input("밑변을 입력하세요"))
윗변=int(input("윗변을 입력하세요"))
높이=int(input("높이를 입력하세요"))
사다리꼴=(f"{(밑변+윗변)*높이/2}")
print(사다리꼴)

import math
x1=int(input("x1좌표를 입력하세요"))
x2=int(input("x2좌표를 입력하세요"))
y1=int(input("y1좌표를 입력하세요"))
y2=int(input("y2좌표를 입력하세요"))
distance= math.sqrt((x2-x1)**2+(y2-y1)**2)
print(distance)

Hanrabong=int(input("한라봉 무게(g)를 입력하세요"))
Hkcal=f"한라봉은 {Hanrabong/2}kcal 입니다."
print(Hkcal)
Strawberry=int(input("딸기 무게(g)를 입력하세요"))
Skcal=f"딸기는 {Strawberry*0.34}kcal 입니다."
print(Skcal)
Banana=int(input("바나나 무게(g)를 입력하세요"))
Bkcal=f"바나나는 {Banana*0.77}kcal 입니다."
print(Bkcal)
