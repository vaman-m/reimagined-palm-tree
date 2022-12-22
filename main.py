import speech_recognition as sr
import pyttsx3
import pandas as pd
import pyaudio


listener = sr.Recognizer()
engine = pyttsx3.init()


def queryDatabase(text):
    readCSV = pd.read_csv("dataOpen.csv")
    df = pd.DataFrame(readCSV)
    answer = df.loc[df['type'] == text]
    print(answer)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        listener.adjust_for_ambient_noise(source)
        print("Listening...")
        audio_data = listener.listen(source)
        # convert speech to text
        command = listener.recognize_sphinx(audio_data)
        print(command)
    readCSV = pd.read_csv("dataOpen.csv")
    df = pd.DataFrame(readCSV)
    products = list(df.type)
    sentence = list(command.split(" "))
    products = set(products)
    for x in sentence:
        if x in products:
            return x
    return command


if __name__=="__main__":
    intro = " Hi i am your assistant."
    intro_part2 = "What tool do you need? Please wait one moment before speaking"
    outro = "Here is the price and a link to the website for purchase"
    print(intro)
    talk(intro)
    print(intro_part2)
    talk(intro_part2)
    tool = take_command()
    queryDatabase(tool)
    talk(outro)
