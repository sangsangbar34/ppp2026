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

def get_maximum_temp_gap(dates, tmax, tmin, selected_years):
    max_diff = -999
    max_diff_data =None
    for date,tx,tn in zip(dates,tmax,tmin):
        if date[0]==selected_years:
            diff = tx - tn
            if diff > max_diff:
                max_diff = diff
                max_diff_data = date
    return max_diff_data, max_diff

def main():
    weather_filename = "../homework14/weather(146)_2001-2022.csv"
    dates = read_dates(weather_filename)
    tmax = read_weather_col(weather_filename, 3)
    tmin = read_weather_col(weather_filename, 5)

    for y in range(2001, 2023):
        date, temp_diff = get_maximum_temp_gap(dates, tmax, tmin, y)
        print(f"{y}년 최대일교차가 발생한 날: {date}, 일교차: {temp_diff:.1f}")

if __name__=="__main__":
    main()