# Imported Modules
from win32com.client import Dispatch
import datetime
import webbrowser
import os

# Functions
def Speak(str):
    speak = Dispatch('SAPI.SpVoice')
    print("Computer: ", str)
    speak.Speak(str)
def Greet():
    # Greeting Logic
    Hour = int(datetime.datetime.now().hour)
    if Hour>=0 and Hour<12:
        Speak("Good Morning Sir!")

    elif Hour>=12 and Hour<16:
        Speak("Good Afternoon Sir!")

    else:
        Speak("Good Evening")
    Speak('I am SAM, how may I help you')

if __name__ == '__main__':
    Greet()
    # Command Lists 
    BrowserCommand = ['open browser', 'open webbrowser', 'open web browser']
    IdeCommands = ['open code', 'open vs code', 'open visual studio code']
    MusicCommands = ['play songs', 'play music']
    ExitCommands = ['exit', 'quit', 'sleep', 'switch off']

    
    while True:
        user_command = input("User: ")

        if user_command.lower() in ExitCommands:
            Speak("Okay Sir")
            break

        elif user_command.lower() in IdeCommands:
            Speak("Opening Visual Studio Code, Sir")
            codepath = "E:\\Microsoft VS Code\\Code.exe" #Path Where VS Code is install
            os.startfile(codepath)

        elif user_command.lower() in MusicCommands:
            Speak("Playing Music..")
            MusicDirectory = "E:\\Songs" #Path to the songs directory
            Songs = os.listdir(MusicDirectory)
            os.startfile(os.path.join(MusicDirectory, Songs[-1]))
        
        elif user_command.lower() in BrowserCommand:
            Speak("Opening Browser...")
            webbrowser.open("google.com")
        else:
            Speak("Sorry Sir, but plaese write a valid command")