from twilio.rest import Client
import pyotp

totp = pyotp.TOTP('base32secret3232', interval=35)

def generate_otp(phone):
    t = totp.now()
    phoneno = str('+91')+str(phone)
    # the following line needs your Twilio Account SID and Auth Token
    client = Client("AC8e7ebb0968e6be74705ba77e4d93c62d", "2c86241cfeb729ca144125287044ac0e")
    # change the "from_" number to your Twilio number and the "to" number
    # to the phone number you signed up for Twilio with, or upgrade your
    # account to send SMS to any phone number
    client.messages.create(to=phoneno, from_="+12512025176", body="OTP for Skillhunt: {}".format(t))
    return True

def verify_otp(votp):
    print(votp, type(votp))
    if len(votp) == 5:
        votp = '0'+ votp
    b =  totp.verify(votp)
    print(b, type(b))
    if b:
        return True
