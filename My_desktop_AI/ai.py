import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime as datetime
import wikipedia 

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
   engine.say(text)
   engine.runAndWait()


def take_command():
  try:
      with sr.Microphone() as source:
        print('Listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        
        if 'lisa' in command:
         engine.say(command)
         engine.runAndWait()
         print(command)
  except:
     pass
  return command

def run_lisa():
   command = take_command()
   print(command)

   if ' play' in command:
      content = command.replace('play' , '')
      talk('playing'+content)
      pywhatkit.playonyt(content)

   elif 'time' in command:
      time = datetime.datetime.now().strftime('%I:%M %p')
      print(time)
      talk('Current time is: '+time)

   elif  'who is'  in command:
      person = command.replace('who  is', '')
      info = wikipedia.summary(person, 1)
      print(info)
      talk(info)

run_lisa()