import streamlit as st
import pandas as pd
import datetime
from utils import calculate_trends

# Title of the app
st.title("Mental Health Check-In")

# Create a session state to store user data
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Date", "Mood", "Sleep Hours", "Stress Level", "Feedback"])

# Input widgets
mood = st.selectbox("How are you feeling today?", ["Happy", "Sad", "Anxious", "Stressed", "Calm"])
sleep_hours = st.slider("How many hours did you sleep?", 0, 24, 7)
stress_level = st.slider("Rate your stress level (1-10)", 1, 10, 5)

# Button to submit
if st.button("Submit"):
    # Get the current date
    current_date = datetime.date.today()
    
    # Calculate feedback based on user input
    feedback = calculate_trends(mood, sleep_hours, stress_level)
    
    # Store the data in the session state DataFrame
    new_entry = {
        "Date": current_date,
        "Mood": mood,
        "Sleep Hours": sleep_hours,
        "Stress Level": stress_level,
        "Feedback": feedback
    }
    st.session_state.data = st.session_state.data.append(new_entry, ignore_index=True)
    
    # Display success message and feedback
    st.success("Thank you for checking in!")
    st.write(feedback)

# Display the user's check-in history
if st.session_state.data.shape[0] > 0:
    st.subheader("Your Check-In History")
    st.dataframe(st.session_state.data)

# Optionally, you can add a button to clear the history
if st.button("Clear History"):
    st.session_state.data = pd.DataFrame(columns=["Date", "Mood", "Sleep Hours", "Stress Level", "Feedback"])
    st.success("Your check-in history has been cleared.")
