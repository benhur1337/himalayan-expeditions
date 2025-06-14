import sys
import pandas
import matplotlib.pyplot as plt
from pandas import DataFrame


# Goals:
# 1. Which season has the highest success rate? pie chart
# 2. Is there a correlation between total members and success rate? scatterplot
# 3. Which routes have favorable success/mortality rates?

def total_seasonal_success(df:DataFrame) -> int:
    total = 0

    for x in range(1,5):
        success = df[f"success{x}"] == True
        total += success.shape[0]


    return total

def respective_season_df(df:DataFrame, season:str) -> DataFrame:
    result = df.loc[df['season'] == season]
    return result


def calculate_seasonal_success(file:DataFrame) -> str:

    print("Seasons Success Rate")

    # filter out a data frame for the seasons and success of each route

    seasons_df = file[["season", "success1", "success2", "success3", "success4"]]

    summer_df = respective_season_df(seasons_df, "Summer")
    spring_df = respective_season_df(seasons_df, "Spring")
    autumn_df = respective_season_df(seasons_df, "Autumn")
    winter_df = respective_season_df(seasons_df, "Winter")

    data = {
        "seasons" : ["summer", "spring", "autumn", "winter"],
        "values" : [total_seasonal_success(summer_df), total_seasonal_success(spring_df), total_seasonal_success(autumn_df), total_seasonal_success(winter_df)]
    }

    graph_df = pandas.DataFrame(data)

    graph_df.plot.pie(y="values", labels = graph_df["seasons"], autopct = "%1.1f%%", title="Pie Chart")

    plt.show()
    # keep score of each successful ascent for each season with respective route

    return ""


def get_popular_routes(file: DataFrame, route: str) -> str:
    """Function returning popular routes"""

    column_count = file[route].value_counts()
    most_common_route = file[route].value_counts().idxmax()
    return f"{most_common_route} ({column_count[most_common_route]} records)"



def main() -> int:
    """Program's Entry Point"""

    user_input = input("Enter csv_name: ")

    try:

        file = pandas.read_csv(user_input)
        print(file)

        r,c = file.shape

        print(f"total records found: {r}")

        for x in range(1, 5):
            print(f"route {x}: " + get_popular_routes(file, f"route{x}"))

        print(calculate_seasonal_success(file))

        return 0

    except Exception as error:

        print(f"An error has occured: {error}")

    return 1


if __name__ == "__main__":
    sys.exit(main())
