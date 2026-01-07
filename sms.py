import requests

def send_sms(message):
    api_url = "https://webapp.usmsgh.com/api/sms/send"
    api_token = "your_api_key"

    headers = { 
                "Authorization": f"Bearer {api_token}",
                "Accept": "application/json",
            }

    data = {
        "recipient":"your_number",
        "sender_id":"your_id",
        "type":"plain",
        "message": message
    }

    resp = requests.post(api_url, headers=headers, json=data)
    # Uncomment for debugging to see the API response
    # print(resp.text)
