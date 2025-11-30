import speech_recognition as sr
import pyttsx3

sr = sr.Recognizer()
engine = pyttsx3.init() 
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change index for different voices
engine.say("Hello, how can I assist you today?")
engine.runAndWait()
with sr.Microphone() as source:
    print("Listening...")
    audio = sr.listen(source)
    try:
        text = sr.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
engine.say("You said: " + text)
engine.runAndWait()
