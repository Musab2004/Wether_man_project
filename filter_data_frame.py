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

def filter_data_frame(appended_data_frame, user_input):
    appended_data_frame[first_col_name].fillna("", inplace=True)
    appended_data_frame.columns = [c.replace(" ", "_") for c in appended_data_frame.columns]

    mask = appended_data_frame[first_col_name].str.contains(user_input)
    at_least_one_true = mask.any()
    if not at_least_one_true:
        print("Year or month doesn't exist in the data ")
        sys.exit()

    filtered_df = appended_data_frame[mask]
    return filtered_df

