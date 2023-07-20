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
first_col_name = "Time_Zone"

month_dict = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12
    }




def check_date_format(user_input):
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


def check_date_month_format(user_input):
    pattern = r"^\d{4}$"
    try:
        if re.match(pattern, user_input):
            return str(user_input)
        else:
            raise ValueError("Invalid input.")
    except ValueError as e:
        print(str(e))
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




def check_input(date_string,file_path):
    


    match = re.search(r"(\d{4})_(\w+)\.txt", file_path)

    if match:
        year = int(match.group(1))
        month_name = match.group(2)
       
        if month_name in month_dict:
            month = month_dict[month_name]
            # Extract month and year from the date string
            date_parts = date_string.split("/")
            comparison_year = int(date_parts[0])
            comparison_month = int(date_parts[1])

            # Compare month and year
            if year == comparison_year and month == comparison_month:
                pass
            else:
                print("File path and Date given do not match")
                sys.exit()
        else:
            print("Invalid month name")
    else:
        print("No match found")



