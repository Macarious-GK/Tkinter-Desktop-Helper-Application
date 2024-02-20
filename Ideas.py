 #1 Screenshots
"""
import pyautogui
import tkinter as tk
from tkinter.filedialog import *
CAT = Tk()
def takeScreenshot():
    myscreenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myscreenshot.save(save_path+'_screenshot2.png')
    print("Screenshot is saved")
button = tk.Button(text='take screenshot',command = takeScreenshot, bg='green', fg='white',font=10)
button.place()
CAT.mainloop()
"""
#2 corector
"""
from tkinter import messagebox
from tkinter import *
from textblob import *
CAT = Tk()
CAT.geometry("550x600+500+50")
CAT.title("Desktop Interface")
def OPEN_VIDEO():
    a = entry1.get()
    b = TextBlob(a)
    messagebox.showinfo(title="Battery", message="correct word is:"+str(b.correct()))
buttom= Button(text='Correct',command=OPEN_VIDEO)
def clear_text():
   entry1.delete(0, END)
entry1 = Entry(width=30)
ClearB = Button(text="Clear", command=clear_text, font=('Helvetica bold',10))
entry1.pack()
buttom.pack()
ClearB.pack()
CAT.mainloop()
"""
#3
"""
import pyautogui
ijh = pyautogui.screenshot()
ijh.save(r"D:\screen.png")
"""
#4 Calendar
"""
from tkinter import *
from tkcalendar import *
ASD = Tk()
ASD.geometry('300x300')
def selectdata():
    myDate=mycal.get_date()
    selectedDate=Label(text=myDate)
    selectedDate.pack()
mycal=Calendar(setmode="day", date_pattern="d/m/yy")
mycal.pack()
open_cal = Button(text='select date', command=selectdata)
open_cal.pack()
ASD.mainloop()
"""
#5 DICTIONARY //////////
"""
from tkinter import *
from PyDictionary import *
dictionary = PyDictionary()
root = Tk()
root.geometry("400x400")
root.title("project")
def dict():
    meaning.config(text=dictionary.meaning(word.get()))
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))
Label(root, text='dictionary', font='Helvetica 20 bold', fg='green').pack(pady=10)
frame = Frame(root)
Label(frame,text="type word", font='Helvetica 15 bold').pack(side=LEFT)
word = Entry(frame, font='Helvetica 15 bold')
word.pack()
frame.pack(pady=10)
frame1 = Frame(root)
Label(frame1, text='meaning', font='Helvetica 10 bold').pack(side=LEFT)
meaning = Label(frame1, text='', font='Helvetica 10 bold')
meaning.pack()
frame1.pack(pady=10)
frame2 = Frame(root)
Label(frame2, text='Synonym:-', font='Helvetica 10 bold').pack(side=LEFT)
synonym = Label(frame2, text='', font='Helvetica 10 bold')
synonym.pack()
frame2.pack(pady=10)
frame3 = Frame(root)
Label(frame3, text='Antonym:-', font='Helvetica 10 bold').pack(side=LEFT)
antonym = Label(frame3, text='', font='Helvetica 10 bold')
antonym.pack()
frame3.pack(pady=10)
Button(root, text='submit', font='Helvetica 10 bold', command=dict).pack()
root.mainloop()
"""
#6 QRCODE       //////
"""
import pyqrcode
import png
from pyqrcode import QRCode
s= "www.curiousprogrammer.com"
url = pyqrcode.create(s)
url.svg("myqr.svg", scale = 8)
url.png("myqr.png", scale = 6)
"""
#7 note book
"""
from tkinter import *
from tkinter import ttk
WINDOW1 = Tk()
WINDOW1.title("Name")
WINDOW1.geometry("500x400+500+200")
note=ttk.Notebook(WINDOW1)
tab1=Frame(note)
tab2=Frame(note)
tab3=Frame(note)
note.add(tab1, text='F page')
note.add(tab2, text='S page')
note.add(tab3, text='T page')
note.pack()
bg = PhotoImage(file="13.png")
label1 = Label(tab1, image=bg).pack()
photo= PhotoImage(file=("20.png"))
label = Label(tab2, image=photo).pack()
photo= PhotoImage(file=("9.png"))
label = Label(tab3, image=photo).pack()
WINDOW1.mainloop()
"""
#8 clock
"""
from tkinter import *
import time
import sys
CAT = Tk()
CAT.geometry("550x600+500+50")
CAT.title("Desktop Interface")
def get_time():
    timevar=time.strftime("%I:%M:%S %p")
    clock.config(text=timevar)
    clock.after(200, get_time)
clock = Label( font=("ds-digital",30,'bold'),bd=5, bg='black',fg='cyan')
clock.pack()
get_time()
CAT.mainloop()
"""
#9 video downloader
"""
from tkinter import *
import webbrowser
CAT = Tk()
CAT.geometry("550x600+500+50")
CAT.title("Desktop Interface")
def DOWNLOWD():
    url = entry1.get()
    downlowd = url[:12] + 'ss' + url[12:]
    webbrowser.open(downlowd)
def clear_text():
   entry1.delete(0, END)
entry1 = Entry(width=30)
ClearB = Button(text="Clear", command=clear_text, font=('Helvetica bold',10))
buttom= Button(text='Downlowd',command=DOWNLOWD)
entry1.pack()
buttom.pack()
ClearB.pack()
CAT.mainloop()
"""
#10 Tranclator
"""
from tkinter import *
from translate import Translator
CAT = Tk()
CAT.geometry("550x600+500+50")
CAT.title("Desktop Interface")
def TRANSLATE():
    W = entry1.get()
    s = Translator(from_lang="english", to_lang="Arabic")
    res = s.translate(W)
    l = Label(text=res).pack()
def clear_text():
   entry1.delete(0, END)
entry1 = Entry(width=30)
entry1.pack()
ClearB = Button(text="Clear", command=clear_text, font=('Helvetica bold',10))
buttom= Button(text='Tranclate',command=TRANSLATE)
entry1.pack()
buttom.pack()
ClearB.pack()
CAT.mainloop()
"""
#11 WEBSITS
"""
from tkinter import *
import webbrowser
CAT = Tk()
CAT.geometry("550x600+500+50")
CAT.title("Desktop Interface")
CAT.resizable(0, 0)
def site1A():
    webbrowser.open("http://courses.nu.edu.eg/")
def site2A():
    webbrowser.open("https://outlook.office.com/mail/inbox")
def site3A():
    webbrowser.open("https://www.youtube.com/")
def site4A():
    webbrowser.open("www.google.com")
def search():
    t = e.get()
    webbrowser.open(t)
B1A = Button(text="NU.Courses", width=10, height=1, command=site1A)
B2A = Button(text="OutLook", width=10, height=1, command=site2A)
B3A = Button(text="Youtube", width=10, height=1, command=site3A)
B4A = Button(text="Google", width=10, height=1, command=site4A)
e = Entry(width=30)
b2=Button(text="SHOW", width=10, height=1, command=search)
B1A.place(x=10,y=80)
B2A.place(x=160,y=80)
B3A.place(x=10,y=40)
B4A.place(x=160,y=40)
e.place(x=40,y=130)
b2.place(x=85,y=150)
CAT.mainloop()
"""
#12 calculator
"""
from tkinter import *
CAT = Tk()
CAT.geometry("312x324")
CAT.title("Desktop Interface")
CAT.resizable(0, 0)  
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)
def bt_clear():
    global expression
    expression = ""
    input_text.set("")
def bt_equal():
    global expression
    result = str(eval(expression))  
    input_text.set(result)
    expression = ""
expression = ""
input_text = StringVar()
input_frame = Frame(tab4, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=500, bg="#eee", bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10, ipadx=20)
btns_frame = Frame(tab4, width=312, height=272.5, bg="grey")
btns_frame.pack()
clear = Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)
seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)
four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)
one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
             command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
              command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)
zero = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
               command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)
CAT.mainloop()
"""
#13 Restart Shutdown
"""
from tkinter import *
import os
CAT = Tk()
CAT.geometry("550x600+500+50")
CAT.title("Desktop Interface")
def ShutDown():
    return os.system("shutdown /s /t 1")
def Restart():
    return os.system("shutdown /r /t 1")
def Logout():
    return os.system("shutdown -l")
B1A = Button(text="ShutDown", width=10, height=1, command=ShutDown)
B2A = Button(text="Restart", width=10, height=1, command=Restart)
B3A = Button(text="Logout", width=10, height=1, command=Logout)
B1A.pack()
B2A.pack()
B3A.pack()
CAT.mainloop()
"""
#14 battery
"""
import psutil
from tkinter import messagebox
from tkinter import *
CAT = Tk()
CAT.geometry("550x600+500+50")
CAT.title("Desktop Interface")
def OPEN_VIDEO():
    battery = psutil.sensors_battery()
    present = str(battery.percent)
    messagebox.showinfo(title="Battery", message=("your laptop battery is: " + present + "% battery"))
buttom= Button(text='Battery Present',command=OPEN_VIDEO)
buttom.pack()
CAT.mainloop()

"""
#15 OPEN YOUTUBE VIDEO
"""
from tkinter import *
import pywhatkit as kit
CAT = Tk()
CAT.geometry("550x600+500+50")
CAT.title("Desktop Interface")
def OPEN_VIDEO():
    W = entry1.get()
    kit.playonyt(W)
def clear_text():
   entry1.delete(0, END)
entry1 = Entry(width=30)
ClearB = Button(text="Clear", command=clear_text, font=('Helvetica bold',10))
buttom= Button(text='OPEN VIDEO',command=OPEN_VIDEO)
entry1.pack()
buttom.pack()
ClearB.pack()
CAT.mainloop()

"""
#16 JPG TO PNG
"""
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=250, bg='lightsteelblue2', relief='raised')
canvas1.pack()
label1 = tk.Label(root, text='File Conversion Tool', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)
def getJPG():
    global im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)
browseButton_JPG = tk.Button(text="      Import JPG File     ", command=getJPG, bg='royalblue', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_JPG)
def convertToPNG():
    global im1
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)
saveAsButton_PNG = tk.Button(text='Convert JPG to PNG', command=convertToPNG, bg='royalblue', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_PNG)
root.mainloop()
"""