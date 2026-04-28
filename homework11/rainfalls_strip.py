def read_rainfalls(weather_filename):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))
    return dataset

def read_t_avg(weather_filename):
    dataset_2 = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset_2.append(float(tokens[4]))
    return dataset_2

def read_five_rainfalls(weather_filename):
    dataset_3 = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            five_rain = float(tokens[9])
            if five_rain >= 5.0:
                dataset_3.append(five_rain)
    return dataset_3

def main():
    weather_filename = "weather(146)_2022.csv"

    t_avg= read_t_avg(weather_filename)
    print(f"연 평균 기온은 {sum(t_avg)/len(t_avg):.1f}℃입니다.")

    rainfalls = read_rainfalls(weather_filename)
    print(f"총 강수량은 {sum(rainfalls):.1f}mm입니다.")

    five_rainfalls = read_five_rainfalls(weather_filename)
    print(f"5mm이상 강수 일수는 {len(five_rainfalls)}일입니다.")

if __name__=="__main__":
    main()