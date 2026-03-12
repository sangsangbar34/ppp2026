# temp_c=input("온도를 입력하세요")
# temp_c=int(temp_c)
#2줄
# temp_c=int(input("온도를 입력하세요"))
# temp_f=(temp_c*9/5)+32
# print(f"{temp_c}℃ => {temp_f}F")
#3줄
# w=float(input("몸무게를 입력하세요"))
# h=float(input("키를 입력하세요"))
# BMI= f"{w / (h * h)}"
# print(BMI)
#int는 문자를 정수로 바꿔주는 도구
#float는 문자를(소수점까지) 숫자로 바꿔주는 도구
# w=(input("몸무게를 입력하세요"))
# h=(input("키를 입력하세요"))
# BMI= f"{float(w) / (float(h) * float(h))}"
# print(BMI)
import math
r=int(input("반지름을 입력하세요"))
O=f"{r**2*math.pi}"
print(O)