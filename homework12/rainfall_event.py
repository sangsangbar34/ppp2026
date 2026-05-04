def read_weather_col(weather_filename, col_idx):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[col_idx]))
    return dataset

def get_rain(rainfall):
    dataset_rainfall=[]
    for r in rainfall:
        if r>=0.1:
            dataset_rainfall.append(1)
        else:
            dataset_rainfall.append(0)

    dataset_rain_event = []
    for i in range(len(dataset_rainfall)):
        r = dataset_rainfall[i]
        if r==0:
            dataset_rain_event.append(0)
        else:
            if i ==0:
                dataset_rain_event.append(1)
            else:
                dataset_rain_event.append(dataset_rain_event[i-1]+1)
    return max(dataset_rain_event)


def get_max_rainfall_event(rainfall):
    dataset= []
    rainfall_event= None
    for r in rainfall:
        if r > 0:
            if rainfall_event != None:
                rainfall_event.append(r)
            else:
                rainfall_event = [r]

        else:
            if rainfall_event != None:
                dataset.append(rainfall_event)
            rainfall_event = None
    max_total=0
    for event in dataset:
        event_sum=sum(event)
        if event_sum > max_total:
            max_total=event_sum
    return max_total


def get_top3(list_values):
    return sorted(list_values)[-3:]

def main():
    weather_filename = "../homework12/weather(146)_2022.csv"
    rainfall = read_weather_col(weather_filename, 9)

    maximum_rain=get_rain(rainfall)
    print(f"최장 연속 강우일수는 {maximum_rain}입니다.")

    max_rainfall_event= get_max_rainfall_event(rainfall)
    print(f"강우 중 최대 강수량은 {max_rainfall_event}입니다.")

    tmax= read_weather_col(weather_filename, 3)
    tmax_top3=get_top3(tmax)
    print(f"tmax 최댓값 3개는 {tmax_top3}입니다.")

if __name__=="__main__":
    main()