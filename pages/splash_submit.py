import streamlit as st
from aquapulse_core import drainlink
import os
import datetime

# Page setup
st.set_page_config(page_title="📝 Report an Issue", layout="centered")

# Title and intro
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 40px;'>📝 Report a Drainage Problem</h1>
        <p style='font-size: 20px; max-width: 750px; margin: 0 auto;'>
            Help us identify problem areas in your city. Your reports allow civic authorities to respond faster and plan better. 🚧💧
        </p>
    </div>
    <hr style='margin-top: 25px;'>
""", unsafe_allow_html=True)

# Title
st.markdown("<h3 style='font-size:24px;'>🏷️ Issue Title</h3>", unsafe_allow_html=True)
title = st.text_input("Short and clear (e.g. 'Drain Overflow at Bus Stand')", max_chars=80)

# Description
st.markdown("<h3 style='font-size:24px;'>🧾 Description</h3>", unsafe_allow_html=True)
description = st.text_area("Describe the issue with details like frequency, severity, etc.", max_chars=500)

# Category
st.markdown("<h3 style='font-size:24px;'>📂 Select a Category</h3>", unsafe_allow_html=True)
category = st.selectbox("Choose the closest match", ["Waterlogging", "Blocked Drain", "Overflow", "Stagnant Water", "Other"])

# Location
st.markdown("<h3 style='font-size:24px;'>🗺️ Enter Location</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    latitude = st.text_input("Latitude (e.g. 30.7333)")
with col2:
    longitude = st.text_input("Longitude (e.g. 76.7794)")

# Contact
st.markdown("<h3 style='font-size:24px;'>📧 Your Email</h3>", unsafe_allow_html=True)
email = st.text_input("We'll use this to notify you about status updates.")

# Images
st.markdown("<h3 style='font-size:24px;'>🖼️ Upload Photos (optional)</h3>", unsafe_allow_html=True)
uploaded_files = st.file_uploader("You can upload up to 3 images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# Submit button
if st.button("🚀 Submit Report", use_container_width=True):
    if title and description and category and latitude and longitude and email:
        conn = drainlink.get_connection()
        cursor = conn.cursor()

        # Ensure user exists
        cursor.execute("SELECT user_id FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()
        if not user:
            cursor.execute("INSERT INTO users (name, email, password_hash, role) VALUES (%s, %s, %s, %s)",
                           (email.split("@")[0], email, '', 'user'))
            conn.commit()
            cursor.execute("SELECT user_id FROM users WHERE email=%s", (email,))
            user = cursor.fetchone()

        user_id = user[0]

        # Insert issue
        cursor.execute("""
            INSERT INTO issues (user_id, title, description, category, latitude, longitude, status, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (user_id, title, description, category, latitude, longitude, 'Reported', datetime.datetime.now()))
        conn.commit()
        issue_id = cursor.lastrowid

        # Save uploaded images
        if uploaded_files:
            os.makedirs("basin_bucket", exist_ok=True)
            for file in uploaded_files:
                save_path = os.path.join("basin_bucket", file.name)
                with open(save_path, "wb") as f:
                    f.write(file.getbuffer())
                cursor.execute("INSERT INTO images (issue_id, file_path) VALUES (%s, %s)", (issue_id, save_path))
            conn.commit()

        st.success("✅ Your issue has been submitted successfully!")
        st.balloons()
    else:
        st.error("⚠️ Please fill in all required fields before submitting.")
