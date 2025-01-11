import streamlit as st
from pymongo import MongoClient
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# Connect to MongoDB
# client = MongoClient("mongodb+srv://usdsc91:Vinhthuanly123@cluster0.ydtaq.mongodb.net/")
# db = client["usdsc91"]  # Your database name
# error_reports_collection = db["ErrorReportsDB"]  # The collection to store error reports

client = MongoClient("mongodb+srv://Prj_Python:Vinhthuanly123@cluster0.hlb6t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["Prj_python"]  # Your database name
error_reports_collection = db["ErrorReportsDB"]
# Email configuration (set your email and password)
sender_email = "botwse@gmail.com"
sender_password = "oguy sfyd bwzj mopj"
receiver_email = "vinhthuanly210@gmail.com"

# Function to send email notification
def send_email_notification(user_name, user_email, error_description, error_type):
    # Configure the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"[Error Report] New Error Report from {user_name}"

    # Email body content
    body = f"""
    A new error report has been submitted by {user_name}.
    
    Contact Email: {user_email}
    Error Type: {error_type}
    Error Description:
    {error_description}
    
    Please review the system for resolution.
    """
    msg.attach(MIMEText(body, 'plain'))

    # Sending the email via SMTP
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
    except Exception as e:
        st.error(f"Could not send email notification: {e}")

# Page configuration and layout
st.set_page_config(
    page_title="Error Report",
    layout="centered",
    page_icon="logo.jpg"
)
# Title for the Error Report page
st.title("Error Report")

# Instructions for the user on how to report an error
st.write("""
We strive to provide the best service. However, if you encounter any issues or errors while using our service, please provide detailed information about the issue so we can address it promptly.

We will review and respond as soon as possible.
""")

# Form for the user to submit error information
st.write("### Error Report Form:")

# Input fields for the user
user_name = st.text_input("Your Name")
user_email = st.text_input("Your Contact Email")
error_description = st.text_area("Describe the error you encountered")

# Dropdown to select the type of error
error_type = st.selectbox(
    "Select the type of error you encountered",
    ["UI Error", "Functionality Error", "Connection Error", "Data Error", "Other"]
)

# Submit button to send the report
if st.button("Submit Report"):
    if user_name and user_email and error_description:
        # Save the report into MongoDB
        report_data = {
            "name": user_name,
            "email": user_email,
            "description": error_description,
            "error_type": error_type,  # Include the type of error in the data
            "timestamp": st.session_state.get("current_time", time.time())
        }
        error_reports_collection.insert_one(report_data) 
        
        # Send email notification
        send_email_notification(user_name, user_email, error_description, error_type)

        # Show success message
        st.success(f"Thank you {user_name}, we have received your report and will process it soon.")
    else:
        st.error("Please fill in all required information.")
