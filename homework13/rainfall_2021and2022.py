def read_weather_col(weather_filename, col_idx=9, conv_fn=float):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(conv_fn(tokens[col_idx]))
    return dataset

def sumifs(rainfall, years, selected_years):
    selected_rain = []
    for m, r in zip(years, rainfall):
        if m in selected_years:
            selected_rain.append(r)
    return sum(selected_rain)

def main():
    weather_filename = "../homework13/weather(146)_2001-2022.csv"
    rainfall = read_weather_col(weather_filename)
    years = read_weather_col(weather_filename, 0, int)

    for y in range(2021, 2023):
        rainfall_y = sumifs(rainfall, years, [y])
        print(f"{y}년 강수량은 {rainfall_y:.1f}mm입니다.")

if __name__=="__main__":
    main()