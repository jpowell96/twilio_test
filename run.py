from flask import Flask, request
from twilio import twiml


#set up Flask to connect this code to the local host, which will
#later be connected to the internet through Ngrok
app = Flask(__name__)

#Main method. When a POST request is sent to our local host throh Ngrok
#(which creates a tunnel to the web), this code will run.  The twilio service # sends the POST request - we will se this up on the Twilio website.
#So when the # a message is sent over SMS to our Twilio number,  this code will run
@app.route("/", methods=['POST'])
def sms():
	#Get the text in the message sent
	message_body = request.form['Body']

	#Create a Twilio response obejct to be able to send a reply back (as per # Twilio docs)
	resp = twiml.Response()

	#Send the message body to the getReply message, where we will query the string and formulate
	#a response
	replyText = getReply(message_body)

	#Text back our response!
	resp.message('Hi\n\n' + replyText)

	return str(resp)
#Function to formulate a response based on message input.
def getReply(message):
	#1. make the message lower care and remove spaces at the end for easier handling
	message = message.lower().strip()
	return "This is a test. Does this work?"


# Function for editing input text. Ex: If you send the message "wolfram calories in bread", 
# the program will recognize "wolfram" and call this function and will 
# change the text to "calories in bread", which will then be sent to wolfram.
def removeHead(fromThis, removeThis):
    if fromThis.endswith(removeThis):
        fromThis = fromThis[:-len(removeThis)].strip()
    elif fromThis.startswith(removeThis):
        fromThis = fromThis[len(removeThis):].strip()
    
    return fromThis


if __name__ =='__main__':
	app.run(debug=True)