from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC6c237577ea70de1b282b5db007aba25d'    #'ACfaf19e50106cf31c26720bf65382be0b'
auth_token = '846ac3bae27fa6635e99550dc97d2bd5'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'],
                              from_='whatsapp:+14155238886',
                              body='Hello, test in progrss!',
                              to='whatsapp:+919860907348'
                          )
print(message.sid)
print(message.media._uri)