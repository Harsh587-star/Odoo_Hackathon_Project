import streamlit as st
from aquapulse_core import drainlink

# Page setup
st.set_page_config(page_title="🛠️ Admin Dashboard", layout="wide")

# Header section
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 40px;'>🛠️ Admin Dashboard</h1>
        <p style='font-size: 20px; max-width: 850px; margin: 0 auto;'>
            Here you can view a live summary of all submitted drainage issues categorized by type. 
            Use this data to identify problem trends and plan better drainage responses. 📊🚧
        </p>
    </div>
    <hr style='margin-top: 25px; margin-bottom: 30px;'>
""", unsafe_allow_html=True)

# Database connection
conn = drainlink.get_connection()
cursor = conn.cursor()
cursor.execute("SELECT category, COUNT(*) FROM issues GROUP BY category")
data = cursor.fetchall()

# Display stats
if data:
    for cat, count in data:
        st.markdown(f"""
            <div style='margin-bottom: 20px;'>
                <h3 style='font-size: 26px;'>📌 {cat}</h3>
                <p style='font-size: 18px;'>🗂️ Total Reports: <b>{count}</b></p>
                <hr style='margin-top: 10px;'>
            </div>
        """, unsafe_allow_html=True)
else:
    st.warning("😕 No reports found. The database might be empty.")
