With this project, I was aiming to recognize user's voices and do some quick tasks so that users don't have to do those things manually like searching for something on Google or searching for a product on Amazon, or even opening Youtube. All these things, just by voice command. I implemented this using Google's SpeechRecognition library in python to convert the recognized voice in the text to operate on that and save all the conversations in a .txt file for later research purposes. I also used Playsound library in python to give the virtual assistant a voice. Each reply by Friday is first converted from text to a .mp3 file using gTTs (Google's Text to Speech library) and then played out using the Playsound library, which gives it the essence of a human talking back.

Here is a list of libraries that you need to install first
SpeechRecognition
gTTs
Playsound
Pyaudio
Webbrowser
