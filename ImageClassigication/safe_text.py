from twilio.rest import Client

account_sid = 'SK27b1f561024d6e29717675705635b04e'
auth_token = '3j5gyRluxFDz0aUgxEJXo10GfMKqR9Lw'

client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+14163473761'
)

print(message.sid)