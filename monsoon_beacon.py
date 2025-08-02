import streamlit as st

# Set page title and layout
st.set_page_config(page_title="🌧️ FloodTrack Home", layout="centered")

# Header
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 42px;'>🌧️ Welcome to FloodTrack</h1>
        <p style='font-size: 22px; max-width: 800px; margin: 0 auto;'>
            Your companion for reporting and monitoring monsoon-related drainage and waterlogging issues in your locality. 
            Help us make your city smarter, cleaner, and flood-free. 🌊🛠️
        </p>
    </div>
    <hr style='margin-top: 25px; margin-bottom: 25px;'>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🚨 FloodTrack Navigation")
st.sidebar.page_link("pages/splash_submit.py", label="📝 Report an Issue")
st.sidebar.page_link("pages/flood_map.py", label="🌍 View Flood Map")
st.sidebar.page_link("pages/my_drain_trails.py", label="📂 My Submissions")
st.sidebar.page_link("pages/drainage_watchtower.py", label="🛠️ Admin Dashboard")

# Welcome message
st.markdown("""
<div style="font-size: 20px; text-align: center;">
    👈 Use the navigation sidebar to access different features of the app.<br><br>
    Thank you for being a part of the solution! 💧✨
</div>
""", unsafe_allow_html=True)
