from tkinter import*
from datetime import datetime
import pytz
from PIL import ImageTk,Image
import time

root=Tk()
root.title("world clock")
root.geometry("900x900")

india=ImageTk.PhotoImage(Image.open("india.jpeg"))
img1=ImageTk.PhotoImage(Image.open("japan.jpeg"))
A=ImageTk.PhotoImage(Image.open("australia.jpeg"))
U=ImageTk.PhotoImage(Image.open("usa.jpeg"))



In_label=Label(root,text=" The India")
In_label.place(relx=0.1,rely=0.1,anchor=CENTER)


In_M=Label(root)
In_M["image"]=india
In_M.place(relx=0.2,rely=0.3,anchor=CENTER)

In_T=Label(root,text="Time")
In_T.place(relx=0.1,rely=0.49,anchor=CENTER)



Ja_label=Label(root,text="Japan")
Ja_label.place(relx=0.9,rely=0.1,anchor=CENTER)

Ja_M=Label(root)
Ja_M["image"]=img1
Ja_M.place(relx=0.8,rely=0.35,anchor=CENTER)


Ja_T=Label(root,text="Time")
Ja_T.place(relx=0.9,rely=0.55,anchor=CENTER)


Us_label=Label(root,text="USA")
Us_label.place(relx=0.1,rely=0.6,anchor=CENTER)

Us_M=Label(root)
Us_M["image"]=U
Us_M.place(relx=0.2,rely=0.77,anchor=CENTER)

Us_T=Label(root,text="Time")
Us_T.place(relx=0.1,rely=0.95,anchor=CENTER)



Au_label=Label(root,text="Australia")
Au_label.place(relx=0.9,rely=0.58,anchor=CENTER)

Au_M=Label(root)
Au_M["image"]=A
Au_M.place(relx=0.8,rely=0.77,anchor=CENTER)

Au_T=Label(root,text="Time")
Au_T.place(relx=0.9,rely=0.95,anchor=CENTER)

class India():
    def time(self):
        home1=pytz.timezone("Asia/Kolkata")
        date1=datetime.now(home1)
        converted_time1=date1.strftime("%H:%M:%S")
        In_T["text"]="time: "+converted_time1
        
class Japan():
    def time(self):
        home1=pytz.timezone("japan")
        date1=datetime.now(home1)
        converted_time1=date1.strftime("%H:%M:%S")
        Ja_T["text"]="time: "+converted_time1
        
class USA():
    def time(self):
        home1=pytz.timezone("US/Central")
        date1=datetime.now(home1)
        converted_time1=date1.strftime("%H:%M:%S")
        Us_T["text"]="time: "+converted_time1
        
class Australia():
    def time(self):
        home1=pytz.timezone("Australia/ACT")
        date1=datetime.now(home1)
        converted_time1=date1.strftime("%H:%M:%S")
        Au_T["text"]="time: "+converted_time1
        

objI=India()
objJ=Japan()
objU=USA()
objA=Australia()

btn_I=Button(root,text="show time",command=objI.time)
btn_I.place(relx=0.2,rely=0.5,anchor=CENTER)
btn_J=Button(root,text="show time",command=objJ.time)
btn_J.place(relx= 0.9,rely=0.6,anchor=CENTER)
btn_U=Button(root,text="show time",command=objU.time)
btn_U.place(relx= 0.2,rely=0.99,anchor=CENTER)
btn_A=Button(root,text="show time",command=objA.time)
btn_A.place(relx= 0.9,rely=0.99,anchor=CENTER)

root.mainloop()


