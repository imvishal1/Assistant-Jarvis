# MODULES AND LIBRARIES IMPORTED FOR THE PROJECT

import pyttsx3 # USE FOR TEXT TO SPEECH CONVERSION
import datetime # USE FOR FETCHING DATE AND TIME FROM THE SYSTEM
import speech_recognition as sr # USE TO RECOGNISE USER VOICE
import wikipedia # USED TO FETCH THE INFORMATION FROM WIKIPEDIA
import webbrowser # USED TO CONTROL BROWSER OPERATIONS
import os # USED TO FETCH FILES ALREADY EXITS IN THE SYSTEM
import random # USED TO GENERATE RANDOM NUMBERS
import pyjokes # USED FETCH JOKES ALREADY EXITS IN THE PYTHON MODULES
import wolframalpha # USED TO CALCULATE MATHS PROBLEMS
import subprocess # USED TO CONTROL POWER FUNCTIONS IN THE SYSTEM(LIKE, SHUTDOWN,RESTART,HIBERNATE etc.)

# initializes the voices
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)

# speaks the audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wish Me Function
def WishMe():
    wishHour = int(datetime.datetime.now().hour)
    if wishHour>=0 and wishHour<12: 
        speak("Good Morning Vishal!")
        speak("and Good Morning all of you who are listening me!! ")

    elif wishHour>=12 and wishHour<18: 
        speak("Good Afternoon Vishal!")
        speak("and Good Afternoon all of you who are listening me!! ")

    else:
        speak("Good Evening Vishal!")
        speak("and Good Evening all of you who are listening me!! ")

    speak("I m jarvis! Please tell me what to do!")
    speak("Are you here Vishal!!")


# Taking the Microphone Input from the User

def Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    #this block will recognise the your voice
    try:
        print("Recognizing...")
        input = r.recognize_google(audio,language="en-in")
        print("you said:",input)
        
    except Exception as e:
        # print(e)
        # print("Please Say it Again Sir...")
        return "none"
    return input

# TIME FUNCTION

def Time():
    get_Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(get_Time)

# DATE FUNCTION

def Date():
    get_year = int(datetime.datetime.now().year)
    get_month = int(datetime.datetime.now().month)
    get_day = int(datetime.datetime.now().day)
    speak("Today's date is " + str(get_day))
    speak("july")
    speak(get_year)

# SEARCH ANYHING FROM WIKIPEDIA
# JARVIS WILL READ THE LINES FROM WIKIPEDIA 

def Search_wikipedia():
    global input, result
    speak("searching from wikipedia...")
    input = input.replace("wikipedia","")
    result = wikipedia.summary(input,sentences=2)
    speak("According to wikipedia, here I got this for you")
    speak(result) 

# MAIN FUNCTION WHERE THE EXECUTION OF THE CODE STARTS

if __name__ == "__main__":
    WishMe()
    while True:
        input = Command().lower()

        # SOME IF AND ELIF STATEMENTS

        if 'wake up' in input:
            speak("I m already waked up, Vishal!, What about you!")

        elif "i am here" in input:
            speak("Ok Vishal!! Glad to hear you!!")

        elif "ok" in input:
            speak("ok!! Thank you Vishal!!")
            speak("and please let me know if you have any qurries!! i will try to remove them!!")
        
        elif "what can you do" in input:
            speak("I can perform many functions Vishal!! Like I can open any application for you!! And also I can search for anything!!")
        
        elif 'hello' in input:
            WishMe()
        
        elif 'time' in input:
            speak(Time())

        elif 'date' in input:
            speak(Date())

        elif "define yourself" in input:
            speak("Thank you sir for giving me this opportunity to introduce myself!!")
            speak("So!! My boss Vishal, calls me jarvis.. i am a Virtual Assisstant of my boss Mr. Vishal!!")
            speak("And I am here to make my boss life easier!!")
        
        elif 'Priti Mam' in input:
            speak("Hello Priti Mam! How are you! You are doing a great job!! My boss admires you")

        elif 'who are you' in input:
            speak("i m mr. Vishal's assisstant!! and I m here to make my boss life easier")
        
        elif "who created you" in input:
            speak("I am created by Mr. Vishal for his project!!")
        
        elif "how are you" in input:
            speak("I m fine Vishal, Glad to hear you! What about you!")

        elif "i am fine" in input:
            speak("Ok that's great, please command me to do something for you!!")

        elif "i love you" in input:
            speak("I love you too Vishal!! But dont understand what actually love is!! please explain me!!")

        elif "leave it"in input:
            speak("Ok Vishal!!")

        elif "thank you" in input:
            speak("No Problem Vishal!! Enjoy!!")

        elif 'wikipedia' in input:
            Search_wikipedia()

        elif 'youtube' in input or "songs" in input:
            speak("Opening in youtube")
            song = input.replace("songs", "")
            webbrowser.open("https://www.youtube.com/?#q=" + song)


        elif 'open face' in input:
            speak("here is the facebook Home Page")
            webbrowser.open("https://www.facebook.com")

        elif "overflow" in input:
            speak("Opening StackOverFlow")
            webbrowser.open("https:\\www.stackoverflow.com")

        elif 'facebook messages' in input:
            speak("I m opening the facebook sir! please check your messages!")
            webbrowser.open("https:\\www.facebook.com")

        elif 'instagram messages' in input:
            speak("I m Opening Your Instram Account! Please Check!")
            webbrowser.open("https:\\www.instagram.com")

        elif "google" in input:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "chrome" in input:
            speak("Ok Sir!! Opening Google Chrome!!")
            chrome_path = "C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)

        elif 'mails' in input:
            speak("I think you have got many mails! please check! Should I open your mails Sir!!")

        elif 'open my mails' in input:
            webbrowser.open("https:\\www.gmail.com")
        
        elif "wiki" in input:
            speak("Opening Wikipedia Sir!!")
            webbrowser.open("www.wikipedia.com")

        elif 'music' in input:
            speak("Ok Sir!!, listen this one!!")
            song_directory = "D:\\Songs\\Mr Vishal Songs"
            songs = os.listdir(song_directory) #TOOK UP ALL THE SONGS
            os.startfile(os.path.join(song_directory,songs[random.randint(0,45)]))
        
        elif "change music" in input: # change the music
            speak("Ok sir, How's this!!")
            os.closefile(os.path.join(song_directory,songs[random.randint(0,45)]))

        elif "jokes" in input:
            speak(pyjokes.get_jokes())

        elif 'search' in input or 'play' in input: 

            speak("Searching as you said " + input)  
            query = input.replace("search", "")  
            query = input.replace("play","")           
            webbrowser.open("https://www.google.com/?#q=" + query)  

        elif 'exit' in input:
            speak("Ok bye Shaan! I m going!! please take care!")
            break  

        elif "calculate" in input:

            app_id = "E9VQAV-PEKV8J37RW" 
            client = wolframalpha.Client(app_id) 
            indx = input.split().index('calculate')  
            query = input.split()[indx + 1:]  
            res = client.query(' '.join(query))  
            answer = next(res.results).text 
            print("The answer is " + answer)  
            speak("The answer is " + answer)

        # THESE ELIFS STATEMENTS WILL TURN OF YOU SYSTEMS

        elif "shutdown my computer" in input:
            speak("please wait for a minute!!") 
            subprocess.call('shutdown / p /f') 

        elif "hibernate" in input:
            speak("Please wait for a minute!!")
            subprocess.call('hibernate / p /f')
        
        elif "sleep" in input:
            speak("Please wait for a minute!!")
            subprocess.call('sleep / p /f')
        
        elif "restart" in input:
            speak("wait for a minute!!")
            subprocess.call('restart / p /f')

        # THESE COMMANDS TO OPEN ALL MICROSOFT OFFICE

        elif "word" in input:
            speak("Opening microsoft office word!!")
            word_path = "C:\\Program Files\\WindowsApps\\Microsoft.Office.Desktop.Word_16051.12624.20466.0_x86_8Wekyb3d8bbwe\\Office16\\WINWORD.exe"
            os.startfile(word_path)

        elif "excel" in input:
            speak("opening Microsoft Excel")
            excel_path = "Mention the excel file path"
            os.startfile(excel_path)

        elif "powerpoint" in input:
            speak("opening Microsoft powerpoint")
            powerpoint_path = "Mention the powerpoint file path"
            os.startfile(powerpoint_path)

        elif "services" in input:
            speak("Searching as you said " + input)  
            query = input.replace("services", "")            
            webbrowser.open("https://www.youtube.com/results?search_query" + query)  
