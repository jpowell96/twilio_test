from twilio.rest import TwilioRestClient

#Find these values at https://twilio.com/user/account
account_sid = "ACed19bd268a8ec4be1cae0d9977001a54"
auth_token = "04a9b8eff4ed40e6baff5adf924f88ea"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+14048399132", from_= "+16784985016", 
	body="Hey, Patricia is the best!!!")