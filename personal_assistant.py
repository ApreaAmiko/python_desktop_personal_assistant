import pyttsx3, webbrowser, smtplib, random, wikipedia, datetime, wolframalpha, os, sys, subprocess
import speech_recognition as sr
from tkinter import *

client = wolframalpha.Client('TV83LL-67JUVUPAVV')
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


def speak(audio):
    print('Computer: ' + audio)
    engine.setProperty('voice', voices[len(voices)-2].id)
    engine.say(audio)
    engine.runAndWait()

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='id')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Try again')
        pass

    return query

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

class Widget:
    def __init__(self):
       root = Tk()
       root.title('Program')
       root.config(background='White')
       root.geometry('400x600')
       root.resizable(0, 0)

       self.compText = StringVar()
       self.userText = StringVar()

       self.userText.set('Tekan \'Start Listening\' Untuk Memberikan Perintah')

       userFrame = LabelFrame(root, text="USER", font=('Black ops one', 10, 'bold'))
       userFrame.pack(fill="both", expand="yes")
         
       left2 = Message(userFrame, textvariable=self.userText, bg='gainsboro', fg='black')
       left2.config(font=("Comic Sans MS", 10, 'bold'))
       left2.pack(fill='both', expand='yes')
       
       btn = Button(root, text='Start Listening!', font=('Black ops one', 10, 'bold'), bg='deepSkyBlue', fg='black', command=self.clicked).pack(fill='x', expand='no')
       btn2 = Button(root, text='Tutup!', font=('Black Ops One', 10, 'bold'), bg='firebrick3', fg='black', command=root.destroy).pack(fill='x', expand='no')

       compFrame = LabelFrame(root, text="COMPUTER", font=('Black ops one', 10, 'bold'))
       compFrame.pack(fill="both", expand="yes")
         
       left1 = Message(compFrame, textvariable=self.compText, bg='powder blue',fg='black')
       left1.config(font=("Comic Sans MS", 10, 'bold'))
       left1.pack(fill='both', expand='yes')
       
       speak('Hello, I am your digital assistan!, What should I do for You?')
       self.compText.set('Hello, I am your digital assistan!, What should I do for You?')

       root.bind("<Return>", self.clicked)
       root.mainloop()

    def clicked(self):
        print('Working')
        query = myCommand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()
        
        if 'buka ccleaner' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files\CCleaner\CCleaner.exe')

        elif 'buka browser' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

        elif 'buka powerpoint' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files\Microsoft Office\Office15\POWERPNT.EXE')

        elif 'buka excel' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files\Microsoft Office\Office15\XLICONS.EXE')

        elif 'buka word' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files\Microsoft Office\Office15\WINWORD.EXE')
        
        elif 'buka youtube' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'buka wikipedia' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.wikipedia.co.id')

        elif 'buka google' in query:
            speak('okay')
            self.compText.set('okay')
            webbrowser.open('www.google.co.id')

        elif 'buka facebook' in query:
            speak('okay')
            self.compText.set('okay')
            webbrowser.open('www.facebook.com')

        elif 'buka gmail' in query:
            speak('okay')
            self.compText.set('okay')
            webbrowser.open('www.gmail.com')

        elif "apa kabar" in query or 'sedang apa' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            self.compText.set(random.choice(stMsgs))
            speak(random.choice(stMsgs))

        elif 'email' in query:
            self.compText.set('Who is the recipient? ')
            speak('Who is the recipient? ')
            recipient = myCommand()
            self.userText.set(recipient)
            recipient = recipient.lower()

            if 'saya' in recipient:
                try:
                    self.compText.set('What should I say? ')
                    speak('What should I say? ')
                    content = myCommand()
                    self.userText.set(content)
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("tasykamil@gmail.com", '39836666')
                    server.sendmail('tasykamil@gmail.com', "tasykamil@gmail.com", content)
                    server.close()
                    self.compText.set('Email sent!')
                    speak('Email sent!')

                except:
                    self.compText.set('Sorry Sir! I am unable to send your message at this moment!')
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'berhenti' in query or 'abort' in query or 'stop' in query:
            self.compText.set('Okay')
            speak('okay')
            self.compText.set('Bye Sir, have a good day.')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            self.compText.set('Hello Sir')
            speak('Hello Sir')
                                    
        elif 'mainkan musik' in query:
            music_dir = 'C:\\Users\\Aprea\\Music\\Oasis'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

            self.compText.set('Okay, here is your music! Enjoy!')      
            speak('Okay, here is your music! Enjoy!')
            

        else:
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    self.compText.set(results)
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    self.compText.set(results)
                    speak(results)
        
            except:
                speak('I don\'t know Sir! Try Google!')
                self.compText.set('I don\'t know Sir! Try Google!')
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')

if __name__ == '__main__':
    greetMe()
    widget = Widget() 
        
