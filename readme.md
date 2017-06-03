  _____  ______          _____  __  __ ______ 
 |  __ \|  ____|   /\   |  __ \|  \/  |  ____|
 | |__) | |__     /  \  | |  | | \  / | |__   
 |  _  /|  __|   / /\ \ | |  | | |\/| |  __|  
 | | \ \| |____ / ____ \| |__| | |  | | |____ 
 |_|  \_\______/_/    \_\_____/|_|  |_|______|
 

 This is a small test app using Twilio to respond to a text message, it was built using the
 tutorial found at this link on Make Magazine:

 http://makezine.com/projects/sms-bot/

 This README explains how to run this locally, the link in the tutorial provides instructions as well.

 Dependencies:
 virtualenv
 ngrok

 virtualenv can be installed using "pip install virtualenv"

 Ngrok can be installed from here:
 https://ngrok.com/




 To run locally:

 1. From the twilio_test_app directory run
 	Scripts\activate
 	This opens the virtual environment
 2. python run.py
 	This command will list the a port number. It's typically 5000

 3. In another shell run the following command:
 	ngrok http <PORT NUM>

4. In the Twilio online console. Go to the Twilio number you'd like to use and click on it. On the Messaging dashboard paste the URL of the forwarding address that appears in your ngrok window.
The address will look similar to this:
		http://6eeb0590.ngrok.io
5. You can now send texts to the number and get a reply!
