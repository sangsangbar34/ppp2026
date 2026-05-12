def read_weather_col(weather_filename, col_idx=9, conv_fn=float):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(conv_fn(tokens[col_idx]))
    return dataset

def read_dates(weather_filename):
    dates = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            date = [int(tokens[0]), int(tokens[1]), int(tokens[2])]
            dates.append(date)
    return dates

def gdd_season(dates, tavg, selected_years):
    gdd_value = 0
    for date,t in zip(dates, tavg):
        if date[1] in [5,6,7,8,9] and date[0]==selected_years:
            if t > 5:
                gdd_value += (t-5)
    return gdd_value

def main():
    weather_filename = "../homework14/weather(146)_2001-2022.csv"
    dates = read_dates(weather_filename)
    tavg = read_weather_col(weather_filename, 4)

    for y in range(2001, 2023):
        gdd_value = gdd_season(dates, tavg, y)
        print(f"{y}년 5~9월 생육도일은 {gdd_value:.1f}입니다.")

if __name__=="__main__":
    main()