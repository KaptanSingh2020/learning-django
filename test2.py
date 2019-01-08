import pymsgbox
import time

time.sleep(5)

#pymsgbox.alert('This is an alert!')
#print(help(pymsgbox))
print(help(pymsgbox.prompt))
pymsgbox.prompt(text='Were you focused? ', title='Reminder')
