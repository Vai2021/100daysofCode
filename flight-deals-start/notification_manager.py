from twilio.rest import Client

TWILIO_SID = "add_your_sid"
TWILIO_AUTH_TOKEN = "add_your_token"
TWILIO_VIRTUAL_NUMBER = "number"
TWILIO_VERIFIED_NUMBER = "receiver"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_msg(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
