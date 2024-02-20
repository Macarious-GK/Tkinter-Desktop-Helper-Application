from tkinter import *
from pyautogui import screenshot as SShot
from textblob import *
from tkcalendar import *
from tkinter import ttk
import time
from webbrowser import open as pen
from translate import Translator
from os import system
from psutil import sensors_battery
from pywhatkit import playonyt
from PIL import Image
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import *
#####################################################################################################(Window)
CAT = Tk()
CAT.geometry("550x600+500+50")
CAT.resizable(0,0 )
CAT.title("Desktop Interface")
#####################################################################################################(Note, tabs)
note = ttk.Notebook(CAT)
tab1 = Frame(note)
tab2 = Frame(note)
tab3 = Frame(note)
tab4 = Frame(note)
note.add(tab1, text='Home')
note.add(tab2, text='Tools')
note.add(tab3, text='Time')
note.add(tab4, text='Calculator')
note.pack()
Photo1 = PhotoImage(file="14.png")
label1 = Label(tab1, image=Photo1).pack()
Photo2 = PhotoImage(file="12.png")
label2 = Label(tab2, image=Photo2).pack()
Photo3 = PhotoImage(file="2.png")
label3 = Label(tab3, image=Photo3).pack()
#####################################################################################################
# PAGE '1' "start"
Label101 = Label(tab1, text="***************************************************************************************************************************", width=70, height=1, font=10, bd=5, bg="sandy brown", fg="black")
Label101.place(x=0, y=420)
Label102 = Label(tab1, text="***************************************************************************************************************************", width=70, height=1, font=10, bd=5, bg="steel blue", fg="black")
Label102.place(x=0, y=190)
label105 = Label(tab1, text='Website Search', bg='coral3')
label105.config(font=('helvetica', 20))
label105.place(x=00, y=0)
label107 = Label(tab1, text='Search', bg='sky blue')
label107.config(font=('helvetica', 20))
label107.place(x=360, y=280)
label108 = Label(tab1, text='URL Downloader', bg='sky blue')
label108.config(font=('helvetica', 20))
label108.place(x=10, y=280)
label104 = Label(tab1, text='Youtube ', bg='steel blue')
label104.config(font=('helvetica', 20))
label104.place(x=00, y=215)
label103 = Label(tab1, text='File Conversion Tool', bg='dark orange')
label103.config(font=('helvetica', 20))
label103.place(x=110, y=460)
#####################################################################################################(Website)
def site1A():
    pen("http://courses.nu.edu.eg/")
def site2A():
    pen("https://outlook.office.com/mail/inbox")
def site3A():
    pen("https://www.youtube.com/")
def site4A():
    pen("www.google.com")
def search():
    t = e101.get()
    pen(t)
def clear_text1():
   e101.delete(0, END)
B1A = Button(tab1, text="NU.Courses", bg='salmon1', fg='white', bd=5, font=('helvetica', 12, 'bold'), activebackground="green", cursor="hand2", command=site1A)
B2A = Button(tab1, text="OutLook", bg='salmon1', fg='white', bd=5, font=('helvetica', 12, 'bold'), activebackground="green", cursor="hand2", command=site2A)
B3A = Button(tab1, text="Youtube", bg='salmon1', fg='white', bd=5, font=('helvetica', 12, 'bold'), activebackground="green", cursor="hand2", command=site3A)
B4A = Button(tab1, text="Google", bg='salmon1', fg='white', bd=5, font=('helvetica', 12, 'bold'), activebackground="green", cursor="hand2", command=site4A)
C1 = Button(tab1, text="Clear", command=clear_text1, bg='salmon1', bd=5, fg='white', font=('helvetica', 12, 'bold'), activebackground="firebrick1", cursor="hand2")
e101 = Entry(tab1, width=30, borderwidth=5)
b2 = Button(tab1, text="SHOW", bg='salmon1', fg='white', bd=5, font=('helvetica', 12, 'bold'), activebackground="green", cursor="hand2", command=search)
B1A.place(x=400, y=70)
B2A.place(x=290, y=140)
B3A.place(x=420, y=140)
B4A.place(x=290, y=70)
e101.place(x=10, y=90)
C1.place(x=150, y=130)
b2.place(x=30, y=130)
#####################################################################################################(Youtube)
def DOWNLOAD():
    url = entry101.get()
    download = url[:12] + 'ss' + url[12:]
    pen(download)
def clear_text2():
   entry101.delete(0, END)
def OPEN_VIDEO():
    W = entry102.get()
    playonyt(W)
def clear_text3():
   entry102.delete(0, END)
entry102 = Entry(tab1, width=30, borderwidth=5)
ClearB2 = Button(tab1, text="Clear", command=clear_text3, bd=4, bg='steel blue', activebackground="firebrick1", cursor="hand2", fg='white',font=('helvetica', 12, 'bold'))
buttom101 = Button(tab1, text='Search', command=OPEN_VIDEO, bd=4, bg='steel blue', activebackground="green", cursor="hand2", fg='white',font=('helvetica', 12, 'bold'))
entry101 = Entry(tab1, width=30, borderwidth=5)
ClearB1 = Button(tab1, text="Clear", command=clear_text2, bd=4, bg='steel blue', fg='white',font=('helvetica', 12, 'bold'), activebackground="firebrick1", cursor="hand2", )
buttom100 = Button(tab1, text='Download', command=DOWNLOAD, bd=4, bg='steel blue', fg='white',font=('helvetica', 12, 'bold'), activebackground="green", cursor="hand2", )
entry101.place(x=10, y=330)
buttom100.place(x=30, y=370)
ClearB1.place(x=150, y=370)
entry102.place(x=300, y=330)
buttom101.place(x=300, y=370)
ClearB2.place(x=470, y=370)
#####################################################################################################(File Conversion Tool)
def getJPG():
    global im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)
browseButton_JPG = Button(tab1, text="    Import JPG File    ", command=getJPG, bd=5, activebackground="green", cursor="hand2", bg='sandy brown', fg='white', font=('helvetica', 12, 'bold'))
browseButton_JPG.place(x=30, y=520)
def convertToPNG():
    global im1
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)
saveAsButton_PNG = Button(tab1, text='Convert JPG to PNG', command=convertToPNG, bd=5, activebackground="green", cursor="hand2", bg='sandy brown', fg='white', font=('helvetica', 12, 'bold'))
saveAsButton_PNG.place(x=300, y=520)
# PAGE '1' "end"
#####################################################################################################
# PAGE '2' "start"
Label201 = Label(tab2, text="===========================================================================================================", width=70, height=1, font=10, bd=5, bg="cornsilk4", fg="black")
Label202 = Label(tab2, text="===========================================================================================================", width=70, height=1, font=10, bd=5, bg="slate blue", fg="black")
label203 = Label(tab2, text='Translator', bg='dodger blue')
label204 = Label(tab2, text='Corrector', bg='dodger blue')
label205 = Label(tab2, text='Screenshot', bg='slate blue')
label206 = Label(tab2, text='Battery', bg='slate blue')
label207 = Label(tab2, text='Laptop Switches', bg='cornsilk4')
label203.config(font=('helvetica', 20))
label204.config(font=('helvetica', 20))
label205.config(font=('helvetica', 20))
label206.config(font=('helvetica', 20))
label207.config(font=('helvetica', 20))
Label201.place(x=0, y=380)
Label202.place(x=0, y=200)
label203.place(x=400, y=0)
label204.place(x=0, y=0)
label205.place(x=40, y=230)
label206.place(x=340, y=230)
label207.place(x=150, y=410)
#####################################################################################################(Translate)
def Translate():
    W = entry201.get()
    s = Translator(from_lang="english", to_lang="Arabic")
    res = s.translate(W)
    messagebox.showinfo(title="Translation", message=res)
def clear_text4():
   entry201.delete(0, END)
entry201 = Entry(tab2, width=30, borderwidth=5)
ClearB201 = Button(tab2, text="Clear", command=clear_text4, bg='dodger blue', bd=3, fg='white',activebackground="firebrick1", cursor="hand2", font=('helvetica', 14, 'bold'))
buttom201 = Button(tab2, text='Tranclate', command=Translate, bg='dodger blue', bd=3, fg='white',activebackground="green", cursor="hand2", font=('helvetica', 14, 'bold'))
entry201.place(x=290, y=90)
buttom201.place(x=300, y=140)
ClearB201.place(x=450, y=140)
#####################################################################################################(Corrector)
def correct():
    a = entry202.get()
    b = TextBlob(a)
    messagebox.showinfo(title="Corrected word", message="correct word is: "+str(b.correct()))
buttom204= Button(tab2, text='Correct',command=correct, bg='dodger blue', fg='white', bd=3, activebackground="green", cursor="hand2" , font=('helvetica', 14, 'bold'))
def clear_text5():
   entry202.delete(0, END)
entry202 = Entry(tab2, width=30, borderwidth=5)
ClearB202 = Button(tab2, text="Clear", command=clear_text5, bg='dodger blue', bd=3, fg='white',activebackground="firebrick1", cursor="hand2" , font=('helvetica', 14, 'bold'))
entry202.place(x=10, y=90)
buttom204.place(x=10, y=140)
ClearB202.place(x=150, y=140)
#####################################################################################################(Battery)
def battery():
    battery1 = sensors_battery()
    present = str(battery1.percent)
    messagebox.showinfo(title="Battery", message=("your laptop battery is: " + present + "% battery"))
buttom203= Button(tab2, text='Battery Present',command=battery, bg='slate blue', fg='white', bd=5, activebackground="green", cursor="hand2" , font=('helvetica', 14, 'bold'))
buttom203.place(x=300, y=300)
#####################################################################################################(Screenshot)
def takescreenshot():
    myscreenshot = SShot()
    save_path = asksaveasfilename()
    myscreenshot.save(save_path+'_screenshot2.png')
    messagebox.showinfo(title="Screenshot", message=("Screenshot is saved"))
button202 = Button(tab2, text='take screenshot', command=takescreenshot, bg='slate blue', bd=5, fg='white', activebackground="green", cursor="hand2" ,font=('helvetica', 14, 'bold'))
button202.place(x=30, y=300)
#####################################################################################################(Shutdown, Restart, Logout)
def ShutDown():
    return system("shutdown /s /t 1")
def Restart():
    return system("shutdown /r /t 1")
def Logout():
    return system("shutdown -l")
B201A = Button(tab2, text="ShutDown", width=10, height=2, bd=10, fg="black", bg='cornsilk4', activebackground="green", cursor="hand2" , font=('Helvetica bold',15), command=ShutDown)
B202A = Button(tab2, text="Restart", width=10, height=2, bd=10, fg="black", bg='cornsilk4', activebackground="green", cursor="hand2" , font=('Helvetica bold',15), command=Restart)
B203A = Button(tab2, text="Logout", width=10, height=2, bd=10, fg="black", bg='cornsilk4', activebackground="green", cursor="hand2" , font=('Helvetica bold',15), command=Logout)
B201A.place(x=10, y=470)
B202A.place(x=190, y=470)
B203A.place(x=370, y=470)
# PAGE '2' "end"
#####################################################################################################
# PAGE '3' "start"
Label301 = Label(tab3, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", width=70, height=1, font=10, bd=5, bg="salmon1", fg="black")
Label301.place(x=0, y=320)
Label302 = Label(tab3, text="Task Alarm", bd=5, bg="salmon1")
Label302.config(font=('helvetica', 20))
Label302.place(x=170, y=350)
Label303 = Label(tab3, text="Task", bd=5, bg="cyan")
Label303.config(font=('helvetica', 10))
Label303.place(x=10, y=420)
Label304 = Label(tab3, text="Min", bd=2, bg="cyan")
Label304.config(font=('helvetica', 10))
Label304.place(x=400, y=425)
#####################################################################################################(Calendar)
def selectdata():
    myDate=mycal.get_date()
    messagebox.showinfo(title="SelectedDate", message="The date is: "+myDate)
mycal=Calendar(tab3, setmode="day", date_pattern="d/m/yy")
mycal.place(x=50, y=60)
open_cal = Button(tab3, text='select date',width=10, height=1, bd=10, fg="black", bg='mediumpurple1', activebackground="green", cursor="hand2" , font=('Helvetica bold',15), command=selectdata)
open_cal.place(x=360, y=120)
#####################################################################################################(Clock)
def get_time():
    timevar = time.strftime("%I:%M:%S %p")
    clock.config(text=timevar)
    clock.after(200, get_time)
clock = Label( tab3, font=("ds-digital",30,'bold'),bd=5, bg='black',fg='cyan')
clock.place(x=250, y=510)
get_time()
#####################################################################################################(Reminder)
def actual_time():
    text = e301.get()
    local_time = e302.get()
    local_time = eval(local_time) * 60
    time.sleep((local_time))
    messagebox.showinfo(title="Reminder", message="Time is up: " + "'" + text + "'")
def clear_text6():
   e301.delete(0, END)
   e302.delete(0, END)
b301 = Button(tab3, text='Remind Me',command=actual_time, bg='mediumpurple1', fg='black', bd=3, activebackground="green", cursor="hand2" , font=('helvetica', 16, 'bold'))
b302 = Button(tab3, text='CLEAR',command=clear_text6, bg='mediumpurple1', fg='black', bd=3, activebackground="RED", cursor="hand2" , font=('helvetica', 8, 'bold'))
b302.place(x=470, y=450)
b301.place(x=40, y=500)
e301 = Entry( tab3, width=50, borderwidth=5)
e301.place(x=10, y=450)
e302 = Entry(tab3,  width=5, borderwidth=5)
e302.place(x=400, y=450)
# PAGE '3' "end"
#####################################################################################################
# PAGE '4' "Start"
Label401 = Label(tab4, width=70, height=1000, bg="sandy brown")
Label401.place(x=0, y=0)
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
input_frame = Frame(tab4, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",highlightthickness=2)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=20, bg="#eee", bd=0,justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10, ipadx=20)
btns_frame = Frame(tab4, width=312, height=272.5, bg="grey")
btns_frame.pack()
clear = Button(btns_frame, text="C", fg="black", width=35, height=3, bg='steelblue', bd=5, cursor="hand2",command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bg='pink3', bd=4, cursor="hand2",command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)
seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bg='salmon1', bd=4, cursor="hand2",command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bg='cornsilk4', bd=4, cursor="hand2",command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bg='salmon1', bd=4, cursor="hand2",command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bg='GREEN', bd=4, cursor="hand2",command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)
four = Button(btns_frame, text="4", fg="black", width=10, height=3, bg='cornsilk4', bd=4, cursor="hand2",command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text="5", fg="black", width=10, height=3,bg='goldenrod2', bd=4, cursor="hand2",command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text="6", fg="black", width=10, height=3, bg='cornsilk4', bd=4, cursor="hand2",command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bg='red4', bd=4, cursor="hand2",command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)
one = Button(btns_frame, text="1", fg="black", width=10, height=3, bg='salmon1', bd=4, cursor="hand2",command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text="2", fg="black", width=10, height=3, bg='cornsilk4', bd=4, cursor="hand2",command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text="3", fg="black", width=10, height=3, bg='salmon1', bd=4, cursor="hand2",command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bg='royalblue', bd=4, cursor="hand2",command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)
zero = Button(btns_frame, text="0", fg="black", width=23, height=3, bg='slate blue', bd=4, cursor="hand2",command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = Button(btns_frame, text=".", fg="black", width=10, height=3, bg='dark turquoise', bd=4, cursor="hand2",command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
equals = Button(btns_frame, text="=", bg='black', bd=4, fg="white", width=10, height=3, cursor="hand2",command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)
# PAGE '4' "end"
CAT.mainloop()
