# This project try to use voice recognition system from Google in order to improve speaking skills when you are not able to practice with another person. 
# The idea is to use AI to solve one of the most commons problems english learner used to face. 
# This is just an starting point and is open to any improvement. 
# This is part of Building AI course project.
# Convert speech to text accurately with an API based on the Google AI technologies and research.
# New customers receive $300 in free credit to use on Speech-to-Text.
# In addition, all customers have 60 free minutes per month
# to transcribe and analyze audio, and are not deducted from your credit.
# https://cloud.google.com/speech-to-text
# To use another API key, use r.recognize_google(audio, language='en-US', show_all=False, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")

import speech_recognition as sr
import os
r = sr.Recognizer()
while True:
	with sr.Microphone() as source:
    		print("Say Something...")
    		audio = r.listen(source)
	try:
		text = r.recognize_google(audio, language='en-US', show_all=False)
		print("You said: {}".format(text))
	except:
		print("I am sorry! I can not understand!")
	break
os.system('voz.py')
	