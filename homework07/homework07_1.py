cal_dict={"한라봉":50, "딸기":34, "바나나":77, "사과":60, "배":55}
eat_dict={"한라봉":100,"딸기":200,"바나나":500}

total_cal = 0
for key,val in eat_dict.items():
    total_cal += val * cal_dict[key]
print(f"총 칼로리는 {total_cal}kcal 입니다.")
