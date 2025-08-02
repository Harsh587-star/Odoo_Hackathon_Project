import streamlit as st
import folium
from streamlit_folium import st_folium
from aquapulse_core import drainlink

# Page setup
st.set_page_config(page_title="🌍 Flood Map", layout="wide")

# Header and description
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 42px;'>🌍 Flood Reports Map</h1>
        <p style='font-size: 22px; max-width: 850px; margin: 0 auto;'>
            This interactive map displays all reported waterlogging and drainage issues near you. Click on any marker to read full report details. 🚨🗺️
        </p>
    </div>
    <hr style='margin-top: 25px; margin-bottom: 25px;'>
""", unsafe_allow_html=True)

# Load data
conn = drainlink.get_connection()
cursor = conn.cursor()
cursor.execute("SELECT latitude, longitude, title, description FROM issues")
data = cursor.fetchall()

# Create map
m = folium.Map(location=[30.7333, 76.7794], zoom_start=13, control_scale=True)

for lat, lon, title, desc in data:
    try:
        lat_float = float(lat)
        lon_float = float(lon)
        folium.Marker(
            [lat_float, lon_float],
            popup=f"<b>{title}</b><br>{desc}",
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(m)
    except:
        continue

# Center the map visually in Streamlit
col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st_data = st_folium(m, width=950, height=600)
