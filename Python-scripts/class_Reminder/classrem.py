import datetime
import time
import pyttsx3
import speech_recognition as sr
import webbrowser


r = sr.Recognizer()

classes = []

engine = pyttsx3.init()

file = open('timetable.txt')

slt = 5     #sleep time is 5 seconds


def getday(d):
    dn: str
    if (d == 0):
        dn = ('monday')
    elif d == 1:
        dn = 'tuesday'
    elif d == 2:
        dn = 'wednesday'
    elif d == 3:
        dn = 'thursday'
    elif d == 4:
        dn = 'friday'
    elif d == 5:
        dn = 'saturday'
    elif d == 6:
        dn = 'sunday'
    else:
        dn = 'invalid'
    return dn


def dowork(request):
    pass


def checkifdate(st):
    # print(today)
    try:
        
        if(datetime.datetime.strptime(st,'%d-%m-%Y').date()==datetime.date.today()):
            return True
        else:
            return False
    except:
        return False



for cl in file:
    cl=cl.replace('\n','')
    cl = cl.split('    ')
    classes.append(cl)

print(classes)
while True:

    day = getday((datetime.date.today().weekday()))
    today = datetime.datetime.today()
    # with sr.Microphone() as source:
    #     print("Say something!")
    #     audio = r.listen(source,timeout=3,phrase_time_limit=5)
    #     print('listening off')
    # try:
    #     ifcalled=r.recognize_google(audio)
    #     ifcalled=ifcalled.lower()
    #     print(ifcalled)
    #     if('sam' in ifcalled):
    #         engine.say('how can I help you sir')
    #         engine.runAndWait()
    #         with sr.Microphone() as source:
    #             print('say something!')
    #             reqa = r.listen(source,timeout=3,phrase_time_limit=8)
    #         try:
    #             req=r.recognize_google(reqa)
    #             dowork(req)
    #             engine.say('Ok sir')
    #             engine.runAndWait()
    #         except sr.UnknownValueError:
    #             engine.say('unable to understand your order, sir')
    #             engine.runAndWait()
    #         except sr.RequestError as e:
    #             engine.say('connectivity issue')
    #             engine.runAndWait()
    # except sr.UnknownValueError:
    #     print('nothing')
    # except sr.RequestError as e:
    #     print('connection issue')
    time.sleep(slt)

    for cl in classes:
        len_c = len(cl)
        for i in range(2, len_c, 2):
            if (cl[i] == day or checkifdate(cl[i]) ):
                print(cl[i+1])
                tdel = datetime.datetime.strptime(cl[i + 1], '%H:%M') - today
                print(tdel.seconds)
                if (tdel.seconds <= 600 and tdel.seconds > 600 - slt):
                    engine.say(cl[0] + 'class in 10 minutes')
                    engine.runAndWait()
                    engine.say(cl[0] + 'class in 10 minutes')
                    engine.runAndWait()
                    engine.say(cl[0] + 'class in 10 minutes')
                    engine.runAndWait()
                elif(tdel.seconds<slt and tdel.seconds>=0):
                    engine.say(cl[0] + 'class is live, Do you want to join?')
                    engine.runAndWait()
                    engine.say(cl[0] + 'class is live, Do you want to join?')
                    engine.runAndWait()
                    with sr.Microphone() as source:
                        print("Say something!")
                        audio = r.listen(source,timeout=3,phrase_time_limit=3)
                        print('listening end')
                    try:
                        response=r.recognize_google(audio)
                        response=response.lower()
                        if(response=='yes'or response=='sure' or response=='ok' ):
                            webbrowser.open(cl[1],new=2)
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                        engine.say("No response recieved, opening class")
                        engine.runAndWait()
                        webbrowser.open(cl[1], new=2)
                    except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))
                        engine.say("No response recieved, opening class")
                        engine.runAndWait()
                        webbrowser.open(cl[1], new=2)