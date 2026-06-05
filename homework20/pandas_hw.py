import requests
import os
import pandas as pd

def read_weather_col(filename, col_idx=9, conv_fn=float):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(conv_fn(tokens[col_idx]))
    return dataset

def download_weather(weather_filename, area, sy, ey):
    url = f"https://api.taegon.kr/stations/{area}/?sy={sy}&ey={ey}&format=csv"

    if not os.path.exists(weather_filename):
        resp = requests.get(url)
        with open(weather_filename, "w") as fout:
            fout.write(resp.text)
    else:
        print(f"이미 {weather_filename}이 있습니다.")

def main():
    filename = f"weather_jeonju_1980-2024.csv"
    filename_sw = f"weather_suwon_1980-2024.csv"
    download_weather(filename, 146, 1980, 2024)
    download_weather(filename_sw, 119, 1980, 2024)

    df = pd.read_csv(filename, skipinitialspace=True)

    print(f'{df[df["year"] == 2012]["rainfall"].sum():.1f}')
    print(f'{df[df["year"] == 2024]["tmax"].max():.1f}')

    df["tdiff"] = df["tmax"] - df["tmin"]
    print(f'{df[df["year"] == 2020]["tdiff"].max():.1f}')

    df_sw = pd.read_csv(filename_sw, skipinitialspace=True)
    prec_jj = df[df["year"] == 2019]["rainfall"].sum()
    prec_sw = df_sw[df_sw["year"] == 2019]["rainfall"].sum()
    print(f'{abs(prec_jj - prec_sw):.1f}')

if __name__=="__main__":
    main()
