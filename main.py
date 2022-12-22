import speech_recognition as sr
import pyttsx3
import pandas as pd
import pyaudio
import sounddevice

listener = sr.Recognizer()
engine = pyttsx3.init()


def queryDatabase(text):
    readCSV = pd.read_csv("D:\DC\dataOpen.csv")
    df = pd.DataFrame(readCSV)
    answer = df.loc[df['Type'] == text]
    print(answer)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        listener.adjust_for_ambient_noise(source, duration=2)
        print("Listening...")
        audio_data = listener.record(source, duration=5)
        # convert speech to text
        command = listener.recognize_google(audio_data)
        print(command)
    products = ['Rake', 'Shovel', 'Pickaxe', 'Machete','Wheelbarrow','Pick-mattock','Pitchfork','Pruning shears','(Aku) Chainsaw','Sprinkler','Sprayers','Tractor','Cultivator','Harvester','Set of harrows','Fertilizer/Seeder','Agricultural roller','Baler','Plough']
    sentence = list(command.split(" "))
    products = set(products)
    for x in sentence:
        if x in products:
            return x
    return command


if __name__=="__main__":
    intro = " Hi i am your assistant."
    krithik = "What tool do you need?"
    print(intro)
    talk(intro)
    print(krithik)
    talk(krithik)

    tool = take_command()
    queryDatabase(tool)