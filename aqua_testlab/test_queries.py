from aquapulse_core.drainlink import get_connection

try:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    print("Connected! Tables in DB:", cursor.fetchall())
    cursor.close()
    conn.close()
except Exception as e:
    print("Database test failed:", e)
