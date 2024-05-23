# import mysql.connector #pip install mysql-connector-python
# import streamlit as st #pip install streamlit

# # 1. Establish Connection to MySQL Server
# myDB = mysql.connector.connect(
#     host='localhost', 
#     user = 'root',
#     password = '', # as used in the setup of sql server
#     database = 'Khidmat', # //

#     )

# myCursor = myDB.cursor()
# print("Connection established")

# # 2. Create Streamlit WebApp    
# def main():
#     st.title("CRUD Operations with MySQL")
#     #streamlit run testing.py


# if __name__ == '__main__':
#     main()

#############
import streamlit as st
import pandas as pd

st.write("## Displaying all of the forms")
st.write("### 1. Adding a new Pet")
# data = pd.read_csv("Cats.csv")
# st.write(data)

###################
# Create a form
form = st.form("Add Pet")

# Name field
name = form.text_input("Name")

# Status dropdown with new options
status = form.selectbox("Status", [
     
    "Adopted", 
    "Discharged",
    "Expired",
    "Fostered",
    "Healthy In Lower Portion",
    "Missing",
    "Moved To Healthy Area",
    "Ready To Be Moved To Healthy Area",
    "Ready To Discharge",
    "Under Observation",
    "Under Treatment"
])

# Cage number text input
cage_num = form.text_input("Cage Number")

# Remarks text area
remarks = form.text_area("Remarks")

# Owner name text input
owner_name = form.text_input("Owner Name")

# Owner contact text input 
owner_contact = form.text_input("Owner Contact")

# Arrange buttons horizontally
col1, col2 = form.columns(2)
with col1:
    submitted = form.form_submit_button("Add Pet")
with col2:
    cancelled = form.form_submit_button("Cancel")

# Flag to track message box visibility
show_message_box = st.empty()  # Initially empty element

if submitted:
    # Check if any of the fields are left unfilled
    if not (name and status and cage_num and owner_name and owner_contact):
        show_message_box.error("Please fill in all fields before submitting.")
    else:
        # Add logic to process form data here 
        st.success(f"Pet {name} added successfully!")
        # You can potentially use the data to update a database or perform other actions
        st.write(f"Name: {name}")
        st.write(f"Status: {status}")
        st.write(f"Cage Number: {cage_num}")
        st.write(f"Remarks: {remarks}")
        st.write(f"Owner Name: {owner_name}")
        st.write(f"Owner Contact: {owner_contact}")

elif cancelled:
    # Handle cancel button click (optional)
    st.warning("Form submission cancelled.")

#########################

st.write("### 2. Ward Details")

import streamlit as st

# Create a form
form = st.form("Add Ward")

# Ward name text input
ward_name = form.text_input("Ward Name")

# Ward type dropdown
ward_type = form.selectbox("Ward Type", [
    "General Ward",
    "ICU Ward",
    "Lounge",
    "Qurantine",
    "Viral Room",
])

# Capacity text input
capacity = form.text_input("Capacity")

# Available beds text input
available_beds = form.text_input("Available Beds")

# Remarks text area
remarks = form.text_area("Remarks")

# Submit button
submitted = form.form_submit_button("Add Ward")
cancelled = form.form_submit_button("Cancel")


if submitted:
    # Add logic to process form data here
    st.success(f"Ward '{ward_name}' added successfully!")
    # You can potentially use the data to update a database or perform other actions
    st.write(f"Ward Name: {ward_name}")
    st.write(f"Ward Type: {ward_type}")
    st.write(f"Capacity: {capacity}")
    st.write(f"Available Beds: {available_beds}")
    st.write(f"Remarks: {remarks}")

elif cancelled:
    # Handle cancel button click (optional)
    st.warning("Form submission cancelled.")
