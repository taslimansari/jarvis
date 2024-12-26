import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests
import cohere
from gtts import gTTS
import pygame
import os

# recognizer object
r = sr.Recognizer()
engine = pyttsx3.init()
newsapi="4cab6b21390546bf82ccf155fe4f6748"

def speak_old(text):
    engine.say(".....Initializing Jarvis")
    engine.runAndWait()
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts=gTTS(text)
    tts.save("temp.mp3")

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")  

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running so the music can play
    while pygame.mixer.music.get_busy():  # Check if music is still playing
        pygame.time.Clock().tick(10)  # Wait and continue checking if music is playing
    pygame.mixer.music.unload() 
    os.remove('temp.mp3')


def aiProcess(command):
    co = cohere.Client("LVwy0jXt62EqxQ5pSpwDrW1rrL6EPAY4TZL4mkxg")  # Replace with your API key

    # First prompt
    response1 = co.generate(
        model="command-xlarge-nightly",
        prompt="You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please!",
        max_tokens=50
    )
    print("Response 1:")
    print(response1.generations[0].text)

    # Second prompt
    response2 = co.generate(
        model="command-xlarge-nightly",
        prompt=command,
        max_tokens=50
    )
    print("\nResponse 2:")
    return response2.generations[0].text


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open netflix" in c.lower():
        webbrowser.open("https://www.netflix.com/browse")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ", 1)[1]
        if hasattr(musicLibrary, "music") and song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song} in the library.")
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        # Fetch data from the API
        response = requests.get(r)
        if response.status_code == 200:
            data = response.json()  # Parse JSON response
            # Check if there are articles in the response
            if "articles" in data:
                articles = data["articles"]
                speak("Top Headlines:")
                # Loop through and speak the headlines
                for i, article in enumerate(articles):
                    speak(f"{i+1}. {article['title']}")
            else:
                speak("No articles found.")
        else:
            speak(f"Failed to fetch news. Status code: {response.status_code}")
    else:
        # let open ai handle the requests
        output = aiProcess(c)
        print(output)
        speak(output)

if __name__ == "__main__":
    speak("I am your assistant Jarvis. I am trained to help you in any questions that you may ask......")
    while True:
        # Listen for the word "Jarvis" to wake the system up
        # obtain audio from the microphone
        # recognize speech using Google
        print("Recognizing audio...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Go ahead!!")
                # listen for command
            with sr.Microphone() as source:
                print("Jarvis Activated...")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                print(command)
                processCommand(command)

        except sr.UnknownValueError:
            print("Jarvis could not understand audio")
        except sr.RequestError as e:
            print("Error; {0}".format(e))
