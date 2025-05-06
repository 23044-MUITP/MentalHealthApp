def calculate_trends(mood, sleep_hours, stress_level):
    # Simple feedback logic
    if sleep_hours < 6:
        return "Consider getting more sleep for better mental health."
    elif stress_level > 7:
        return "It might be helpful to talk to someone about your stress."
    else:
        return "You're doing well! Keep it up!"
