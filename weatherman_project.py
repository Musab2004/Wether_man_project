#!/usr/bin/env python
# coding: utf-8

# In[132]:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import os
import pandas as pd
import sys
import re




def check_format_2(user_input):
    pattern = r'^\d{4}/\d{1,2}$'
     
    if re.match(pattern, user_input):
       year, month = user_input.split('/')
       if int(month)<=12 and int(month)>=1:
            # print("here",month)
            return str(user_input)
        
    print(f"Invalid Input.")
    sys.exit()




def check_format_1(user_input):
    pattern = r'^\d{4}$'

    if re.match(pattern, user_input):
          
            return str(user_input)
        
    print(f"Invalid input.")
    sys.exit()


def openfolder(directory):
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        sys.exit()
    else:
        # Use glob to get the list of text files
        # print("now here")
        print(directory)
        # base_name = os.path.basename(directory)
        # print(base_name)
        if "Dubai" in directory:
           first_col_name='GST'          
        elif "lahore" or "Murree" in directory:
            first_col_name='PKT'
        text_files = glob.glob(directory + '*.txt')


    i=0
    for file_path in text_files:
        with open(file_path, 'r') as file:
            data_frame = pd.read_csv(file_path)
            if i==0:
             appended_df = data_frame
            
            else:
             appended_df= pd.concat([appended_df, data_frame], ignore_index=True)   
            i=i+1
    return appended_df,first_col_name


def openfile(directory):
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        sys.exit()
    else:
        base_name = os.path.basename(directory)
       
        if "Dubai" in base_name:
           first_col_name='GST'

        elif "lahore" or "Murree" in base_name:
            first_col_name='PKT'
        text_files = glob.glob(directory + '*.txt')
        # Use glob to get the list of text files
        data_frame = pd.read_csv(directory)
    return data_frame,first_col_name        
# numeric_value = get_fixed_length_numeric_input(6)




def check_choice(user_input):
    if user_input.isdigit() and len(user_input) == 1:
        if user_input >= "1" and user_input <= "3":
            return int(user_input)

    print("Invalid input.")
    sys.exit()

def filter_dataframe(appended_df,user_input,first_col_name):
    appended_df[first_col_name].fillna("",inplace=True)
    appended_df.columns = [c.replace(' ', '_') for c in appended_df.columns]


    mask = appended_df[first_col_name].str.contains(user_input)
    at_least_one_true = mask.any()
    # print(at_least_one_true)
    # filtered_df = appended_df[mask]
    # print(filtered_df)
    # all_false = mask.all()
    # print(mask)
    if not at_least_one_true:
        print("Year or month doesn't exist in the data ")
        sys.exit()
        


    filtered_df = appended_df[mask]
    return filtered_df



def case1(filtered_df,first_col_name):
    months_dict = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
}
    
    highest_row = filtered_df.loc[filtered_df['Max_TemperatureC'].idxmax()]
    year,month,day=highest_row[first_col_name].split('-')
    print("Date : ",months_dict[int(month)],day,"Highest : ",highest_row['Max_TemperatureC'])
    highest_row = filtered_df.loc[filtered_df['Min_TemperatureC'].idxmin()]
    year,month,day=highest_row[first_col_name].split('-')
    print("Date : ",months_dict[int(month)],day,"Lowest : ",highest_row['Min_TemperatureC'])

    highest_row = filtered_df.loc[filtered_df['Max_Humidity'].idxmax()]
    year,month,day=highest_row[first_col_name].split('-')
    
    print("Date : ",months_dict[int(month)],day,"Humid : ",highest_row['Max_Humidity'])




def case2(filtered_df,first_col_name):
    Max_temp_mean = filtered_df['Max_TemperatureC'].mean()
    print("Max temp:",Max_temp_mean)
    Min_temp_mean = filtered_df['Min_TemperatureC'].mean()
    print("Min Temp mean :",Min_temp_mean)


    humidity = filtered_df['Max_Humidity'].mean()
    print("Humidity Mean: ",humidity)




def case3(filtered_df,first_col_name):
        GST = filtered_df[first_col_name]
        Max_Temprature = filtered_df['Max_TemperatureC']
        Min_Temprature = filtered_df['Min_TemperatureC']

        # Set the height of the bars
        bar_height = 0.35

        # Set the positions of the bars on the y-axis
        y = np.arange(len(GST))

        # Create the horizontal bar plot for Max Temperature
        plt.barh(y, Max_Temprature, height=bar_height, label='Max Temperature')

        # Shift the positions of the bars for Min Temperature
        y = y + bar_height

        # Create the horizontal bar plot for Min Temperature
        plt.barh(y, Min_Temprature, height=bar_height, label='Min Temperature')

        # Set the labels and title
        plt.ylabel('GST')
        plt.xlabel('Max and Min Temperatures')
        plt.title('Horizontal Bar Plot of Max and Min Temperatures')

        plt.yticks(y - bar_height / 2, GST)

        # Add a legend
        plt.legend()

        # Display the plot
        plt.show()


# Main        
user_input=sys.argv[1]

directory=sys.argv[2]
choice = str(sys.argv[3])
choice = check_choice(choice)

# print(user_input)

if choice==1:
 check_format_1(user_input)
 df,first_col_name=openfolder(directory)

 df=filter_dataframe(df,user_input,first_col_name)
 case1(df,first_col_name)
 
elif choice==2:
 check_format_2(user_input)
 user_input=user_input.replace("/","-")
 df,first_col_name=openfile(directory)
 df=filter_dataframe(df,user_input,first_col_name)
 case2(df,first_col_name)
elif choice==3:
 check_format_2(user_input)
 user_input=user_input.replace("/","-")
 df,first_col_name=openfile(directory)
 df=filter_dataframe(df,user_input,first_col_name)
 case3(df,first_col_name)    














