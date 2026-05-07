def read_weather_col(weather_filename, col_idx=9, conv_fn=float):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(conv_fn(tokens[col_idx]))
    return dataset

def sumifs(rainfall, months, selected_month=[6, 7, 8]):
    selected_rain = []
    for m, r in zip(months, rainfall):
        if m in selected_month:
            selected_rain.append(r)
    return sum(selected_rain)

def main():
    weather_filename = "../homework13/weather(146)_2022.csv"
    rainfall = read_weather_col(weather_filename)
    months = read_weather_col(weather_filename, 1, int)

    summer_rainfall = sumifs(rainfall, months)
    print(f"여름철(6-8월) 총 강수량은 {summer_rainfall:.1f}mm입니다.")

if __name__=="__main__":
    main()