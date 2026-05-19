import requests
import os

def read_weather_col(filename, col_idx=9, conv_fn=float):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(conv_fn(tokens[col_idx]))
    return dataset

def main():
    year = 2023
    url= f"https://api.taegon.kr/stations/146/?sy={year}&ey={year}&format=csv"
    filename = f"weather_{year}.csv"

    if not os.path.exists(filename):
        resp = requests.get(url)
        with open(filename, "w") as fout:
            fout.write(resp.text)
    else:
        print(f"이미 {filename}이 있습니다.")

    tavg = read_weather_col(filename, 4)
    t_avg = sum(tavg) / len(tavg)
    with open("weather_2023.csv.result2.txt", "w", encoding="UTF-8-sig") as f_out:
        f_out.write(f"연 평균 기온은 {t_avg:.1f}℃입니다.\n")

if __name__=="__main__":
    main()