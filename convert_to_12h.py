from datetime import datetime

def convert_24h_to_12h(time_24h_str):
    """
    Converts a 24-hour time string (e.g., "14:30") to a 12-hour format 
    with AM/PM (e.g., "02:30 PM").
    """
    try:
        # Parse the 24-hour time string into a datetime object
        time_obj = datetime.strptime(time_24h_str, "%H:%M")
        
        # Format the datetime object to a 12-hour string with AM/PM
        time_12h_str = time_obj.strftime("%I:%M %p")
        
        return time_12h_str
    except ValueError:
        return "Invalid time format. Please use HH:MM."