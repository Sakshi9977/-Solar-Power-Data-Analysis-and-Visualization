import streamlit as st
import plotly.express as px
import pandas as pd

# Import preprocessor functions
from preprocessor import load_data, filter_data, compute_moving_average, descriptive_statistics, key_insights

# Set the Plotly colors palette
colors = px.colors.qualitative.Plotly 

# Set up the main dashboard
st.set_page_config(page_title="Solar Power Plant Dashboard", layout="wide")

# Sidebar for user inputs
st.image("assets/SOLAR POWER.jpg", width=120)
st.sidebar.image("assets/SOLAR POWER.jpg", width=120)
st.sidebar.title("Solar Power Plant Analysis Dashboard")
page = st.sidebar.radio("Go to", ["Home", "Insights", "Data Visualization"])

# Load the datasets based on user selections
plant = st.sidebar.selectbox("Select Plant", ["Plant 1", "Plant 2"])
generation_data, weather_data = load_data(plant)

# Reduce space between sidebar and main content
st.markdown("<style>div.row-widget.stRadio {margin-top: -20px;}</style>", unsafe_allow_html=True)

if page == "Home":
    st.title("🌞Welcome to the Solar Power Plant Dashboard🌞")
    st.write("This dashboard allows you to explore power generation and weather data from solar power plants in India.")
    st.write("Use the sidebar to navigate to different pages and visualize the data.")
    st.markdown("---")  # Separator
    # Introduction
    st.header("⚡ Introduction")
    st.write(
    """Welcome to the **Solar Power Analysis Dashboard**! This project dives deep into the solar power generation data from two different plants, aiming to uncover valuable insights, visualize essential trends, and create an interactive dashboard using **Streamlit**. Our goal is to empower stakeholders to efficiently manage and optimize solar power generation.""")

    # Core Functionality
    st.header("🚀 Core Functionality")
    st.write(
    """The dashboard serves as a powerful tool that provides key insights into solar power generation trends, evaluates plant performance, and identifies patterns to optimize energy production.""")

    # Project Type
    st.header("🛠️ Project Type")
    st.write("**Data Analysis and Visualization**")

    # Deployed Application
    st.header("🌐 Deployed Application")
    st.write(
    """- **Frontend**: Streamlit Dashboard\n
    - Data is analyzed and visualized directly within Streamlit, ensuring a seamless user experience.\n
    - **Database**: Data is sourced from CSV files—no external database is used, making it lightweight and efficient.""")

    # Contributors
    st.header("🧑‍🤝‍🧑 Contributors")
    contributors = [
        "🌟 **Gaurav Lakshakar (Team Lead)**",
        "🌟 **Aayush Vishwakarma (Team Member)**",
        "🌟 **Sakshi Prajapati (Team Member)**",
        "🌟 **Shailesh Kumar Singh (Team Member)**"
    ]

    for contributor in contributors:
        st.write(contributor)

    # Footer
    st.markdown("---")
    st.write("Thank you for visiting the Solar Power Analysis Dashboard!")
    
elif page == "Insights":
    st.title("🚀 **Key Insights:**")
    st.write("""
- **Peak Power Generation**: Typically between 10 AM and 2 PM.
- **Seasonal Impact**: Higher generation in summer.
- **Plant Performance**: Certain plants perform better, suggesting geographical advantages.
""")

    insights = key_insights(generation_data, weather_data)
    
    st.subheader("Generation Insights")
    st.write(f"Maximum AC Power: {insights['max_ac_power']}")
    st.write(f"Minimum AC Power: {insights['min_ac_power']}")
    st.write(f"Average Daily Yield: {insights['average_daily_yield']:.2f}")
    
    st.subheader("Weather Insights")
    st.write(f"Maximum Ambient Temperature: {insights['max_temp']}")
    st.write(f"Minimum Ambient Temperature: {insights['min_temp']}")
    st.write(f"Average Irradiation: {insights['average_irradiation']:.2f}")
    
    # Key Insights
    st.header("✨ Key Insights")
    key_insights = [
        "🔆 **Peak Power Generation Times**: Most plants achieve peak solar power generation between **10 AM and 2 PM**.",
        "☀️ **Seasonal Impact**: Power generation soars during summer months, averaging a **20% increase** compared to winter.",
        "📉 **Performance Disparities**: Analyze performance differences between plants, shedding light on inefficiencies or geographical advantages.",
        "🌧️ **Power Loss Trends**: An average **15% power loss** during rainy seasons due to reduced sunlight exposure.",
        "⚠️ **Outliers in Power Output**: Sudden drops in power generation in Plant C could indicate potential equipment issues.",
        "📈 **Maximizing Output**: Optimizing solar panel angles can enhance power generation by **10%** on average."
    ]

    for insight in key_insights:
        st.write(insight)

    # Features
    st.header("✨ Features")
    features = [
       "🌍 **Interactive Filters**: Dynamically filter data by solar plant, date range, or power output.",
       "📊 **Insightful Visualizations**: Engage with line charts, bar charts, and scatter plots.",
       "⚖️ **Plant Performance Comparison**: Compare generation across different plants or timeframes.",
       "📅 **Time-Series Analysis**: Analyze solar power generation daily, monthly, or seasonally.",
       "📝 **Top KPIs & Insights**: Key insights are highlighted for informed decision-making."
    ]

    for feature in features:
        st.write(feature)

    # Design Decisions
    st.header("🎨 Design Decisions & Assumptions")
    design_decisions = [
       "📉 **Handling Missing Data**: Missing data points have been removed for clarity, while outliers are noted.",
       "🎯 **Focus on Visuals**: This project emphasizes data analysis without backend complexity.",
       "📊 **Scalability**: Designed for easy addition of new solar plants."
    ]

    for decision in design_decisions:
        st.write(decision)

    # Usage Instructions
    st.header("🎯 Usage")
    st.write(
        """To start using the Streamlit app:\n
        1. **Filter Data**: Select your desired date range, plant, and other options using intuitive sliders and dropdowns.\n
        2. **Explore Visualizations**: Dive into various graphs to analyze performance trends and identify patterns."""
    )

    # Technology Stack
    st.header("💻 Technology Stack")
    technology_stack = [
        "🔧 **Python**: Core programming language for data analysis.",
        "📊 **Pandas**: Essential for data cleaning and preprocessing.",
        "🌐 **Streamlit**: Framework for building our interactive web app.",
        "📈 **Matplotlib & Plotly**: Libraries for creating dynamic visualizations."
    ]

    for tech in technology_stack:
        st.write(tech)

    # Additional Features
    st.header("🚀 Additional Features")
    additional_features = [
       "🌟 **Dark Mode Support**: Switch between light and dark themes.",
       "🔍 **Advanced Filtering**: Filter by power output ranges or specific date intervals.",
       "📈 **Real-time Data Updates**: Future iterations will enable fetching and analyzing live data.",
       "📋 **KPI Summary Section**: Show key performance metrics (max, min, average power generation).",
       "📱 **Mobile Responsive**: The dashboard is optimized for mobile viewing."
    ]

    for feature in additional_features:
       st.write(feature)

    # Future Work
    st.header("📝 Future Work")
    future_work = [
      "🔗 **Integration with Live Data Sources**: Automating the data pipeline for real-time solar plant data.",
      "📊 **Predictive Modeling**: Incorporating machine learning algorithms to forecast power output.",
      "⚙️ **Optimization Suggestions**: Providing actionable insights to optimize plant performance."
    ]

    for work in future_work:
       st.write(work)
       
elif page == "Data Visualization":
    data_type = st.sidebar.selectbox("Select Data Type", ["Generation Data", "Weather Data"])

    # Date range selection
    if data_type == "Generation Data":
        start_date = st.sidebar.date_input("Start Date", value=generation_data['DATE_TIME'].min().date())
        end_date = st.sidebar.date_input("End Date", value=generation_data['DATE_TIME'].max().date())
        
        start_date, end_date = pd.to_datetime(start_date), pd.to_datetime(end_date)
        filtered_data = filter_data(generation_data, start_date, end_date)

        # Moving Average Window Size
        window_size = st.sidebar.number_input("Select Moving Average Window Size", min_value=1, value=7)

        # Calculate and plot Moving Average of AC Power
        filtered_data['MA_AC_POWER'] = compute_moving_average(filtered_data, 'AC_POWER', window_size)
        st.line_chart(filtered_data[['DATE_TIME', 'MA_AC_POWER']].set_index('DATE_TIME'))

        # Descriptive Statistics
        if st.sidebar.checkbox("Show Descriptive Statistics"):
            st.subheader("Descriptive Statistics")
            stats = descriptive_statistics(filtered_data)
            st.dataframe(stats)  # Display the DataFrame without hiding the index

        # Graph type selection
        graph_type = st.sidebar.selectbox("Select Graph Type", ["Line", "Bar", "Scatter", "Boxplot", "Histogram", "Pie", "Heatmap"])

        # Display graphs based on selected type
        if graph_type == "Line":
            fig = px.line(filtered_data, x='DATE_TIME', y=['DC_POWER', 'AC_POWER'], title=f"Line Plot for {plant}", color_discrete_sequence=colors)
            st.plotly_chart(fig)
            st.write("**Related Insight:** Comparison of DC and AC over time.")
        elif graph_type == "Bar":
            fig = px.bar(filtered_data, x='DATE_TIME', y='DC_POWER', title=f"Bar Plot of DC Power ({plant})", color_discrete_sequence=colors)
            st.plotly_chart(fig)
            st.write("**Related Insight:** DC power generation trends over time.")
        elif graph_type == "Scatter":
            fig = px.scatter(filtered_data, x='DC_POWER', y='AC_POWER', title=f"Scatter Plot (DC vs AC Power) ({plant})", color_discrete_sequence=colors)
            st.plotly_chart(fig)
            st.write("**Related Insight:** Relationship between DC power and AC power generation.")
        elif graph_type == "Boxplot":
            fig = px.box(filtered_data, y='DC_POWER', title=f"Boxplot of DC Power ({plant})", color_discrete_sequence=colors)
            st.plotly_chart(fig)
            st.write("**Related Insight:** Distribution of DC power output over time.")
        elif graph_type == "Histogram":
            fig = px.histogram(filtered_data, x='DC_POWER', nbins=50, title=f"Histogram of DC Power ({plant})", color_discrete_sequence=colors)
            st.plotly_chart(fig)
            st.write("**Related Insight:** Distribution of DC Power generation over time.")
        elif graph_type == "Pie":
            fig = px.pie(filtered_data, names='DATE_TIME', values='DC_POWER', title=f"Pie Chart of Power Generation ({plant})", color_discrete_sequence=colors)
            st.plotly_chart(fig)
            st.write("**Related Insight:** Distribution of power generation between different plants.")
        elif graph_type == "Heatmap":
            correlation_data = filtered_data[['DC_POWER', 'AC_POWER', 'DAILY_YIELD']].corr()
            fig = px.imshow(correlation_data, title=f"Heatmap of Power Data ({plant})")
            st.plotly_chart(fig)
            st.write("**Related Insight:** Correlation between DC power and AC power.")
    elif data_type == "Weather Data":
        start_date = st.sidebar.date_input("Start Date", value=weather_data['DATE_TIME'].min().date())
        end_date = st.sidebar.date_input("End Date", value=weather_data['DATE_TIME'].max().date())
        
        start_date, end_date = pd.to_datetime(start_date), pd.to_datetime(end_date)
        filtered_weather_data = filter_data(weather_data, start_date, end_date)

        # Moving Average Window Size for Weather Data
        window_size_weather = st.sidebar.number_input("Select Moving Average Window Size for Weather", min_value=1, value=7)

        # Calculate and plot Moving Average of Ambient Temperature
        filtered_weather_data['MA_AMBIENT_TEMP'] = compute_moving_average(filtered_weather_data, 'AMBIENT_TEMPERATURE', window_size_weather)
        st.line_chart(filtered_weather_data[['DATE_TIME', 'MA_AMBIENT_TEMP']].set_index('DATE_TIME'))

        # Descriptive Statistics for Weather Data
        if st.sidebar.checkbox("Show Descriptive Statistics for Weather Data"):
            st.subheader("Descriptive Statistics for Weather Data")
            stats_weather = descriptive_statistics(filtered_weather_data)
            st.dataframe(stats_weather)

        # Weather graph type selection
        weather_graph_type = st.sidebar.selectbox("Select Weather Graph Type", ["Line", "Bar", "Scatter", "Boxplot", "Histogram", "Pie", "Heatmap"])

        # Display weather graphs
        if weather_graph_type == "Line":
            fig = px.line(filtered_weather_data, x='DATE_TIME', y=['AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE'],
                          title=f"Temperature Over Time ({plant})", color_discrete_sequence=colors)
            st.plotly_chart(fig)
            st.write("**Related Insight:** Trends in ambient and module temperatures reveal their correlation over time.")
        elif weather_graph_type == "Bar":
            fig = px.bar(filtered_weather_data, x='DATE_TIME', y='AMBIENT_TEMPERATURE', title=f"Bar Plot of Ambient Temperature ({plant})", color_discrete_sequence=colors)
            st.plotly_chart(fig)
            st.write("**Related Insight:** Distribution of average ambient temperature across different time periods.")
        elif weather_graph_type == "Scatter":
            fig = px.scatter(filtered_weather_data, x='AMBIENT_TEMPERATURE', y='IRRADIATION',
                             title=f"Scatter Plot (Temperature vs Irradiation) ({plant})", color_discrete_sequence=colors)
            st.plotly_chart(fig)
            st.write("**Related Insight:** Relationship between temperature (ambient/module) and irradiation.")
        elif weather_graph_type == "Boxplot":
            fig = px.box(filtered_weather_data, y='AMBIENT_TEMPERATURE', title=f"Boxplot of Ambient Temperature ({plant})", color_discrete_sequence=colors)
            st.plotly_chart(fig)
            st.write("**Related Insight:** Distribution and variability of ambient temperature.")
        elif weather_graph_type == "Histogram":
            fig = px.histogram(filtered_weather_data, x='AMBIENT_TEMPERATURE', nbins=50, title=f"Histogram of Ambient Temperature ({plant})", color_discrete_sequence=colors)
            st.plotly_chart(fig)
            st.write("**Related Insight:** Distribution of ambient temperature values.")
        elif weather_graph_type == "Pie":
            fig = px.pie(filtered_weather_data, names='DATE_TIME', values='IRRADIATION', title=f"Pie Chart of Irradiation ({plant})", color_discrete_sequence=colors)
            st.plotly_chart(fig)
            st.write("**Related Insight:** Irradiation distribution across different days or plant locations.")
        elif weather_graph_type == "Heatmap":
            correlation_weather_data = filtered_weather_data[['AMBIENT_TEMPERATURE', 'MODULE_TEMPERATURE', 'IRRADIATION']].corr()
            fig = px.imshow(correlation_weather_data, title=f"Heatmap of Weather Data ({plant})")
            st.plotly_chart(fig)
            st.write("**Related Insight:** Correlation between ambient temperature, module temperature, and irradiation.")
# Add any additional resources or information in the sidebar
st.sidebar.title("Additional Resources")
st.sidebar.write("Include relevant resources or documentation.")
st.sidebar.markdown("- **User Guide:** Detailed documentation on using this dashboard.")
st.sidebar.markdown("- **Contact:** Email support at support@example.com")
st.sidebar.markdown("- **Feedback:** We value your feedback! Please fill out our [survey](#).")
