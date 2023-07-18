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


def check_format_Scenario_2_3(user_input):
    pattern = r"^\d{4}/\d{1,2}$"

    if re.match(pattern, user_input):
        year, month = user_input.split("/")
        if int(month) <= 12 and int(month) >= 1:
       
            return str(user_input)

    print(f"Invalid Input.")
    sys.exit()


def check_format_Scenario_1(user_input):
    pattern = r"^\d{4}$"

    if re.match(pattern, user_input):
        return str(user_input)

    print(f"Invalid input.")
    sys.exit()


def openfolder(directory):
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        sys.exit()
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
                appended_df = data_frame

            else:
                appended_df = pd.concat([appended_df, data_frame], ignore_index=True)
            i = i + 1
    return appended_df


def openfile(directory):
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        sys.exit()
    else:
        data_frame = pd.read_csv(directory)
        data_frame.rename(columns={data_frame.columns[0]: "Time_Zone"}, inplace=True)
    return data_frame


def check_choice(user_input):
    if user_input.isdigit() and len(user_input) == 1:
        if user_input >= "1" and user_input <= "3":
            return int(user_input)

    print("Invalid input.")
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


def Extreme_Weather_Report_in_a_year(filtered_df):
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

    highest_row = filtered_df.loc[filtered_df["Max_TemperatureC"].idxmax()]
    year, month, day = highest_row[first_col_name].split("-")
    print(
        "Highest : ",
        highest_row["Max_TemperatureC"],
        "C ",
        "On ",
        months_dict[int(month)],
        day,
    )
    highest_row = filtered_df.loc[filtered_df["Min_TemperatureC"].idxmin()]
    year, month, day = highest_row[first_col_name].split("-")
    print(
        "Lowest : ",
        highest_row["Min_TemperatureC"],
        "C ",
        "On ",
        months_dict[int(month)],
        day,
    )

    highest_row = filtered_df.loc[filtered_df["Max_Humidity"].idxmax()]
    year, month, day = highest_row[first_col_name].split("-")

    print(
        "Humid : ",
        highest_row["Max_Humidity"],
        "% ",
        "On ",
        months_dict[int(month)],
        day,
    )


def Average_Weathre_Report_in_a_month(filtered_df):
    Max_temp_mean = filtered_df["Max_TemperatureC"].mean()
    print("Max temp:", Max_temp_mean, "C")
    Min_temp_mean = filtered_df["Min_TemperatureC"].mean()
    print("Min Temp mean :", Min_temp_mean, "C")

    humidity = filtered_df["Max_Humidity"].mean()
    print("Humidity Mean: ", humidity, "%")


def Bar_Graph_Weather_Report(filtered_df):
    GST = filtered_df[first_col_name]
    Max_Temprature = filtered_df["Max_TemperatureC"]
    Min_Temprature = filtered_df["Min_TemperatureC"]
    color_red = "\033[91m"
    color_blue = "\033[94m"
    color_reset = "\033[0m"
    for i in range(0, len(GST)):
        print(color_reset + GST[i], end="     ")
  
        if math.isnan(Max_Temprature[i]):
       
            pass
        else:
            for j in range(0, int(Max_Temprature[i])):
                print(color_red + "+", end="")
            print("   ", color_red + str(Max_Temprature[i]), "C", end=" ")
        print()
        print(color_reset + GST[i], end="     ")
        if math.isnan(Max_Temprature[i]):
            # print()
            pass
        else:
            for j in range(0, int(Min_Temprature[i])):
                print(color_blue + "+", end="")
            print("   ", color_blue + str(Min_Temprature[i]), "C", end=" ")
        print()





user_input = sys.argv[2]

directory = sys.argv[3]
choice = str(sys.argv[1])

num_args = len(sys.argv) - 1
if num_args !=3:
    print("invalid input format")
    sys.exit()


if choice == "-a":
    check_format_Scenario_1(user_input)
    df = openfolder(directory)

    df = filter_data_frame(df, user_input)

    Extreme_Weather_Report_in_a_year(df)

elif choice == "-e":
    check_format_Scenario_2_3(user_input)
    user_input = user_input.replace("/", "-")

    df = openfile(directory)

    df = filter_data_frame(df, user_input)

    Average_Weathre_Report_in_a_month(df)
elif choice == "-c":
    check_format_Scenario_2_3(user_input)
    user_input = user_input.replace("/", "-")
    df = openfile(directory)
    df = filter_data_frame(df, user_input)
    Bar_Graph_Weather_Report(df)
else:
    print("Wrong flag")

print()
