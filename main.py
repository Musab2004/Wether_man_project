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
import  check_functions,open_directory,filter_data_frame,Weather_Reports 


num_args = len(sys.argv) - 1
if num_args != 3:
    raise ValueError("Invalid input format")
user_input = sys.argv[2]
directory = sys.argv[3]
choice = str(sys.argv[1])

try:
    if choice == "-a":
        check_functions.check_date_month_format(user_input)
        data_frame = open_directory.open_folder(directory)  
        data_frame = filter_data_frame.filter_data_frame(data_frame, user_input)

        Weather_Reports.extreme_weather_report_in_year(data_frame)

    elif choice == "-e":
        check_functions.check_input(user_input,directory)
        check_functions.check_date_format(user_input)
        user_input = user_input.replace("/", "-")

        data_frame = open_directory.open_file(directory)

        data_frame = filter_data_frame.filter_data_frame(data_frame, user_input)

        Weather_Reports.average_weather_report_in_month(data_frame)

    elif choice == "-c":
        check_functions.check_input(user_input,directory)
        check_functions.check_date_format(user_input)
        
        user_input = user_input.replace("/", "-")
        data_frame = open_directory.open_file(directory)
        data_frame = filter_data_frame.filter_data_frame(data_frame, user_input)
        Weather_Reports.bar_graph_weather_report(data_frame)

    else:
        raise ValueError("Wrong flag")

except ValueError as e:
    print(str(e))

except Exception as e:
    print("An error occurred:", str(e))
