🌧️ FloodTrack – Smart Drainage & Flood Issue Reporting System
🚀 Developed for:
Odoo x CGC Hackathon 2025
Problem Statement 2: “Drainage and Monsoon Flood Mapping”

Problem: Monsoon floods due to choked drains or improper slope planning.
Feature Idea: Citizens report blocked drains, water logging, stagnant water.
Advanced Add-on: GIS mapping of drainage problem-prone zones with history logs.
Impact: Data helps municipal bodies plan better drainage in monsoon.

🧠 Project Overview:
FloodTrack is a smart, citizen-driven flood and drainage reporting system that allows real-time reporting, mapping, and 
monitoring of monsoon-related civic issues. Designed specifically for monsoon-prone cities, the app helps residents report problems like:

🚫 Blocked drains

🌊 Waterlogging

💧 Stagnant water areas

These reports are visualized on a live flood map, creating a powerful geo-database of flood-prone zones. 
The platform enables civic bodies to analyze drainage patterns, identify hotspots, and respond faster using real-time data.

🛠️ Key Features:
📋 Report Interface: Citizens can report issues using a simple, interactive form (title, category, location, photo upload).

📍 Flood Map: All reports are visualized using GIS-style markers on a Folium-based map.

📬 Submission Tracker: Users can track past submissions by email.

🛠️ Admin Dashboard: View report count per category for civic monitoring.

🖼️ Image Uploads: Optional image proof is stored for visual validation.

📦 MySQL Database Integration: All data is stored and fetched from a relational database.

💡 Why It Matters:
Empowers local communities to take part in civic problem-solving

Reduces manual survey burden for authorities

Creates a historical data trail for predictive flood response

Bridges communication between citizens and municipalities during monsoon

💻 Tech Stack Used:
Layer	Technology
Frontend	🧩 Streamlit (Python) for UI
Backend	🔗 Python + Custom modules
Database	🗄️ MySQL
Map Layer	🌍 Folium + Streamlit-Folium
File Uploads	🖼️ Stored in local directory (basin_bucket/)
Project Structure	Modular with folders: aquapulse_core, downpour_routes, pages, etc.
Testing	✅ Sample input scripts via aqua_testlab

🔍 How It Works (Workflow):
📥 User opens the app and selects "Report an Issue"

📝 Fills in the form (title, category, lat/lon, email, image)

💾 Data gets stored in users, issues, and images tables

🗺️ Issue appears on the live Flood Map

📬 User can track their own issues via My Submissions

🛠️ Admin views report categories for analytics & intervention

📈 Future Scope:
🌐 Integration with Google Maps API for real-world overlays

📱 Mobile-friendly PWA or Android version

📊 Advanced analytics dashboard for municipality insights

📍 Real-time notification system for emergency alerts

🛰️ GIS shapefile support for ward-wise or city-sector overlays
