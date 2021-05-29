# Imported Modules
import datetime
import webbrowser
import os


# Functions

def Greet():
    # Greeting Logic
    Hour = int(datetime.datetime.now().hour)
    if Hour>=0 and Hour<12:
        print("Good Morning Sir!")

    elif Hour>=12 and Hour<16:
        print("Good Afternoon Sir!")

    else:
        print("Good Evening Sir!")
    print('I am SAM how may I help you')

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
            print("Okay Sir")
            break

        elif user_command.lower() in IdeCommands:
            print("Opening Visual Studio Code, Sir")
            codepath = "E:\\Microsoft VS Code\\Code.exe" #Path Where VS Code is install
            os.startfile(codepath)

        elif user_command.lower() in MusicCommands:
            print("Playing Music..")
            MusicDirectory = "E:\\Songs" #Path to the songs directory
            Songs = os.listdir(MusicDirectory)
            os.startfile(os.path.join(MusicDirectory, Songs[-1]))
        
        elif user_command.lower() in BrowserCommand:
            print("Opening Browser...")
            webbrowser.open("google.com")

        else:
            print("Sorry Sir, but plaese write a valid command")

