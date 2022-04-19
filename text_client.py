from twilio.rest import Client
import data.info as info

def send_text(body):
    client = Client(info.TWILIO_SID, info.TWILIO_AUTH)
    
    return client.messages.create(
                            from_=info.TWILIO_PHONE_NUM,
                            to=info.USER_PHONE_NUM,
                            body=body)
