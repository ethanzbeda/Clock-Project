from tkinter import *
from time import *
import datetime
import pytz

def update_time():
    timezone = pytz.timezone('US/Eastern')
    current_time = datetime.datetime.now(timezone)
    time_string = current_time.strftime('%-I:%M:%S %p')
    time_label.config(text=time_string)
    window.after(1000, update_time)

    day_string = strftime('%A')
    day_label.config(text=day_string)

    date_string = strftime('%B %d, %Y')
    date_label.config(text=date_string)
    
window = Tk()
window.configure(background='black')
  
time_label = Label(window,font=('Arial', 50),fg='black',bg='white')
time_label.pack()

day_label = Label(window,font=('Arial', 25),fg='white', bg='black')
day_label.pack()

date_label = Label(window,font=('Arial', 50),fg='white', bg='black')
date_label.pack()
                   
update_time()

window.mainloop()

