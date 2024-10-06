import pandas as pd
import numpy as np

def load_generation_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['DATE_TIME'])
    df['DATE'] = df['DATE_TIME'].dt.date
    return df


# Function to load and preprocess weather data
def load_weather_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['DATE_TIME'])
    df['DATE'] = df['DATE_TIME'].dt.date
    return df

# Example function to calculate daily production
def daily_production(df):
    return df.groupby('DATE').agg({'DAILY_YIELD': 'max'}).reset_index()

# Example function to preprocess and merge generation and weather data
def merge_data(generation_df, weather_df):
    merged_df = pd.merge(generation_df, weather_df, on=['DATE_TIME', 'PLANT_ID'])
    return merged_df

import pandas as pd
import numpy as np

# Load generation data and create 'DATE' column
def load_generation_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['DATE_TIME'])
    df['DATE'] = df['DATE_TIME'].dt.date
    return df

# Load weather data and create 'DATE' column
def load_weather_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['DATE_TIME'])
    df['DATE'] = df['DATE_TIME'].dt.date
    return df

# Daily Production Distribution
def daily_production_distribution(df):
    return df.groupby('DATE').agg({'DAILY_YIELD': 'max'}).reset_index()

# Daily Production Density per Source
def daily_production_density_per_source(df):
    return df.groupby(['DATE', 'SOURCE_KEY']).agg({'DAILY_YIELD': 'sum'}).reset_index()

# Average Daily AC and DC Power
def average_daily_ac_dc_power(df):
    return df.groupby('DATE').agg({'AC_POWER': 'mean', 'DC_POWER': 'mean'}).reset_index()

# Hourly Daily Production Density
def hourly_daily_production_density(df):
    df['HOUR'] = df['DATE_TIME'].dt.hour
    return df.groupby(['DATE', 'HOUR']).agg({'DAILY_YIELD': 'sum'}).reset_index()

# AC and DC Power Density per Source
def ac_dc_power_density_per_source(df):
    return df.groupby(['DATE', 'SOURCE_KEY']).agg({'AC_POWER': 'mean', 'DC_POWER': 'mean'}).reset_index()

# Total Production Distribution Among Sources
def total_production_distribution(df):
    return df.groupby('SOURCE_KEY').agg({'DAILY_YIELD': 'sum'}).reset_index()

# Daily Total AC and DC Power Graphs
def daily_total_ac_dc_power(df):
    return df.groupby('DATE').agg({'AC_POWER': 'sum', 'DC_POWER': 'sum'}).reset_index()

# Daily and Total Production
def daily_and_total_production(df):
    df['CUMULATIVE_YIELD'] = df['DAILY_YIELD'].cumsum()
    return df[['DATE', 'DAILY_YIELD', 'CUMULATIVE_YIELD']]

# AC Power per Source
def ac_power_per_source(df):
    return df.groupby('SOURCE_KEY').agg({'AC_POWER': 'mean'}).reset_index()

# DC Power per Source
def dc_power_per_source(df):
    return df.groupby('SOURCE_KEY').agg({'DC_POWER': 'mean'}).reset_index()

# Weekly Production
def weekly_production(df):
    df['WEEK'] = df['DATE_TIME'].dt.isocalendar().week
    return df.groupby('WEEK').agg({'DAILY_YIELD': 'sum'}).reset_index()

# AC & DC Power Throughout the Day
def ac_dc_power_throughout_day(df):
    df['HOUR'] = df['DATE_TIME'].dt.hour
    return df.groupby('HOUR').agg({'AC_POWER': 'mean', 'DC_POWER': 'mean'}).reset_index()

# Change in AC & DC Power Throughout the Day
def change_ac_dc_power_throughout_day(df):
    df['HOUR'] = df['DATE_TIME'].dt.hour
    ac_diff = df.groupby('HOUR')['AC_POWER'].mean().diff().fillna(0)
    dc_diff = df.groupby('HOUR')['DC_POWER'].mean().diff().fillna(0)
    return pd.DataFrame({'HOUR': df['HOUR'].unique(), 'AC_CHANGE': ac_diff, 'DC_CHANGE': dc_diff})

# Percentage of DC Power Converted to AC Power
def percent_dc_converted_to_ac(df):
    df['PERCENT_DC_TO_AC'] = (df['AC_POWER'] / df['DC_POWER']) * 100
    return df[['DATE', 'PERCENT_DC_TO_AC']]

# Temperature Trends over Time
def temperature_trends(df):
    return df.groupby('DATE').agg({'AMBIENT_TEMPERATURE': 'mean', 'MODULE_TEMPERATURE': 'mean'}).reset_index()

# Daily Average Temperatures and Irradiation
def daily_avg_temp_irradiation(df):
    return df.groupby('DATE').agg({'AMBIENT_TEMPERATURE': 'mean', 'IRRADIATION': 'mean'}).reset_index()

# Ambient Temperature vs. Irradiation
def temp_vs_irradiation(df):
    return df[['DATE_TIME', 'AMBIENT_TEMPERATURE', 'IRRADIATION']]

# Daily Min/Max Ambient Temperature
def daily_min_max_temp(df):
    return df.groupby('DATE').agg({'AMBIENT_TEMPERATURE': ['min', 'max']}).reset_index()

# Hourly Average Temperatures and Irradiation
def hourly_avg_temp_irradiation(df):
    df['HOUR'] = df['DATE_TIME'].dt.hour
    return df.groupby('HOUR').agg({'AMBIENT_TEMPERATURE': 'mean', 'MODULE_TEMPERATURE': 'mean', 'IRRADIATION': 'mean'}).reset_index()

# Difference Between Module and Ambient Temperatures over Time
def temp_diff_module_vs_ambient(df):
    df['TEMP_DIFF'] = df['MODULE_TEMPERATURE'] - df['AMBIENT_TEMPERATURE']
    return df[['DATE', 'TEMP_DIFF']]

# Distribution of Irradiation Values
def irradiation_distribution(df):
    return df['IRRADIATION'].describe()

# Hourly Average Ambient Temperature by Day of Week
def hourly_avg_temp_by_day(df):
    df['DAY_OF_WEEK'] = df['DATE_TIME'].dt.day_name()
    df['HOUR'] = df['DATE_TIME'].dt.hour
    return df.groupby(['DAY_OF_WEEK', 'HOUR']).agg({'AMBIENT_TEMPERATURE': 'mean'}).reset_index()

# Hourly Average Irradiation by Day of Week
def hourly_avg_irradiation_by_day(df):
    df['DAY_OF_WEEK'] = df['DATE_TIME'].dt.day_name()
    df['HOUR'] = df['DATE_TIME'].dt.hour
    return df.groupby(['DAY_OF_WEEK', 'HOUR']).agg({'IRRADIATION': 'mean'}).reset_index()

# Correlation Between Ambient Temperature and Irradiation
def correlation_temp_irradiation(df):
    return df[['AMBIENT_TEMPERATURE', 'IRRADIATION']].corr()

# 7-day Moving Averages for Ambient Temperature and Irradiation
def moving_avg_temp_irradiation(df):
    df['7_DAY_TEMP_MA'] = df['AMBIENT_TEMPERATURE'].rolling(window=7).mean()
    df['7_DAY_IRRADIATION_MA'] = df['IRRADIATION'].rolling(window=7).mean()
    return df[['DATE', '7_DAY_TEMP_MA', '7_DAY_IRRADIATION_MA']]

# Correlation Matrix of Key Variables
def correlation_matrix(df):
    return df[['AC_POWER', 'DC_POWER', 'AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE', 'IRRADIATION']].corr()

# Daily Energy Production Time Series
def daily_energy_production(df):
    return df.groupby('DATE').agg({'DAILY_YIELD': 'sum'}).reset_index()

def avg_ac_dc_power(data):
    ac_power_avg = data['AC_POWER'].mean()
    dc_power_avg = data['DC_POWER'].mean()
    return ac_power_avg, dc_power_avg

def production_density(data):
    # Assume this function calculates production density per source
    density = data.groupby('SOURCE_KEY').agg({'AC_POWER': 'sum', 'DC_POWER': 'sum'}).reset_index()
    return density

# Daily Min/Max Ambient Temperature
def daily_min_max_temp(df):
    min_max = df.groupby('DATE').agg({'AMBIENT_TEMPERATURE': ['min', 'max']}).reset_index()
    # Flatten the multi-level columns
    min_max.columns = ['DATE', 'MIN_AMBIENT_TEMPERATURE', 'MAX_AMBIENT_TEMPERATURE']
    return min_max

