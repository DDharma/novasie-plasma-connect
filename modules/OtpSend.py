from twilio.rest import Client
import random

def optSender(mob):
    # Your Account Sid and Auth Token from twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid ='AC7b424e70120299d5bed11730a2b33782'
    auth_token = '9af5cbd5bd4ff219f2b7204789c7f1ff'
    client = Client(account_sid, auth_token)

    OtpNo = random.randint(1000,9999)
    MonNo = "+91"+mob
    data = {
        "OTP_NO" : OtpNo,
        "MobNo"  : mob,
        "Msz"    : "Your OTP in for Mob no verification is"+str(OtpNo)
    }

    message = client.messages \
                    .create(
                        body="Your OTP in for Mob no verification is"+str(OtpNo),
                        from_='+12159874586',
                        to= MonNo
                    )
    
    return data