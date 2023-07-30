import pyttsx3
import speech_recognition as sr
import webbrowser as wb
from datetime import datetime
import wikipedia as wp
import smtplib
import winshell
from calendar import *
import pyautogui as pa
from pygame import mixer
import os
import random
from tkinter import *
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening')
		r.pause_threshold = 1;r.energy_threshold = 200
		audio = r.listen(source)
		try:
			print("Recognizing")
			Query = r.recognize_google(audio, language='en-in')
			print("the command is printed=", Query)
			
		except Exception as e:
			# print(e)
			print("Say that again sir");speak("Say that again sir")
			return "None"
		return Query

def tellDay():
	day = datetime.datetime.today().weekday() + 1
	Day_dict = {1: 'Monday', 2: 'Tuesday',3: 'Wednesday', 4: 'Thursday',5: 'Friday', 6: 'Saturday',7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		speak("The day is " + day_of_the_week)

def Hello():
	speak("hello I am your desktop assistant.")

def wishme():
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
                speak("Good Morning!")
        elif hour>=12 and hour<18:
                speak("Good Afternoon!")
        else:
                speak("Good Evening!")

        speak("I am kara How may I help you?")

# def Take_query():
	# Hello()
#     wishme()
def sendEmail(to, content):
        obj=smtplib.SMTP_SSL("smtp.gmail.com",465)
        obj.login("asp15299@gmail.com","wbhdpjblnscdyskq")
        obj.sendmail("asp15299@gmail.com",to,content)
        obj.quit()

if __name__ == '__main__':
#   Hello();wishme()
  while True:
        Query=takeCommand().lower()
        # Query="play music"
        if "from wikipedia" in Query:
                speak("Searching wikipedia...!")
                Query = Query.replace("wikipedia", "")
                # Query = Query.replace("tell me about", "")
                r=wp.summary(Query, sentences=2)
                speak("According to wikipedia we got..")
                print(r)
                speak(r)

        elif "today's weather" in Query or "how is weather" in Query:
                wb.open("https://www.msn.com/en-in/weather/forecast/in-Kolhapur,Maharashtra?loc=eyJsIjoiS29saGFwdXIiLCJyIjoiTWFoYXJhc2h0cmEiLCJyMiI6IktvbGhhcHVyIiwiYyI6IkluZGlhIiwiZyI6ImVuLWluIiwieCI6NzQuMjMzMywieSI6MTYuNjkxN30%3D&weadegreetype=C&content=NormalWeather_wxnw_greeting&ocid=msedgntp&cvid=e3ab818e056b44ffaab95b5db989388a")
                
        elif "news" in Query:
                speak("which language would you like to hear")
                Query1=takeCommand().lower()
                if "marathi" in Query1:
                        wb.open("https://www.youtube.com/watch?v=04y0H01GTg0")
                        # continue
                
                elif "hindi" in Query1:
                        wb.open("https://www.youtube.com/watch?v=nyd-xznCpJc")
                        # continue

                elif "english" in Query1:
                        wb.open("https://www.youtube.com/watch?v=w_Ma8oQLmSM")
                        # continue
                elif "any" in Query1:
                        wb.open("https://www.youtube.com/watch?v=04y0H01GTg0")

        elif "which day it is" in Query:
                tellDay()

        elif "tell me your name" in Query:
                speak("I am kara How may I help you?")

        elif "tell me about yourself" in Query:
                speak("hi, I am kara. I am an virtual desktop assistant born in august 2022. My work is to automate tasks by using symbolic artificial Intelligence. ")

        elif "open google" in Query:
                speak("Opening Google")
                wb.open("www.google.com")
                # continue

        elif "open youtube" in Query:
                speak("Opening youtube")
                wb.open("youtube.com")
                # exit()
                # continue

        elif "open hackerrank" in Query:
                speak("Opening hackerrank")
                wb.open("https://www.hackerrank.com/satejbpatil")
                # continue

        elif "open linkedin" in Query:
                speak("Opening linkedin")
                wb.open("https://www.linkedin.com/in/satejbpatil/")
                # continue

        elif "open leetcode" in Query:
                speak("Opening leetcode")
                wb.open("https://leetcode.com/satyam47/")
                # continue

        elif "open twitter" in Query:
                speak("Opening twitter")
                wb.open("https://twitter.com/satejbpatil")
                # continue

        elif "open whatsapp" in Query:
                speak("Opening whatsapp")
                wb.open("https://web.whatsapp.com/")
                # continue

        elif "send message" in Query:
                try:
                        speak("What should I say?")
                        Query1=takeCommand().lower()
                # Query1=takeCommand().lower()
                        hr=datetime.now()
                        print(hr.hour)
                        print(hr.minute)
                        pywhatkit.sendwhatmsg("+919145080875",Query1,hr.hour,hr.minute+1)
                except Exception as e:
                        print(e)
                        speak("MESSAGE HAS NOT SENT YET!")  


                # continue

        elif "hotels near me" in Query:
                wb.open("https://www.google.com/maps/search/restaurants/@16.9424297,74.4008749,15z/data=!3m1!4b1")


        elif "open map" in Query:
                wb.open("https://www.google.com/maps")
                # continue

        # shopping
        elif "shopping" in Query:
                speak("which website would you like.")
                Query1=takeCommand().lower()
                if "amazon" in Query1:
                        wb.open("www.amazon.in")
                        # continue
                
                elif "myntra" in Query1:
                        wb.open("https://www.myntra.com/?utm_source=dms_google&utm_medium=searchbrand_cpc&utm_campaign=dms_google_searchbrand_cpc_Search_Brand_Myntra_Brand_India_BM_TROAS_SOK&gclid=Cj0KCQiAm5ycBhCXARIsAPldzoUnVJ24avNWDOD31LCMucKtNRaxDhA3m0cG687ts2ZvMaIE_VLIjNMaAlSaEALw_wcB")
                        # continue

                elif "meesho" in Query1:
                        wb.open("https://www.meesho.com/")
                        # continue

        elif "open spotify" in Query:
                wb.open("https://open.spotify.com/show/5MIQC4i9ggv1AaQaXMI5Nv")
                # continue

        elif "play music" in Query:
                music_dir='D:\\Music\\Waiting For Love.mp3'
                # songs=os.listdir(music_dir)
                # print(songs)
                # os.startfile(os.path.join(music_dir, songs[0]))
                os.startfile(music_dir)
        # elif "play music" in Query:
        #         music_dir = "D:\\Music\\"
        #         songs=os.listdir(music_dir)
        #         print(songs)
        #         rand=random.randint(0, 2)
        #         print(rand)
        #         os.startfile(os.path.join(music_dir,songs[rand]))
                # exit()
                # continue

        elif "open music player" in Query:
                t=Tk()

                t.minsize(250,390)
                t.maxsize(330,470)
                t.title("OS Player")
                t.configure(bg="#ffffbf")
                t = Frame(t, highlightbackground="black", highlightthickness=2)
                t.pack(padx=20, pady=20)

                music_dir = "D:\Pro\Music"

                songs=os.listdir(music_dir)
                maxSong=len(songs)
                rand=random.randint(0, maxSong-1)

                def play1():
                        mixer.init()
                        global maxSong
                        global rand
                        global music_dir
                        global songs
                        print(songs)
                        print(rand)
                        mixer.music.load(os.path.join(music_dir,songs[rand]))
                        mixer.music.play(loops=-1)
        
                def pause():
                        mixer.music.pause()

                def resume():
                        mixer.music.unpause()

                def next():
                        global maxSong
                        global rand
                        global music_dir
                        global songs
                        # Circular queue
                        rand=(rand+1)%maxSong

        # rand=rand+1
        # if(rand==maxSong):
        #         rand=0

                        mixer.music.load(os.path.join(music_dir,songs[rand]))
                        mixer.music.play(loops=-1)

                def prev():
                        global maxSong
                        global rand
                        global music_dir
                        global songs
                        rand=(rand-1)
                        if rand==-1:
                                rand=maxSong-1
                        mixer.music.load(os.path.join(music_dir,songs[rand]))
                        mixer.music.play(loops=-1)
        
                def rewind():
                        mixer.music.rewind()
    
# l=Label(t,text="MUSIC PLAYER",bg="cyan",width=20,height=2).grid(row=0,column=3,pady=30)
                b1=Button(t,text="Play Music",command=play1,activebackground="#b100cd",width=20,height=2,foreground="white",activeforeground="blue",bg="#4c00b0").grid(row=1,column=3)
                b2=Button(t,text="Next",command=next,activebackground="#b100cd",width=7,height=2,foreground="white",activeforeground="blue",bg="#ca5cdd").grid(row=2,column=5,padx=1,pady=20)
                b3=Button(t,text="Previous",command=prev,activebackground="#b100cd",width=7,height=2,foreground="white",activeforeground="blue",bg="#ca5cdd").grid(row=2,column=2,padx=1,pady=20)
                b4=Button(t,text="Pause",command=pause,activebackground="#b100cd",width=7,height=2,foreground="white",activeforeground="blue",bg="#ca5cdd").grid(row=3,column=3,padx=1,pady=20)
                b5=Button(t,text="Resume",command=resume,activebackground="#b100cd",width=7,height=2,foreground="white",activeforeground="blue",bg="#ca5cdd").grid(row=2,column=3,pady=20)
                b6=Button(t,text="Rewind",command=rewind,activebackground="#b100cd",width=7,height=2,foreground="white",activeforeground="blue",bg="#ca5cdd").grid(row=4,column=3,padx=1,pady=20)
                b7=Button(t,text="Exit",command=exit,activebackground="magenta",width=7,height=2,foreground="white",activeforeground="blue",bg="red").grid(row=5,column=3)

                t.mainloop()

        elif "the time" in Query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
                # continue

        elif "open code editor" in Query: #not running.
                # codepath="C:\\Users\\91777\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                # codepath="C:\\Users\\satej\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
                codepath="C:\\Users\\satej\\AppData\\Local\\Programs\\Microsoft VS Code\\Code"
                os.startfile(codepath)
                # continue

        elif "open ms office apps" in Query or  "open ms office app" in Query:
                speak("which software do you want")
                Query1=takeCommand().lower()
                if "powerpoint" in Query1:
                        codepath="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                        os.startfile(codepath)
                
                elif "word" in Query1:
                        codepath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                        os.startfile(codepath)

                elif "excel" in Query1:
                        codepath="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                        os.startfile(codepath)
        # elif "open powerpoint" in Query:
        #         codepath="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
        #         os.startfile(codepath)
                # continue

        # elif "open word" in Query:
        #         codepath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        #         os.startfile(codepath)
                # continue

        # elif "open excel" in Query:
        #         codepath="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
        #         os.startfile(codepath)
                # continue

        elif "open chrome" in Query:
                codepath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(codepath)
                # continue

        elif "create folder" in Query:
                speak("name of directory ")
                directory = takeCommand()
                parent_dir = "D:/Kara_Project/"
                path = os.path.join(parent_dir, directory)
                os.mkdir(path)
                print("Directory '% s' created" % directory)
                speak("Folder is created")
                # continue

        elif "create file" in Query:
                speak("name of file")
                file_name = takeCommand()
                parent_dir="D:/Kara_Project/"
                path = os.path.join(parent_dir, file_name)
                s=open(path,"w") 
                s.close() 
                print("file '% s' created" % file_name)
                speak("File is created")

        elif "delete file" in Query:
                speak("name of file")
                file_name = takeCommand()
                parent_dir="D:/Kara_Project/"
                path = os.path.join(parent_dir, file_name)
                if os.path.exists(path):
                        os.remove(path)
                        print("Successfully Deleted.")
                        speak("Successfully Deleted.")
                else:
                        print("The file does not exist")
                        speak("The file does not exist")

        elif "task to do" in Query:
                pyobj=pyttsx3.init()
                fo=open("todo.txt","r")
                ip=fo.read()
                pyobj.say(ip)
                pyobj.runAndWait()

        elif "add task" in Query:
                # speak("name of file")
                # file_name = takeCommand()
                # parent_dir="D:/Kara_Project/"
                # path = os.path.join(parent_dir, file_name)
                s=open("todo.txt","a") 
                speak("what should I add.")
                con=takeCommand()
                con="\n"+con
                s.write(con)
                s.close() 
                print("Written")
                speak("Task is added")
                # print("file '% s' created" % file_name)

        elif "add data in file" in Query:
                speak("name of file")
                file_name = takeCommand()
                parent_dir="D:/Kara_Project/"
                path = os.path.join(parent_dir, file_name)
                s=open(path,"a") 
                speak("Contain in a file")
                con=takeCommand()
                s.write(con)
                s.close() 
                print("Written")
                speak("Successfully written in a file.")
                # print("file '% s' created" % file_name)

        elif "open control panel" in Query:
                codepath="C:\\Users\\satej\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel"
                os.startfile(codepath)
                # continue

        elif "open web server" in Query:
                codepath="C:\\xampp\\xampp-control.exe"
                os.startfile(codepath)

        elif "open microsoft edge" in Query:
                codepath="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(codepath)
                # exit()
                

        elif "send email" in Query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "fcbixaron@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
                # continue
                # exit()
            except Exception as e:
                print(e)
                speak("EMAIL HAS NOT SENT YET!")    
                
                # continue

        elif "recycle bin" in Query:
                try:
                        winshell.recycle_bin().empty(confirm=False,show_progress=False,sound=True)
                        print("Recycle bin is emptied Now!")
                        speak("Recycle bin is emptied Now!")
                except:
                        print("Recycle bin is already empty!")
                        speak("Recycle bin is already empty!")
                # continue

        elif "change the desktop" in Query:
                pa.hotkey('win','ctrl','left') #will switch one desktop to the left
                pa.hotkey('win','ctrl','right') #will switch one desktop to the right
                # continue

        elif "open calendar" in Query:
                # year=int(input("Enter Year: "))
                print("ghjhjbj")
                print(calendar(2022,2,1,8,4))
                # continue

#         # pip install AppOpener
# from AppOpener import run
# run("whatsapp") # Opens whatsapp if installed

        

        elif "bye" in Query or "end" in Query or "shutdown" in Query:
                speak("As you wish, sir. Have a nice day.") 
                exit()

        elif "none" in Query:
                # print("No such Command.")
                print("None")
                pass
                
        else:
                speak("I beg your pardon.")
                # continue




# C:\Users\satej\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup