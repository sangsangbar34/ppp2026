import random

def get_lotto():
    a = random.randint(1,45)
    b = random.randint(1,45)
    c = random.randint(1, 45)
    d = random.randint(1, 45)
    e = random.randint(1, 45)
    f = random.randint(1, 45)
    num_list=[a, b, c, d, e, f]
    return num_list

def main():
    x =int(input("몇 번 추출할까요?"))
    for i in range(x):
        print(get_lotto())
if __name__=="__main__":
    main()
