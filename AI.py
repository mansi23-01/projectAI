from tkinter import *
from tkinter.font import BOLD, ITALIC, names
from PIL import Image,ImageTk
from pygame.constants import DOUBLEBUF
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pyautogui
from pygame import mixer
import pyjokes
from time import sleep,strftime


f=open('assistant_name.txt','r')
assistant_name=f.read().title()
f.close()
t=0
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[t].id)

def speak(text):
    write(f'{assistant_name} : {text}')
    root.update()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening...")
        audio = r.listen(source,phrase_time_limit = 3)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        write(f"You : {query}")
        root.update()
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return 'none'
    return query

def wishme():
    hour=datetime.datetime.now().hour
    if hour >= 0 and hour < 12:

      speak("Hello,Good Morning")
 
    elif hour >= 12 and hour < 18:

      speak("Hello,Good Afternoon")

    else:

      speak("Hello,Good Evening")   

def Start_AI(): 
    menuframe.pack_forget()
    clock.pack_forget()
    labelf.pack_forget()
    start_b.pack_forget()
    workscreen()
    root.update()
    run=1
    wishme()
    while run==1:
       
        statement=takeCommand().lower()
        if 'none' in statement:
            continue
        if 'wikipedia' in statement:
            if 'open wikipedia' in statement:
                webbrowser.open_new_tab('http://www.wikipedia.com')
            else:
             statement.replace('wikipedia' , '')
             result=wikipedia.summary(statement,3)
             speak('According to wikipedia baba..')
             print(result)
             speak(result)

        elif 'open google' in statement:
            speak('Google rolling in..')
            webbrowser.open_new_tab('https://www.google.com')

        elif 'open youtube' in statement:
            speak('Opening Youtube')
            webbrowser.open_new_tab('http://www.youtube.com')

        elif 'open geeksforgeeks' in statement or 'open geeks'in statement:
            speak('Opening GeeksForGeeks')
            webbrowser.open_new_tab('http://www.geeksforgeeks.org')

        elif 'play music' in statement or 'play song' in statement:
            speak('Here you go with Music')
            dir='song'
            song_list=os.listdir(dir)
            os.startfile(os.path.join(dir,random.choice(song_list)))
            
        elif'next music' in statement or 'next song' in statement:
            dir='song'
            song_list = os.listdir(dir)
            mixer.music.play(os.path.join(dir, random.choice(song_list)))

        elif 'previous song' in statement or 'previous music' in statement:
            pyautogui.press('prevtrack')

        elif 'pause song' in statement or 'pause music' in statement:
            pyautogui.press('playpause')

        elif 'time' in statement:
            curtime=datetime.datetime.now().strftime('%H:%M:%S')
            hour=int(curtime[0:2])
            min=int(curtime[3:5])
            str='AM'
            if hour>12 :
                hour=hour%12
                str='PM'
            print(hour," ",min)
            speak(f'Time is {hour}{min}{str}')


        elif 'switch window' in statement or 'next window' in statement:
             pyautogui.keyDown('altleft')
             pyautogui.press('tab')
             sleep(0.5)
             pyautogui.keyUp('altleft')
        elif 'calculate' in statement:
              statement=statement.replace('calculate','')
              ans=eval(statement)
              speak(f'Answer is {ans}')
              print(f'{statement} = {ans}')
          
        elif 'joke' in statement:
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'make a note' in statement or 'write this down' in statement:
            speak('What would you like me to write down?')  
            start=1
            note=''
            while start==1: 
                print(start)
                statement=takeCommand().lower()
                if 'save this file' not in statement:
                    if statement == 'none':
                     speak('Can You repeat this statement again')
                    else:
                     note=note+" "+statement
                else: 
                 start=2   
            speak('what should be the fie name?')
            file=takeCommand().title()
            f=open(os.path.join(f'{os.getcwd()}/Documents',f'{file}.txt'),'w')
            f.write(note)
            f.close()
            speak('File Saved')

        elif "goodbye" in statement or "offline" in statement or "bye" in statement:
                speak("Alright sir, going offline. It was nice working with you")
                run=0

    root.overrideredirect(0)
    responseframe.pack_forget()
    name.pack_forget()
    img1label.pack_forget()
    menuframe.pack(side=LEFT,fill=Y)
    labelf.pack(pady=(80,0))
    start_b.pack(padx=80)
    clock.pack(side=BOTTOM,anchor = 'ne',padx=20,pady=20)
    
    root.update()

def time():
       string = strftime('%H:%M:%S')
       clock.config(text = string)
       clock.after(1000, time)

def workscreen():
    root.overrideredirect(1)
    global responseframe
    responseframe=Frame(root,bg='#01172e')
    global response_box
    response_box=Text(responseframe,width=40,height=30,bg='black',fg='white')
    Label(responseframe,text='Response Box',font='times 19 bold').pack(side=TOP,anchor='nw')
    response_box.pack()
    global name
    name=Label(root,text=f'{assistant_name}.2.0',font=('Lucida Handwriting', 40),bg='#01172e',fg='#00faff')
    name.pack(side=TOP,anchor='nw',padx=150)
    global img1
    global img1label
    img1=ImageTk.PhotoImage(Image.open('icons\start.png'))
    img1label=Label(root,image=img1,bg='#01172e')
    img1label.pack(side=LEFT,padx=100)
    responseframe.pack(side=BOTTOM,anchor='e',padx=15,pady=15)
    
    
def hideall():
    settingf.pack_forget()
    start_b.pack_forget()
    aboutf1.pack_forget()
    aboutf2.pack_forget()   
    text.pack_forget()
     
def write(text):
    response_box.insert(END,f'\n{text}')

def homefun():
    hideall()
    label1.config(image=img2)
    label2.config(image=img3)
    start_b.pack(padx=80)

def settingfun():
    hideall()
    label1.config(image=img3)
    label2.config(image=img2)
    settingf.pack(pady=15)

def aboutfun():
    hideall()
    label1.config(image=img2)
    label2.config(image=img3)
    text.pack(pady=25,padx=10)
    aboutf1.pack(side=LEFT,anchor='n',padx=10)
    aboutf2.pack(side=RIGHT,anchor='nw',padx=10)

def changename():
    global assistant_name,id
    name=newname.get().title()
    if name != '':
     f=open('assistant_name.txt','w')
     f.write(name)
     assistant_name=name.title()
     f.close()
     label3.config(text=f'{assistant_name}.2.O')
     root.title(assistant_name)
     root.update()
     newnameentry.delete(0,'end')
    t=voice.get()
    engine.setProperty('voice',voices[t].id)
    print(id)
    
def mainscreen():
    global root
    root=Tk()
    root.geometry('1150x800')
    root.title(assistant_name.title())
    root.iconbitmap('icons\icon.ico')
    root.config(background='#01172e')
    root.resizable(0,0)
    global menuframe
    menuframe=Frame(root,bg='black')
    menuframe.pack(side=LEFT,fill=Y)
    # =========menu frame===============
    
    home = ImageTk.PhotoImage(Image.open('icons\home.png').resize((35,35),Image.ANTIALIAS))
    about = ImageTk.PhotoImage(Image.open('icons\info.png').resize((35,35),Image.ANTIALIAS))
    setting = ImageTk.PhotoImage(Image.open('icons\setting.png').resize((35,35),Image.ANTIALIAS))
    exit = ImageTk.PhotoImage(Image.open('icons\exit.png').resize((35,35),Image.ANTIALIAS))

    home_b = Button(menuframe,text='HOME ',font= ('times 20'),image=home,bg='black',compound=LEFT,relief=FLAT,fg='white',padx=10,width=180,justify=LEFT,command=homefun)
    about_b = Button(menuframe,text='ABOUT',font= ('times 20'),image=about,bg='black',compound=LEFT,relief=FLAT,fg='white',padx=10,width=180,justify=LEFT,command=aboutfun)
    setting_b = Button(menuframe,text='SETTING',font= ('times 20'),image=setting,bg='black',compound=LEFT,relief=FLAT,fg='white',padx=10,command=settingfun)
    exit_b= Button(menuframe,text='EXIT',font= ('times 20'),image=exit,bg='black',compound=LEFT,relief=FLAT,fg='white',command=quit,justify=LEFT,anchor='w',width=180,padx=10)

    home_b.pack()
    setting_b.pack()
    about_b.pack()
    exit_b.pack(side=BOTTOM)
    home_b.bind('<Enter>',lambda e: home_b.config(background='white',fg='black'))
    home_b.bind('<Leave>',lambda e: home_b.config(background='black',fg='white'))
    about_b.bind('<Enter>',lambda e: about_b.config(background='white',fg='black'))
    about_b.bind('<Leave>',lambda e: about_b.config(background='black',fg='white'))
    setting_b.bind('<Enter>',lambda e: setting_b.config(background='white',fg='black'))
    setting_b.bind('<Leave>',lambda e: setting_b.config(background='black',fg='white'))
    exit_b.bind('<Enter>',lambda e: exit_b.config(background='red'))
    exit_b.bind('<Leave>',lambda e: exit_b.config(background='black'))
    menuframe.grid_propagate(False)

    
    # =======================home screen=============================
    
    global clock
    clock=Label(root,font='times 30 bold',background = 'black', foreground = 'white',width=7,height=1)
    clock.pack(side=BOTTOM,anchor = 'ne',padx=20,pady=20)
    time()
    global img2,img3
    img2=ImageTk.PhotoImage(Image.open('icons\iconrobot.png'))
    img3=ImageTk.PhotoImage(Image.open('icons\iconrobot1.png'))
    
    global labelf
    labelf=Frame(root,background='#01172e')
    global label1,label2
    label1=Label(labelf,image=img2,bg='#01172e',width=50)
    label2=Label(labelf,image=img3,bg='#01172e',width=50)
    global label3
    label3=Label(labelf,text=f'{assistant_name}.2.O',bg='#01172e',relief='flat',font=('Lucida Handwriting', 50,BOLD ,UNDERLINE),fg='white')
    label1.pack(side=LEFT,padx=20)
    label2.pack(side=RIGHT,padx=20)
    label3.pack(pady=40)
    labelf.pack(pady=(50,0))
    global start_b
    start=ImageTk.PhotoImage(Image.open('icons\start-button.png').resize((200,200),Image.ANTIALIAS))
    start_b=Button(root,image=start,font=('times',50),command=Start_AI,background='#01172e',activebackground='#01172e',relief='flat')
    start_b.pack(padx=80)
    
    # ====================Setting menu=============================
    
    global newname
    global settingf
    settingf=Frame(root,background='#00faff')
    newname=StringVar()
    label4=Label(settingf,text='Change Assistant Name :- ',font='times 20 bold')
    label4.pack(side=TOP,anchor=W,pady=10,padx=10)
    global newnameentry
    newnameentry=Entry(settingf,textvariable=newname,width=30,font='times 20')
    newnameentry.pack(pady=15,padx=10)
    global voice
    voice=IntVar()
    label5=Label(settingf,text='Assistant voice :- ',font='times 20 bold')
    label5.pack(anchor='w',pady=10,padx=10)
    male=Radiobutton(settingf,text='Male',variable=voice,value=0,font='times 15')
    female=Radiobutton(settingf,text='Female',variable=voice,value=1,font='times 15')
    male.pack(anchor='w',pady=5,padx=10)
    female.pack(anchor='w',pady=5,padx=10)
    submitb=Button(settingf,text='Submit',font='times 20 bold',fg='blue',command=changename)
    submitb.pack()
    # settingf.pack(pady=15)
    
    # =====================About Menu==================
    
    global aboutf1
    aboutf1=Frame(root,bg='#03f0fc',width=50)
    global text
    text=Label(root,text='-: Developers :-' , font=('helvetica',30,ITALIC),width=50,bg='#03f0fc')
    # text.pack(pady=25,padx=10)
    name=Label(aboutf1,text='Ashish Kumar',font=('helvetica',15,ITALIC),bg='#03f0fc')
    email=Label(aboutf1,text='Email:- ashishvg1437@gmail.com',font=('helvetica',15,ITALIC),bg='#03f0fc')
    insta=ImageTk.PhotoImage(Image.open('icons\instagram.png').resize((40,40),Image.ANTIALIAS))
    fb=ImageTk.PhotoImage(Image.open('icons\iconfacebook.png').resize((40,40),Image.ANTIALIAS))
    linkin=ImageTk.PhotoImage(Image.open('icons\linkedin.png').resize((40,40),Image.ANTIALIAS))
    info1=Frame(aboutf1,bg='#03f0fc',width=50)
    insta1=Button(info1,image=insta,bg='#03f0fc',activebackground='#03f0fc',relief='flat')
    fb1=Button(info1,image=fb,bg='#03f0fc',activebackground='#03f0fc',relief='flat')
    link1=Button(info1,image=linkin,bg='#03f0fc',activebackground='#03f0fc',relief='flat')
    name.pack()
    email.pack()
    insta1.pack(side=LEFT,padx=10)
    fb1.pack(side=LEFT,padx=10)
    link1.pack(side=LEFT,padx=10)
    info1.pack()
    # aboutf1.pack(side=LEFT,anchor='n',padx=10)
    
    global aboutf2
    aboutf2=Frame(root,bg='#03f0fc',width=50)
    name2=Label(aboutf2,text='Mansi Srivastav',font=('helvetica',15,ITALIC),bg='#03f0fc')
    email2=Label(aboutf2,text='Email:- mansisrivastav2102@gmail.com',font=('helvetica',15,ITALIC),bg='#03f0fc')
    info2=Frame(aboutf2,bg='#03f0fc',width=50)
    insta2=Button(info2,image=insta,bg='#03f0fc',activebackground='#03f0fc',relief='flat',command=lambda: webbrowser.open_new_tab('www.google.com'))
    fb2=Button(info2,image=fb,bg='#03f0fc',activebackground='#03f0fc',relief='flat')
    link2=Button(info2,image=linkin,bg='#03f0fc',activebackground='#03f0fc',relief='flat')
    name2.pack()
    email2.pack()
    insta2.pack(side=LEFT,padx=10)
    fb2.pack(side=LEFT,padx=10)
    link2.pack(side=LEFT,padx=10)
    info2.pack()
    # aboutf2.pack(side=RIGHT,anchor='nw',padx=10)
    root.mainloop()  

    

mainscreen()