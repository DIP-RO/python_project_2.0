import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pyjokes
import time
def speech_recognition_for_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understood")
            return ""  # Return an empty string or any default value


def text_to_speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 100)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    if "alexa" in speech_recognition_for_text().lower():
        text_to_speech("hey i am  alexa , how can i help you")
        while True:
            data1 = speech_recognition_for_text().lower()
            if 'your name' in data1:
                name = "my name is alexa"
                text_to_speech(name)
            elif "about akash" in data1:
                akash = "akash akta motherchod"
                text_to_speech(akash)
            elif 'time' in data1:
                current_time = datetime.datetime.now().strftime("%H %M %p")
                text_to_speech(current_time)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            elif "joke" in data1:
                jokes = pyjokes.get_joke(language="en", category="neutral")
                text_to_speech(jokes)
            elif "exit" in data1:
                text_to_speech("Thank you")
                break
            time.sleep(2)
    else:
        print("Thank You")