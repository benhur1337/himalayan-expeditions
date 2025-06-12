import sys
import pandas
from pandas import DataFrame


# Goals:
# 1. Does season or route impact the success rate of an expedition?
# 2. Is there a correlation between total members, oxygen used, and success rate?
# 3. Routes with favorable success/mortality rates


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

        for x in range(1, 5):
            print(f"route {x}: " + get_popular_routes(file, f"route{x}"))

        return 0

    except Exception as error:

        print(f"An error has occured: {error}")

    return 1


if __name__ == "__main__":
    sys.exit(main())
