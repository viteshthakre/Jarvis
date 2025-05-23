import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
   engine = pyttsx3.init('sapi5')
   voices = engine.getProperty('voices')
   engine.setProperty('voice', voices[1].id)
   engine.setProperty('rate', 174)   
   eel.DisplayMessage(text)  
#    print(voices)
   engine.say(text)
   engine.runAndWait()



def takecommand():
        r=sr.Recognizer()
      
        with sr.Microphone() as source:
            print('listening....')
            eel.DisplayMessage('listening....')
            r.pause_threshold=1;
            r.adjust_for_ambient_noise(source)
            
            audio = r.listen(source, 10, 6)
            
        try:
            print('recognizing')
            eel.DisplayMessage('recognizing....')
            query = r.recognize_google(audio,language='en-in')
            print(f"user said: {query}")
            eel.DisplayMessage(query)
            time.sleep(2)
            # speak(query)
            
        except Exception as e:
            return  ""   
          
        return  query.lower()
# text = takecommand()
# speak(text)  

@eel.expose

def allCommands():
    
    query = takecommand()
    print(query)
    
    if "open" in query:
        from engine.features import openCommand
        openCommand(query)
    elif "on yputube":  
        from engine.features import PlayYoutube
        PlayYoutube(query)
    else:
         print("not run")   
         
    eel.ShowHood()     