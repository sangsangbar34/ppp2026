import matplotlib.pyplot as plt
import pandas as pd
import koreanize_matplotlib

def main():
    df = pd.read_csv('weather_jeonju_1980-2024.csv')
    # df_year_temp = df.groupby("year")[" tavg"].reset_index()
    # df_birthday = df[df[' month'] == 9] and df[df['day'] == 18]
    df_birthday = df[(df[' month'] == 9) & (df[' day'] == 18)]

    year = df_birthday['year'].astype(str)
    temp =df_birthday[' tavg']
    # month = df_year_temp[df_year_temp[' month'] == 9]
    # day = df_year_temp[df_year_temp[' day'] == 18]
    fig, ax = plt.subplots(figsize=(20, 6))
    ax.plot(year, temp, color="r", label="생일 평균 기온")

    ax.set_ylabel("기온(℃)")
    ax.set_xlabel("연도")
    ax.legend()
    plt.xticks(rotation=45)

    fig.savefig("line_birthday.png")
    plt.show()

    # birthday_2006 = df_birthday[df_birthday['year'] == 2006][' tavg'].values[0]
    # print(f" 2006년은 {birthday_2006:.1f}℃로 40번째로 높았습니다 ")
    # birthday_2006 = df_birthday[df_birthday['year'] == 2006][' tavg']
    # max_temp_0918 = df_birthday['year'][' tavg'].max().values[0]
    # df_sorted = df.sort_values(df[' tavg'], ascending= True)
    df_sorted = df_birthday.sort_values(by=' tavg', ascending=False)

    max_year = df_sorted['year'].values[0]
    max_temp = df_sorted[' tavg'].values[0]
    print(f"역대 9월 18일 중 가장 기온이 높았던 해는 {max_year}년으로, {max_temp:.1f}℃였습니다")

    min_year = df_sorted['year'].values[44]
    min_temp = df_sorted[' tavg'].values[44]
    print(f"역대 9월 18일 중 가장 기온이 낮았던 해는 {min_year}년으로, {min_temp:.1f}℃였습니다")

    year_list = list(df_sorted['year'])
    rank = year_list.index(2006) + 1
    max_temp = df_sorted[df_sorted['year'] == 2006][' tavg'].values[0]
    print(f"2006년 9월 18일은 역대 9월 18일 중 {rank}번째로 더웠으며, 기온은 {max_temp:.1f}℃였습니다")

if __name__ == "__main__":main()