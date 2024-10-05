import pandas as pd

def load_data(plant):
    if plant == "Plant 1":
        generation_data = pd.read_csv('Plant_1_Generation_Data.csv')  
        weather_data = pd.read_csv('Plant_1_Weather_Sensor_Data.csv')  
    else:
        generation_data = pd.read_csv('Plant_2_Generation_Data.csv') 
        weather_data = pd.read_csv('Plant_2_Weather_Sensor_Data.csv')  
    
    # Ensure DATE_TIME is in datetime format
    generation_data['DATE_TIME'] = pd.to_datetime(generation_data['DATE_TIME'], dayfirst=True)
    weather_data['DATE_TIME'] = pd.to_datetime(weather_data['DATE_TIME'], dayfirst=True)

    return generation_data, weather_data

def filter_data(data, start_date, end_date):
    return data[(data['DATE_TIME'] >= start_date) & (data['DATE_TIME'] <= end_date)]

def compute_moving_average(data, column, window_size):
    return data[column].rolling(window=window_size).mean()

def descriptive_statistics(data):
    return data.describe()

def key_insights(generation_data, weather_data):
    insights = {
        "max_ac_power": generation_data['AC_POWER'].max(),
        "min_ac_power": generation_data['AC_POWER'].min(),
        "average_daily_yield": generation_data['DAILY_YIELD'].mean(),
        "max_temp": weather_data['AMBIENT_TEMPERATURE'].max(),
        "min_temp": weather_data['AMBIENT_TEMPERATURE'].min(),
        "average_irradiation": weather_data['IRRADIATION'].mean(),
    }
    return insights
