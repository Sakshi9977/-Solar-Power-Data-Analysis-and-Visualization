import streamlit as st
import pandas as pd
from preprocessor import (
    load_generation_data,
    load_weather_data,
    daily_production_distribution,
    daily_production_density_per_source,
    average_daily_ac_dc_power,
    total_production_distribution,
    daily_total_ac_dc_power,
    weekly_production,
    temperature_trends,
    daily_avg_temp_irradiation,
    daily_min_max_temp,
    correlation_temp_irradiation,
)

# Set up the main dashboard
st.set_page_config(page_title="Solar Power Plant Dashboard", layout="wide")

# Title and description
st.title("🌞 Solar Power Plant Analysis Dashboard 🌞")
st.write("This dashboard allows you to explore power generation and weather data from two solar power plants in India.")
st.write("📊 Use the sidebar to visualize the data 📊")
st.markdown("---")
st.image("SOLAR.jpg",width=400 ,use_column_width=50)
st.write("🎯 Thank you for visiting the Solar Power Analysis Dashboard 🎯")
st.markdown("---")

# Load the datasets
generation_data_plant_1 = load_generation_data('Plant_1_Generation_Data.csv')
weather_data_plant_1 = load_weather_data('Plant_1_Weather_Sensor_Data.csv')
generation_data_plant_2 = load_generation_data('Plant_2_Generation_Data.csv')
weather_data_plant_2 = load_weather_data('Plant_2_Weather_Sensor_Data.csv')

# Sidebar for dataset selection
st.sidebar.title("Select Data")
dataset_selection = st.sidebar.radio(
    "Select dataset:",
    ("Generation Data - Plant 1", "Weather Data - Plant 1", 
     "Generation Data - Plant 2", "Weather Data - Plant 2")
)

# Sidebar for multiselect options
if dataset_selection == "Generation Data - Plant 1":
    st.sidebar.subheader("Select Analysis for Plant 1 Generation Data")
    options = st.sidebar.multiselect(
        "Select options:",
        [
            "Daily Production Distribution",
            "Daily Production Density per Source",
            "Average Daily AC/DC Power",
            "Total Production Distribution",
            "Daily Total AC/DC Power",
            "Weekly Production",
        ],
    )
    df = generation_data_plant_1
elif dataset_selection == "Weather Data - Plant 1":
    st.sidebar.subheader("Select Analysis for Plant 1 Weather Data")
    options = st.sidebar.multiselect(
        "Select options:",
        [
            "Temperature Trends",
            "Daily Average Temperatures and Irradiation",
            "Daily Min/Max Ambient Temperature",
            "Correlation Between Ambient Temperature and Irradiation",
        ],
    )
    df = weather_data_plant_1
elif dataset_selection == "Generation Data - Plant 2":
    st.sidebar.subheader("Select Analysis for Plant 2 Generation Data")
    options = st.sidebar.multiselect(
        "Select options:",
        [
            "Daily Production Distribution",
            "Daily Production Density per Source",
            "Average Daily AC/DC Power",
            "Total Production Distribution",
            "Daily Total AC/DC Power",
            "Weekly Production",
        ],
    )
    df = generation_data_plant_2
else:
    st.sidebar.subheader("Select Analysis for Plant 2 Weather Data")
    options = st.sidebar.multiselect(
        "Select options:",
        [
            "Temperature Trends",
            "Daily Average Temperatures and Irradiation",
            "Daily Min/Max Ambient Temperature",
            "Correlation Between Ambient Temperature and Irradiation",
        ],
    )
    df = weather_data_plant_2

# Display selected options
for option in options:
    if option == "Daily Production Distribution":
        st.subheader("Daily Production Distribution")
        daily_prod_dist = daily_production_distribution(df)
        st.write(daily_prod_dist)

    elif option == "Daily Production Density per Source":
        st.subheader("Daily Production Density per Source")
        density_per_source = daily_production_density_per_source(df)
        st.write(density_per_source)

    elif option == "Average Daily AC/DC Power":
        st.subheader("Average Daily AC/DC Power")
        avg_power = average_daily_ac_dc_power(df)
        st.write(avg_power)

    elif option == "Total Production Distribution":
        st.subheader("Total Production Distribution")
        total_dist = total_production_distribution(df)
        st.write(total_dist)

    elif option == "Daily Total AC/DC Power":
        st.subheader("Daily Total AC/DC Power")
        daily_totals = daily_total_ac_dc_power(df)
        st.write(daily_totals)

    elif option == "Weekly Production":
        st.subheader("Weekly Production")
        weekly_prod = weekly_production(df)
        st.write(weekly_prod)

    elif option == "Temperature Trends":
        st.subheader("Temperature Trends")
        temp_trends = temperature_trends(df)
        st.write(temp_trends)

    elif option == "Daily Average Temperatures and Irradiation":
        st.subheader("Daily Average Temperatures and Irradiation")
        avg_temp_irradiation = daily_avg_temp_irradiation(df)
        st.write(avg_temp_irradiation)

    elif option == "Daily Min/Max Ambient Temperature":
        st.subheader("Daily Min/Max Ambient Temperature")
        min_max_temp = daily_min_max_temp(df)
        st.write(min_max_temp)

    elif option == "Correlation Between Ambient Temperature and Irradiation":
        st.subheader("Correlation Between Ambient Temperature and Irradiation")
        correlation = correlation_temp_irradiation(df)
        st.write(correlation)

# Visualization options
st.sidebar.header("Select Graphs")
graph_options = []
for option in options:
    if option == "Daily Production Distribution":
        graph_options.append("Daily Production Distribution Graph")
    elif option == "Daily Production Density per Source":
        graph_options.append("Daily Production Density per Source Graph")
    elif option == "Average Daily AC/DC Power":
        graph_options.append("Average Daily AC/DC Power Graph")
    elif option == "Total Production Distribution":
        graph_options.append("Total Production Distribution Graph")
    elif option == "Daily Total AC/DC Power":
        graph_options.append("Daily Total AC/DC Power Graph")
    elif option == "Weekly Production":
        graph_options.append("Weekly Production Graph")
    elif option == "Temperature Trends":
        graph_options.append("Temperature Trends Graph")
    elif option == "Daily Average Temperatures and Irradiation":
        graph_options.append("Daily Average Temperatures and Irradiation Graph")
    elif option == "Daily Min/Max Ambient Temperature":
        graph_options.append("Daily Min/Max Ambient Temperature Graph")
    elif option == "Correlation Between Ambient Temperature and Irradiation":
        graph_options.append("Correlation Graph")

selected_graphs = st.sidebar.multiselect("Select graphs to display:", graph_options)

# Show selected graphs
if "Daily Production Distribution Graph" in selected_graphs:
    st.subheader("Daily Production Distribution Graph")
    st.line_chart(daily_production_distribution(df)['DAILY_YIELD'])
    st.write("The Daily Production Distribution Graph reveals the variability in energy output, highlighting peak production days and periods of low performance, which can inform operational adjustments.")

if "Daily Production Density per Source Graph" in selected_graphs:
    st.subheader("Daily Production Density per Source Graph")
    density_data = daily_production_density_per_source(df)
    st.bar_chart(density_data.set_index('SOURCE_KEY')['DAILY_YIELD'])
    st.write("The Daily Production Density per Source graph reveals variations in energy output efficiency across different sources, highlighting which sources are most effective on specific days.")
 
if "Average Daily AC/DC Power Graph" in selected_graphs:
    st.subheader("Average Daily AC/DC Power Graph")
    avg_power_data = average_daily_ac_dc_power(df)
    st.write(avg_power_data)
    st.write("The Average Daily AC/DC Power graph reveals trends in energy production efficiency and highlights potential areas for optimizing solar panel performance over time.")
    
if "Total Production Distribution Graph" in selected_graphs:
    st.subheader("Total Production Distribution Graph")
    total_dist_data = total_production_distribution(df)
    st.bar_chart(total_dist_data.set_index('SOURCE_KEY')['DAILY_YIELD'])
    st.write("The Total Production Distribution graph reveals the overall yield variability, highlighting peak production periods and identifying trends in energy output efficiency.")

if "Daily Total AC/DC Power Graph" in selected_graphs:
    st.subheader("Daily Total AC/DC Power Graph")
    daily_totals_data = daily_total_ac_dc_power(df)
    st.line_chart(daily_totals_data.set_index('DATE'))
    st.write("The Daily Total AC/DC Power graph reveals trends in energy generation efficiency and system performance, highlighting variations in output based on environmental conditions.")

if "Weekly Production Graph" in selected_graphs:
    st.subheader("Weekly Production Graph")
    weekly_prod_data = weekly_production(df)
    st.line_chart(weekly_prod_data.set_index('WEEK'))
    st.write("The Weekly Production Graph reveals trends in production output, highlighting peak performance weeks and identifying periods for potential efficiency improvements.")

if "Temperature Trends Graph" in selected_graphs:
    st.subheader("Temperature Trends Graph")
    temp_trends_data = temperature_trends(df)
    st.line_chart(temp_trends_data.set_index('DATE'))
    st.write("The Temperature Trends graph highlights seasonal variations, revealing peaks and troughs that indicate changes in ambient temperature over time")

if "Daily Average Temperatures and Irradiation Graph" in selected_graphs:
    st.subheader("Daily Average Temperatures and Irradiation Graph")
    avg_temp_irradiation_data = daily_avg_temp_irradiation(df)
    st.line_chart(avg_temp_irradiation_data.set_index('DATE'))
    st.write("The Daily Average Temperatures and Irradiation graph reveals the correlation between temperature fluctuations and solar irradiance, indicating optimal conditions for solar energy generation.")
    
if "Daily Min/Max Ambient Temperature Graph" in selected_graphs:
    st.subheader("Daily Min/Max Ambient Temperature Graph")
    min_max_temp_data = daily_min_max_temp(df)
    st.line_chart(min_max_temp_data.set_index('DATE'))
    st.write("The Daily Min/Max Ambient Temperature graph reveals fluctuations in temperature patterns, indicating seasonal changes and potential impacts on energy production and plant efficiency.")
    
if "Correlation Graph" in selected_graphs:
    st.subheader("Correlation Between Ambient Temperature and Irradiation Graph")
    correlation_data = correlation_temp_irradiation(df)
    st.line_chart(correlation_data)
    st.write("The graph reveals a positive correlation between ambient temperature and irradiation, indicating that higher temperatures generally coincide with increased solar irradiance.")
    
# Display additional information
st.sidebar.header("Additional Information")
if st.sidebar.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(df)

# Additional resources or information 
st.sidebar.title("Additional Resources:-")
st.sidebar.markdown("- **Contact:** Email support at gauravlakshakar581@gmail.com")
st.sidebar.markdown("- **Feedback:** We value your feedback! Please fill out our survey.")

st.markdown("---")
# Survey Form Title
st.title("User Feedback Survey")

# Survey Questions
name = st.text_input("What is your name?")
email = st.text_input("What is your email address?")
feedback = st.text_area("Please provide your feedback:")
rating = st.radio("How would you rate our service?", ["Excellent", "Good", "Average", "Poor"])

# Submit Button
if st.button("Submit"):
    st.success("Thank you for your feedback!")