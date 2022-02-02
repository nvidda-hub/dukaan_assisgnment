from twilio.rest import Client



def sendOTP(mobile, otp):
    account_sid = 'ACa784c1bde9531f25e8bc5acea82a5008'
    auth_token = 'c7fc3eb75ea7fe7a922b9b4d3563fa78'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=f'your OTP is {otp} for djnago app!',
            from_='+18593282852',
            to=f'+91{mobile}'
        )

    return message.sid