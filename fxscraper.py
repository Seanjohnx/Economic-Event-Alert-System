from bs4 import BeautifulSoup
import requests
import datetime
import convert_to_12h

# Stores all high-impact events happening today
TODAY_EVENTS = []

def get_today_events():

    """
    Scrapes MyFxBook economic calendar and returns
    today's high-impact economic events.
    """
    # Get current date/time as a formatted string
    current_datetime = datetime.datetime.now()
    current_datetime_str = current_datetime.strftime("%c")

    fx_url = "https://www.myfxbook.com/forex-economic-calendar"

    # Fetch the webpage
    response = requests.get(fx_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Economic events are inside the table body
    table = soup.find('tbody')

    # Loop through each event row
    for table_row in table.find_all('tr', class_='economicCalendarRow'):

        table_data = table_row.find_all('td', class_='calendarToggleCell')

        # Impact level (High)
        impact = table_data[5].div.text.strip()

        # Raw date text example: "Jan 06, 00:00"
        raw_date_text = table_data[0].div.text.strip()

        # Split date and time → ["Jan 06", " 00:00"]
        date_part = raw_date_text.split(',')[0]

        # Split month and day → ["Jan", "06"]
        month_day_parts = date_part.split()

        # Remove leading zero from day ("06" → "6")
        day_without_zero = month_day_parts[1].lstrip('0')

        # Rebuild date as "Jan  6"
        # (two spaces to match strftime("%c") formatting)
        normalized_date = f"{month_day_parts[0]}  {day_without_zero}"

        # Debug output (can be removed later)
        # print(normalized_date, current_datetime_str)
        
        # check if high impact and event happens today
        if impact == 'High' and normalized_date in current_datetime_str:

            # Extract event details
            currency = table_data[3].text.strip()
            event_name = table_data[4].a.text.strip()
            
            # Extract time portion and convert to 12-hour format
            raw_time_text = table_data[0].text.strip()
            time_24h = raw_time_text.split(',')[1].strip()
            time_12h = convert_to_12h.convert_24h_to_12h(time_24h)

            # Store event details
            TODAY_EVENTS.append({
                "time": time_12h,
                "currency": currency,
                "event": event_name
            })
    # Debug output (can be removed later)
    print(TODAY_EVENTS)

    return TODAY_EVENTS

# Run function (for testing)
get_today_events()
