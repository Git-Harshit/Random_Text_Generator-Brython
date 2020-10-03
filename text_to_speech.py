# this file is for the referance and the code has been intigrated into the main file(brython_script.bry)

# importing stuff for speech
import pyttsx3
import speech_recognition as sr
from difflib import SequenceMatcher

# defining voice and engine

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # index 0 is for female voice and 1 is for male voice

# defining module for speaking

def speak(audio):
    engine.say(audio)
    break
    
