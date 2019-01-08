import os
import time
import ctypes

interuptions = 0

def timer():
    seconds = int(0)
    minutes = int(0)
    hours = int(0)
    global interuptions
    run = input("Enter R to run the program. ")
    while run.lower() == 'r':
        if seconds > 59:
            seconds = 0
            minutes += 1
        if minutes > 59:
            minutes = 0
            hours += 1
        os.system('cls')
        seconds = seconds + 1
        print(str(hours).zfill(2), ":", str(minutes).zfill(2), ":", str(seconds).zfill(2))
        time.sleep(1)
        if seconds == 10:
            user32 = ctypes.WinDLL('user32')
            SW_MAXIMISE = 3
            hWnd = user32.GetForegroundWindow()
            user32.ShowWindow(hWnd, SW_MAXIMISE)
            check = input("Are you focused on your work?")
        if seconds == 20:
            check = input("Are you focused on your work?")
        try:
            pass
        except KeyboardInterrupt as e:
            break
        if seconds == 30:
            check = input("Was the flow interupted?    Yes         No ")
            if check.lower() == 'yes':
                interuptions = interuptions + 1
                os.system('cls')
                print("The number of interuptions: " + str(interuptions))
                restart = input("Do you want to restart the timer? ")
                if restart.lower() == 'yes':
                    timer()
                else:
                    pass
            break

timer()
