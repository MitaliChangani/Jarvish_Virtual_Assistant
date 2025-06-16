import speech_recognition as sr
import webbrowser
import pyttsx3


musicLibrary = {
    "stealth": "https://www.youtube.com/watch?v=U47Tr9BB_wE",
    "march": "https://www.youtube.com/watch?v=Xqeq4b5u_Xw",
    "skyfall": "https://www.youtube.com/watch?v=DeumyOzKqgI&pp=ygUHc2t5ZmFsbA%3D%3D",
    "wolf": "https://www.youtube.com/watch?v=ThCH0U6aJpU&list=PLnrGi_-oOR6wm0Vi-1OsiLiV5ePSPs9oF&index=21",
    "omjai":"https://youtu.be/rxajgk2TOPQ",
    "suzume":"https://youtu.be/qal34e9v_pk",
    "vraj":"https://youtu.be/epH1-UoJD1A",
    "khamma":"https://youtu.be/gTastlkWMFs",
    "unstoppable":"https://youtu.be/YaEG2aWJnZ8?list=RDQMgP_OCp3EMZc",
    "perfact":"https://youtu.be/2Vv-BfVoq4g?list=RDQMgP_OCp3EMZc",
    "waka waka":"https://youtu.be/pRpeEdMmmQ0?list=RDQMgP_OCp3EMZc",
    "believer":"https://youtu.be/7wtfhZwyrcc?list=RDQMgP_OCp3EMZc",
    "scar":"https://youtu.be/MWASeaYuHZo?list=RDQMgP_OCp3EMZc",
    "let me down slowly":"https://youtu.be/50VNCymT-Cs?list=RDQMgP_OCp3EMZc",
    "runaway":"https://youtu.be/Fc7XWW_Ehb8",
    "moral of the story":"https://youtu.be/WQq98YPV8yk",
    "princesses don't cry":"https://youtu.be/2tJjplMngFE",
    "alon":"https://youtu.be/HhjHYkPQ8F0",
    "dreamers":"https://youtu.be/jEdfjuG0Fx4",
    "dynamite":"https://youtu.be/gdZLi9oWNZg?list=RDEMI0V0e34vA6znf4KLMCIbbQ",
    "butter":"https://youtu.be/WMweEpGlu_U?list=RDEMI0V0e34vA6znf4KLMCIbbQ",
    "permission to dance":"https://youtu.be/CuklIb9d3fI?list=RDEMI0V0e34vA6znf4KLMCIbbQ",
    "fire":"https://youtu.be/4ujQOR2DMFM?list=RDEMI0V0e34vA6znf4KLMCIbbQ",
    "life gose on":"https://youtu.be/-5q5mZbe3V8?list=RDEMI0V0e34vA6znf4KLMCIbbQ",
    "seven":"https://youtu.be/QU9c0053UAU?list=RDEMI0V0e34vA6znf4KLMCIbbQ",
    "that that":"https://youtu.be/8dJyRm2jJ-U?list=RDEMI0V0e34vA6znf4KLMCIbbQ",
    "make ie right":"https://youtu.be/eXBu09fwe3I?list=RDEMI0V0e34vA6znf4KLMCIbbQ",
    "christmas evel":"https://youtu.be/57n4dZAPxNY?list=RDEMI0V0e34vA6znf4KLMCIbbQ",
    "deandline":"https://youtu.be/5gg17XXXiNo?list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbA",
    "despacito":"https://youtu.be/kJQP7kiw5Fk?list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbA",
    "die with smile":"https://youtu.be/zgaCZOQCpp8?list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbA",
    "cheap thrills":"https://youtu.be/31crA53Dgu0?list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbA",
    "middle of the night":"https://youtu.be/31crA53Dgu0?list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbA",
    "shape of you":"https://youtu.be/JGwWNGJdvx8?list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbA",
    "diamonds":"https://youtu.be/lWA2pjMjpBs?list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbA",
    "friends":"https://youtu.be/jzD_yyEcp0M?list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbA",
    "darkside":"https://youtu.be/M-P4QBt-FWw?list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbA",
    "on my way":"https://youtu.be/dhYOPzcsbGM?list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbA",
    "one kiss":"https://youtu.be/YaOlxgJHif0?list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbA",
    "until I found you":"https://youtu.be/GxldQ9eX2wo?list=RDGMEMQ1dJ7wXfLlqCjwV0xfSNbA",
    "night changes":"https://youtu.be/syFZfO_wfMQ",
    "left and right":"https://youtu.be/a7GITgqwDVg",
    "3D":"https://youtu.be/Z3x9i7njCCo",
}

recognizer = sr.Recognizer()
engine = pyttsx3.init() 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.get(song)
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))