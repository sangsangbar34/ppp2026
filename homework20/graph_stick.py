import matplotlib.pyplot as plt
import pandas as pd
import koreanize_matplotlib

def main():
    df = pd.read_csv('weather_jeonju_1980-2024.csv')
    # print(df.columns)
    # fig, ax = plt.subplots(figsize=(15, 6))
    fig, ax = plt.subplots(figsize=(20, 6))

    # year = df["year"].astype(str)
    # rain = df[" rainfall"]
    # rain = f"{df[" rainfall"].sum():.1f}"
    # df_year_rain = f"{df.groupby("year")[" rainfall"].sum().reset_index():.1f}"
    df_year_rain = df.groupby("year")[" rainfall"].sum().reset_index()

    year = df_year_rain["year"].astype(str)
    rain = df_year_rain[" rainfall"]

    ax.bar(year, rain, color="b")
    ax.set_ylabel("연평균강우량(mm)")
    ax.set_xlabel("연도")

    fig.savefig("stick_rain.png")
    plt.xticks(rotation=45)
    plt.show()



if __name__ == "__main__":
    main()