import os
import time
import ctypes

interuptions = 0
successes = 0

def timer():
    seconds = int(0)
    minutes = int(0)
    hours = int(0)
    global interuptions
    global successes
    print('\n')

    while True:
        try:
            if seconds > 59:
                seconds = 0
                minutes += 1
            if minutes > 59:
                minutes = 0
                hours += 1
            #os.system('cls')
            seconds = seconds + 1
            print(str(hours).zfill(2), ":", str(minutes).zfill(2), ":", str(seconds).zfill(2), end='\r')
            time.sleep(1)
            if minutes == 30:
                ctypes.windll.user32.MessageBoxW(0, "", "Time up!", 0x1000)
                print('')
                check = input("Are you focused on your work?  ")
            if minutes == 30 and hours == 1:
                print('')
                check = input("Was the flow interupted?  ")
                if check.lower() == 'yes':
                    interuptions = interuptions + 1
                    #os.system('cls')
                    print("The number of successful sessions: " + str(successes))
                    print("The number of interuptions: " + str(interuptions))
                    timer()
                if check.lower() == 'no':
                    successes = successes + 1
                    print("The number of successful sessions: " + str(successes))
                    print("The number of interuptions: " + str(interuptions))
                    timer()
        except KeyboardInterrupt as e:
                break

timer()
