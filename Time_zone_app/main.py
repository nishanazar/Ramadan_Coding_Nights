import streamlit as st 
from datetime import datetime
from zoneinfo import ZoneInfo

st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: green !important;
        color: white !important;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px;
    }
    div.stsubheader
    </style>
    """,
    unsafe_allow_html=True
) 

TIME_ZONES = [
    "UTC",                  
    "America/New_York",     
    "America/Los_Angeles",   
    "Europe/London",        
    "Europe/Paris",          
    "Europe/Berlin",         
    "Europe/Moscow",         
    "Asia/Dubai",            
    "Asia/Karachi",          
    "Asia/Kolkata",          
    "Asia/Tokyo",            
    "Asia/Shanghai",        
    "Australia/Sydney",      
    "America/Sao_Paulo",     
    "Africa/Cairo"           
]

st.title("Time Zone App🕐 ")

selected_time_zone = st.multiselect("Select Time Zones", TIME_ZONES, default=["UTC", "Asia/Karachi"]) 

st.subheader(":green[Selected Timezones]")
for tz in selected_time_zone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")


st.subheader(":red[Convert Time Between Timezones]")
current_time = st.time_input("Current Time ", value=datetime.now().time())

from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(),current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"Converted Time in {to_tz}: {converted_time}")