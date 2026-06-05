import matplotlib.pyplot as plt
import pandas as pd
import koreanize_matplotlib

def main():
    df_jj = pd.read_csv('weather_jeonju_1980-2024.csv')
    df_sw = pd.read_csv('weather_suwon_1980-2024.csv')
    fig, ax = plt.subplots(figsize=(20, 6))

    # df_jj_year_temp = df_jj.groupby("year")[" tavg"].sum().reset_index()
    # df_sw_year_temp = df_sw.groupby("year")[" tavg"].sum().reset_index()
    # df_jj_year_temp = df_jj.groupby("year")[" tavg"].sum()/len().reset_index()
    df_jj_year_temp = df_jj.groupby("year")[" tavg"].mean().reset_index()
    df_sw_year_temp = df_sw.groupby("year")[" tavg"].mean().reset_index()

    year_jj = df_jj_year_temp['year'].astype(str)
    avg_jj =df_jj_year_temp[' tavg']
    year_sw = df_sw_year_temp['year'].astype(str)
    avg_sw = df_sw_year_temp[' tavg']

    ax.plot(year_jj, avg_jj, color="r", label="전주 연평균 기온")
    ax.plot(year_sw,avg_sw, color="b", label="수원 연평균 기온")

    ax.set_ylabel("기온(℃)")
    ax.set_xlabel("연도")
    ax.legend()
    plt.xticks(rotation=45)
    fig.savefig("line_temp.png")
    plt.show()

if __name__ == "__main__":main()