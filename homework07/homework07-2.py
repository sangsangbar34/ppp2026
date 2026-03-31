mart = {"우유": 2800, "계란": 300, "빵": 1200, "물": 1700}
cart=["물","물","계란","빵","빵", "빵", "우유"]
total=0
for i in cart:
    total+=mart[i]
print(f"총 금액은 {total:,}원 입니다.")