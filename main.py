from fxscraper import get_today_events
from sms import send_sms

def main():

    # Attempt to fetch today's events
    try:
        events = get_today_events()
    except Exception as e:
        # If scraping fails, notify via SMS
        message = "Error fetching economic news."
        send_sms(message)
        return
    
     # Handle case where there are no high-impact events today(events is empty)
    if not events:
        message = "No high-impact news today."
        send_sms(message)
        return
    
    # Build SMS message content
    message_lines = ["High Impact Forex Events Today:\n"]

    for event in events:
        line = f"{event['currency']} - {event['event']} at {event['time']}"
        message_lines.append(line)

    final_message = "\n".join(message_lines)
    # print(final_message)

    # Send SMS
    try:
        send_sms(final_message)
        # print("SMS sent successfully.")
    except Exception as e:
        print(f"Error sending SMS: {e}")

# Ensures this file only runs when executed directly
if __name__ == "__main__":
    main()
