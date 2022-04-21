
import time
from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry("300x250")

root.title("Timer :)")

root.attributes("-topmost",True)
hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hourEntry= Entry(root, width=3, font=("Arial",18,""),textvariable=hour)
hourEntry.place(x=80,y=20)
name1 = Label(text="hr").place(x=80,y=60)

minuteEntry= Entry(root, width=3, font=("Arial",18,""),textvariable=minute)
minuteEntry.place(x=130,y=20)
name2 = Label(text="min").place(x=130,y=60)

secondEntry= Entry(root, width=3, font=("Arial",18,""),textvariable=second)
secondEntry.place(x=180,y=20)
name3 = Label(text="sec").place(x=180,y=60)
print("hour=",hour," minute=",minute,"  second=",second)
def submit():
    try:
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        print(" total sec=",temp)
    except :
        print("Please input the right value")
    while temp>-1:
        mins,secs = divmod(temp,60)
        hours = 0
        if(mins > 60):
            hours,mins = divmod(mins,60)
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        root.update()
        time.sleep(1)
        if(temp == 0):
            messagebox.showinfo("Timer Countdown" , " Time is OVER!")
        temp-=1

btn = Button(root,text = "Set-time Conuntdown",bd='5',command = submit())
btn.place(x = 70,y = 120)


root.mainloop()


        