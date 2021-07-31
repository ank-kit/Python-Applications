#5. Text to Speech

import pyttsx3​

frnd  = pyttsx3.init()​

name = input (' Please enter your name ')​

msg = "hello "+ name +". Welcome to bitLabs webinar session, Have a nice day!!"​

frnd.say(msg)​

frnd.runAndWait()​