w=float(input("몸무게(kg)를 입력하세요"))
h=float(input("키(cm)를 입력하세요"))
BMI= w / (h**2)*10000
if BMI<24.9:
    print(f"당신의 BMI는 {BMI}kg/㎡ 비만 전단계입니다.")
elif 25<= BMI <30:
    print(f"당신의 BMI는 {BMI}kg/㎡ 1단계 비만입니다.")
elif 30<= BMI <35:
    print(f"당신의 BMI는 {BMI}kg/㎡ 2단계 비만입니다.")
else:
    print(f"당신의 BMI는 {BMI}kg/㎡ 3단계 비만입니다.")
print("-"*30)
x=int(input("x좌표를 입력하세요"))
y=int(input("y좌표를 입력하세요"))
if x>0 and y>0:
    print(f"좌표 ({x}, {y})는 1사분면에 있습니다.")
elif x<0 and y>0:
    print(f"좌표 ({x}, {y})는 2사분면에 있습니다.")
elif x<0 and y<0:
    print(f"좌표 ({x}, {y})는 3사분면에 있습니다.")
elif x>0 and y<0:
    print(f"좌표 ({x}, {y})는 4사분면에 있습니다.")
else:
    print(f"좌표 ({x}, {y})는 사분면에 속해있지 않습니다.")
print("-"*30)
import math
r=int(input("반지름(cm)을 입력하세요"))
area=r**2*math.pi
circumference=2*math.pi*r
print("원의 면적은 {:.2f}cm 입니다.".format(area))
print("원의 둘레는 {:.1f}cm 입니다.".format(circumference))