import speech_recognition as sr
import webbrowser
from gtts import gTTS
import os
import playsound as pl

r1=sr.Recognizer()

    
f=open('D:\My_Data\MCA\Just_Coding\Friday\convo.txt','a') 


def talk(mytext):
    myobj = gTTS(text=mytext, lang='en', slow=False)  
    myobj.save('r.mp3')
    pl.playsound('r.mp3') 
    os.remove('r.mp3')
    f.write('\nFriday : '+mytext)

def hear():
    
    with sr.Microphone() as source:
        r1.adjust_for_ambient_noise(source,duration=1)
        f=0
        while f==0:
            au=r1.listen(source)
            try:
                said=r1.recognize_google(au)
                f=1
                return said
            except:
                print("\t\tListening again...") 

def amazon():
    print('Friday : Say What you want to buy...')
    talk('Say What you want to buy...')
    se=hear()
    url='https://www.amazon.in/s?k='+se+'&ref=nb_sb_noss_2'
    webbrowser.open_new_tab(url)
    talk('searching...'+se+' on amazon')
    print('Friday : searching...',se,'on amazon')
    f.write('\nUser : '+se)

def youtube_open():
    talk('Opening Youtube...')
    webbrowser.open_new_tab('https://www.youtube.com')
    print("Friday : Opening Youtube...")

def youtube_search():
    print('Friday : Say What you want to search...')
    talk('Say What you want to search...')
    se=hear()
    url='https://www.youtube.com/results?search_query='+se
    webbrowser.open_new_tab(url)
    talk('searching...'+se+'on youtube')
    print('Friday : searching...',se,'on youtube')
    f.write('\nUser : '+se)

def google_search():
    print('Friday : Say What you want to search...')
    talk('Say What you want to search...')
    se=hear()
    url='http://google.com/search?q='+se
    webbrowser.open_new_tab(url)
    talk('searching...'+se+'on Google')
    print('Friday : searching...',se,' on Google')

def main(): 
     
    print("\t\nMeet Friday...")
    s=hear()
    print('User : ',s)
    f.write("\n\nUser : "+s)

    if ('hello' in s) or ('hi' in s):
        res='Hello!'
        talk(res)
        print('Friday : ',res)
    elif ('how are you' in s):
        res="It's always good to talk to you sir."
        talk(res)
        print('Friday : ',res)

    print("\nSay a Command --> \n")

    y=hear()
    while ('close' not in y.lower()) and ('stop' not in y.lower()):
        f.write('\nUser : '+y)
        print('User : ',y)
        if ('youtube' in y.lower()) and ('search' in  y.lower()):
            youtube_search()
        elif (('youtube' in y.lower()) and ('open' in y.lower())) or ('youtube' in y.lower())  :
            youtube_open()
        elif 'amazon' in y.lower():
            amazon()
        elif ('google' in y.lower()) and ('search' in y.lower()):
            google_search()
        else:
            talk('None of the cases matches the commmand.')
            print('None of the cases matches the commmand.')
        y=hear()
    f.write('\nUser : '+y)
    talk('I am Closing, Good bye.')
    f.close()
    
if __name__=="__main__":
    main()

