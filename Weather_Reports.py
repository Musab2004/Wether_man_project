import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os
import pandas as pd
import sys
import re
import math
from datetime import datetime

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
first_col_name = "Time_Zone"

def extreme_weather_report_in_year(filtered_data_frame):


    highest_row_max_temp = filtered_data_frame.loc[filtered_data_frame["Max_TemperatureC"].idxmax()]
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
    highest_row_min_temp = filtered_data_frame.loc[filtered_data_frame["Min_TemperatureC"].idxmin()]
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

    highest_row_max_humid = filtered_data_frame.loc[filtered_data_frame["Max_Humidity"].idxmax()]

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
            pass
        else:
            for j in range(0, int(min_temprature[i])):
                print(color_blue + "+", end="")
            print("   ", color_blue + str(min_temprature[i]), "C", end=" ")
        print()