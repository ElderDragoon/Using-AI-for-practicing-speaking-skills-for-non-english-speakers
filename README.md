# Using AI for practicing speaking skills for non-english speakers


## Summary

This project try to use voice recognition system from Google in order to improve speaking skills when you are not able to practice with another person.
The idea is to use AI to solve one of the most commons problems english learner used to face.
This is just an starting point and is open to any improvement.
This is part of Building AI course project.


## Background

Which problems does our idea solve? How common or frequent is this problem?
Usually practicing speaking is the most dificult situation for non-english speakers, many times because there are not anybody to practice with.
With this project the idea is bring the opportunity to practice speaking even if you are alone.

Why is this topic important or interesting?
If your computer can understand you, probably you are doing well and anyone will understand you.
The system will recognice your voice and will tell you what it is understanding.


## How is it used?

Using the solution is quite easy, you just need to copy the file on your PC and run it.
Who are the users, what kinds of needs should be taken into account? Well, basically any non-english speaker are welcome


## Data sources and AI methods

Where does our data come from? Do we collect it by ourselves or do we use data collected by someone else?

We convert speech to text accurately with an API based on the Google AI technologies and research.
[Google API] (https://cloud.google.com/speech-to-text)
So, as you can imagine, we send all data to Google in order to be processed
The API can be used for free. New customers receive $300 in free credit to use on Speech-to-Text. In addition, all customers have 60 free minutes per month to transcribe and analyze audio, and are not deducted from your credit.
We are using the testing (default) API Key, to use another API key, use r.recognize_google(audio, language='en-US', show_all=False, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")


## Challenges

What does our project _not_ solve?
The project try to be just a starting point for more complex projects.


## What next?

How could our project grow and become something even more?
The project can grow in many ways:
The system can be optimized using different APIs.
We could add a graphical user interface.
We could avoid the use of an external API.
We could improve the system creating more modules for improve reading, listening and writing skills.
The system can be addapted to practice any other language.
The system can be integrated in any other teaching method.


## Acknowledgments

Thanks to University of Helsinki
