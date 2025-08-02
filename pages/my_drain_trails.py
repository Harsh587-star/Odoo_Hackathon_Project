import streamlit as st
from aquapulse_core import drainlink

# Page setup
st.set_page_config(page_title="📂 My Submissions", layout="centered")

# Page title and instructions
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 40px;'>📂 My Reported Issues</h1>
        <p style='font-size: 20px; max-width: 800px; margin: 0 auto;'>
            Enter your registered email address below to view your past issue reports. You’ll see details like title, status, and submission time. 📬🧾
        </p>
    </div>
    <hr>
""", unsafe_allow_html=True)

# Input email
email = st.text_input("📧 Enter your email to fetch reports", help="Make sure to enter the same email you used during submission.")

# Fetch and display reports
if email:
    conn = drainlink.get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT title, description, status, timestamp 
        FROM issues i 
        JOIN users u ON i.user_id = u.user_id 
        WHERE u.email = %s
    """, (email,))
    data = cursor.fetchall()

    if data:
        for idx, (title, desc, status, ts) in enumerate(data, 1):
            st.markdown(f"<h3 style='font-size: 26px;'>📝 {idx}. {title}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 18px;'>🗒️ <b>Description:</b> {desc}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 18px;'>📅 <b>Reported On:</b> {ts}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 18px;'>🔖 <b>Status:</b> <code>{status}</code></p>", unsafe_allow_html=True)
            st.markdown("<hr style='margin-top: 10px; margin-bottom: 25px;'>", unsafe_allow_html=True)
    else:
        st.warning("😕 No issues found for the provided email. Try again or make sure the email is correct.")
