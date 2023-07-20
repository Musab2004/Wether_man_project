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



def open_folder(directory):
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


def open_file(directory):
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
