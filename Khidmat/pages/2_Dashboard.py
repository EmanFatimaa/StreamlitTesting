# import streamlit as st
# import pandas as pd


# data = pd.read_csv("Donations.csv")
# st.write(data)
# st.line_chart(data)

import streamlit as st
import pandas as pd

st.write("# DashBoard!")

# Read the cleaned CSV data
df = pd.read_csv('Donations.csv')
# st.write(df)
# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

# Extract month from 'Date' column
df['Month'] = df['Date'].dt.strftime('%b')

# Group by month and sum the donations
monthly_donations = df.groupby('Month')['Amount'].sum().reset_index()

# Display bar chart
st.write("## Donations Received by Month")
st.bar_chart(monthly_donations.set_index('Month')['Amount'])
