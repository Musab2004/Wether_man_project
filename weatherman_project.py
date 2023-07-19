import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os
import pandas as pd
import sys
import re
import math

first_col_name = "Time_Zone"


def check_format_scenario_2_3(user_input):
    pattern = r"^\d{4}/\d{1,2}$"
    try:
        if re.match(pattern, user_input):
            year, month = user_input.split("/")
            if 1 <= int(month) <= 12:
                return str(user_input)
            else:
                raise ValueError("Invalid month value.")
        else:
            raise ValueError("Invalid date format.")
    except ValueError as e:
        print("Error:", str(e))

        print(f"Invalid Input.")
        sys.exit()


def check_format_scenario_1(user_input):
    pattern = r"^\d{4}$"
    try:
        if re.match(pattern, user_input):
            return str(user_input)
        else:
            raise ValueError("Invalid input.")
    except ValueError as e:
        print(str(e))
        sys.exit()


def openfolder(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")
        else:
            text_files = glob.glob(directory + "*.txt")

        i = 0
        for file_path in text_files:
            with open(file_path, "r") as file:
                data_frame = pd.read_csv(file_path)
                data_frame.rename(
                    columns={data_frame.columns[0]: "Time_Zone"}, inplace=True
                )
                if i == 0:
                    appended_data_frame = data_frame
                else:
                    appended_data_frame = pd.concat(
                        [appended_data_frame, data_frame], ignore_index=True
                    )
                i = i + 1

        return appended_data_frame

    except FileNotFoundError as e:
        print(str(e))
        sys.exit()

    except Exception as e:
        print("An error occurred:", "Wrong directory")
        sys.exit()


def openfile(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")

        data_frame = pd.read_csv(directory)
        data_frame.rename(columns={data_frame.columns[0]: "Time_Zone"}, inplace=True)

        return data_frame

    except FileNotFoundError as e:
        print(str(e))
        sys.exit()

    except Exception as e:
        print("An error occurred:", "Wrong Directory")
        sys.exit()


def check_choice(user_input):
    try:
        if user_input.isdigit() and len(user_input) == 1:
            if "1" <= user_input <= "3":
                return int(user_input)
            else:
                raise ValueError("Invalid input.")
        else:
            raise ValueError("Invalid input.")
    except ValueError as e:
        print(str(e))
        sys.exit()


def filter_data_frame(appended_df, user_input):
    appended_df[first_col_name].fillna("", inplace=True)
    appended_df.columns = [c.replace(" ", "_") for c in appended_df.columns]

    mask = appended_df[first_col_name].str.contains(user_input)
    at_least_one_true = mask.any()
    if not at_least_one_true:
        print("Year or month doesn't exist in the data ")
        sys.exit()

    filtered_df = appended_df[mask]
    return filtered_df


def extreme_weather_report_in_year(filtered_df):
    months_dict = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec",
    }

    highest_row_max_temp = filtered_df.loc[filtered_df["Max_TemperatureC"].idxmax()]
    try:
        year, month, day = highest_row_max_temp[first_col_name].split("-")

    except ValueError:
        print("Error: Invalid date format.")

    try:
        print(
            "Highest: ",
            highest_row_max_temp["Max_TemperatureC"],
            "C ",
            "On ",
            months_dict[int(month)],
            day,
        )
    except KeyError as e:
        print("Error: Missing key in the 'highest_row' dictionary.")
    except ValueError as e:
        print("Error: Invalid month value.")
    highest_row_min_temp = filtered_df.loc[filtered_df["Min_TemperatureC"].idxmin()]
    try:
        year, month, day = highest_row_min_temp[first_col_name].split("-")

    except ValueError:
        print("Error: Invalid date format.")
    try:
        print(
            "Lowest: ",
            highest_row_min_temp["Min_TemperatureC"],
            "C ",
            "On ",
            months_dict[int(month)],
            day,
        )
    except KeyError as e:
        print("Error: Missing key in the 'highest_row_min_temp' dictionary.")
    except ValueError as e:
        print("Error: Invalid month value.")

    highest_row_max_humid = filtered_df.loc[filtered_df["Max_Humidity"].idxmax()]

    # year, month, day = highest_row[first_col_name].split("-")
    try:
        year, month, day = highest_row_max_humid[first_col_name].split("-")

    except ValueError:
        print("Error: Invalid date format.")

    try:
        print(
            "Humid: ",
            highest_row_max_humid["Max_Humidity"],
            "% ",
            "On ",
            months_dict[int(month)],
            day,
        )
    except KeyError as e:
        print("Error: Missing key in the 'highest_row_max_humid' dictionary.")
    except ValueError as e:
        print("Error: Invalid month value.")


def average_weather_report_in_month(filtered_df):
    max_temp_mean = filtered_df["Max_TemperatureC"].mean()
    print("Max temp:", max_temp_mean, "C")
    min_temp_mean = filtered_df["Min_TemperatureC"].mean()
    print("Min Temp mean :", min_temp_mean, "C")

    humidity = filtered_df["Max_Humidity"].mean()
    print("Humidity Mean: ", humidity, "%")


def bar_graph_weather_report(filtered_df):
    time_zone = filtered_df[first_col_name]
    max_temprature = filtered_df["Max_TemperatureC"]
    min_temprature = filtered_df["Min_TemperatureC"]
    color_red = "\033[91m"
    color_blue = "\033[94m"
    color_reset = "\033[0m"
    for i in range(0, len(time_zone)):
        print(color_reset + time_zone[i], end="     ")

        if math.isnan(max_temprature[i]):
            pass
        else:
            for j in range(0, int(max_temprature[i])):
                print(color_red + "+", end="")
            print("   ", color_red + str(max_temprature[i]), "C", end=" ")
        print()
        print(color_reset + time_zone[i], end="     ")
        if math.isnan(max_temprature[i]):
            # print()
            pass
        else:
            for j in range(0, int(min_temprature[i])):
                print(color_blue + "+", end="")
            print("   ", color_blue + str(min_temprature[i]), "C", end=" ")
        print()


num_args = len(sys.argv) - 1
if num_args != 3:
    raise ValueError("Invalid input format")


user_input = sys.argv[2]
directory = sys.argv[3]
choice = str(sys.argv[1])

try:
    if choice == "-a":
        check_format_scenario_1(user_input)
        data_frame = openfolder(directory)

        data_frame = filter_data_frame(data_frame, user_input)

        extreme_weather_report_in_year(data_frame)

    elif choice == "-e":
        check_format_scenario_2_3(user_input)
        user_input = user_input.replace("/", "-")

        data_frame = openfile(directory)

        data_frame = filter_data_frame(data_frame, user_input)

        average_weather_report_in_month(data_frame)

    elif choice == "-c":
        check_format_scenario_2_3(user_input)
        user_input = user_input.replace("/", "-")
        data_frame = openfile(directory)
        data_frame = filter_data_frame(data_frame, user_input)
        bar_graph_weather_report(data_frame)

    else:
        raise ValueError("Wrong flag")

except ValueError as e:
    print(str(e))

except Exception as e:
    print("An error occurred:", str(e))
