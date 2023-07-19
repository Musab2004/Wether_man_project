import os
from datetime import datetime

# First date
date1 = "2006/8"

# Second date (assuming it's a file path)
file_path = "/home/musab/Downloads/Weather_man_project/lahore_weather/lahore_weather_2006_Aug.txt"

# Extract month and year from the file name
file_name = os.path.basename(file_path)
name_components = file_name.split("_")
date2 = name_components[-1].split(".")[0]

# Convert dates to datetime objects
date1_obj = datetime.strptime(date1, "%Y/%m")
date2_obj = datetime.strptime(date2, "%Y_%b")

# Compare month and year components
if date1_obj.month != date2_obj.month or date1_obj.year != date2_obj.year:
    print("The two dates are different in terms of month and year.")
else:
    print("The two dates are the same in terms of month and year.")