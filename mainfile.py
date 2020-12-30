import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
import random
import os
import text_to_speech as ts
import speech_recognition as sr
import tkinter.scrolledtext as scrolledtext
import mysql.connector
import database_credits as dc

data = mysql.connector.connect(
        host= 'localhost',
        user= 'root',
        password="",
        database = "chatbot_final"
)

cur = data.cursor()

windoww = tk.Tk()
windoww.title("login")
windoww.configure(bg="black")

canvas = Canvas(windoww, width=340, height=200)
canvas.configure(bg="black")

canvas.pack(padx=4, pady=4)
img = ImageTk.PhotoImage(Image.open("elsa1.png "))
canvas.create_image(20, 20, anchor=NW, image=img)

email_id = 0
password = 0

def signup():
    windoww.withdraw()
    win = Toplevel(windoww)
    win.title("Registration form")
    win.geometry('400x400')
    win.configure(background="#d1ffeb")

    def submit():
        firstname = str(fname.get())
        lastname = str(lname.get())
        emailUser = str(email.get())
        passwordUser = str(passwod.get())
        contact_no = int(num.get())
        planUser = str(plan.get())

        if((firstname, lastname, emailUser, passwordUser, contact_no, planUser == "") and contact_no == 0):
            messagebox.showinfo("alert", "any field must not be empty")
            windoww.deiconify()
            win.destroy()
        else:
            dc.credit(firstname, lastname, emailUser, passwordUser, contact_no, planUser)
            clr()
            windoww.deiconify()
            win.destroy()
            messagebox.showinfo("submit", "YOUR RESPONSE HAVE BEEN SUBMITED")

    def clr():
        clearscreen = ""
        fname.set(clearscreen)
        lname.set(clearscreen)
        email.set(clearscreen)
        passwod.set(clearscreen)
        num.set(clearscreen)
        plan.set(clearscreen)

    fname = StringVar()
    lname = StringVar()
    email = StringVar()
    passwod = StringVar()
    num = IntVar()
    plan = StringVar()

    title = Label(win, text="First Time Registration", bg="white", borderwidth=2, relief="groove",
                  font=("Times", 22, "bold")).grid(row=0, column=0, ipadx=2, ipady=2, padx=20, pady=20, columnspan=2)
    a = Label(win, text="First Name :", bg="white", fg="black").grid(row=1, column=0, padx=5, pady=5)
    b = Label(win, text="Last Name :", bg="white").grid(row=2, column=0, padx=5, pady=5)
    c = Label(win, text="Email Id :", bg="white").grid(row=3, column=0, padx=5, pady=5)
    d = Label(win, text="password :", bg="white").grid(row=4, column=0, padx=5, pady=5)
    e = Label(win, text="Contact No :", bg="white").grid(row=5, column=0, padx=5, pady=5)
    f = Label(win, text="Current Plan :", bg="white").grid(row=6, column=0, padx=5, pady=5)

    a1 = Entry(win, textvariable=fname).grid(row=1, column=1, padx=5, pady=5)
    b1 = Entry(win, textvariable=lname).grid(row=2, column=1, padx=5, pady=5)
    c1 = Entry(win, textvariable=email).grid(row=3, column=1, padx=5, pady=5)
    d1 = Entry(win, textvariable=passwod).grid(row=4, column=1, padx=5, pady=5)
    e1 = Entry(win, textvariable=num).grid(row=5, column=1, padx=5, pady=5)
    f1 = Entry(win, textvariable=plan).grid(row=6, column=1, padx=5, pady=5)

    button1 = Button(win, text="Submit", command=submit, width=10, bg="red", fg="white").grid(row=7, column=0, padx=5,
                                                                                              pady=5)
    button2 = Button(win, text="clear", command=clr, width=10, bg="yellow").grid(row=7, column=1, padx=5, pady=5)

    win.mainloop()

def login():
    windoww.withdraw()

    def mainwindow():
        winn.withdraw()

        try:
            qq = "select email,password from user where email = %s"
            email = emid.get()
            cur.execute(qq, (email,))
            v = cur.fetchone()
            email_user = v[0]
            password_user = v[1]

            if ((email_user == emid.get()) and (password_user == passs.get())):
                window = Toplevel(windoww)
                def clear():  # clear in menu bar
                    txt.delete(1.0, END)

                def search():  # search in menu bar
                    nroot = Toplevel(window)
                    nroot.title("Search")
                    nroot.configure(bg='light blue')
                    ee2 = Entry(nroot, width=65, bd=3)
                    ee2.insert(0, 'Search previous message..')
                    ee2.pack()

                    def abc():
                        messagebox.showinfo("search command", "searching")
                        txt.tag_remove('found', '1.0', END)
                        s = ee2.get()
                        if s:
                            idx = '1.0'
                            while 1:
                                idx = txt.search(s, idx, nocase=1, stopindex=END)
                                if not idx: break
                                lastidx = '%s+%dc' % (idx, len(s))
                                txt.tag_add('found', idx, lastidx)
                                idx = lastidx
                        txt.tag_config('found', foreground='red')

                    btn5 = Button(nroot, bg="#009688", text='Search', fg="white", width=10, command=abc).pack()
                    nroot.mainloop()  # search block ends here

                def window1():  # maths tab start here
                    root = Toplevel(window)
                    root.title("MATHS")
                    root.configure(bg='light blue')
                    v = StringVar()
                    display = StringVar()

                    def answer():
                        showValue = v.get()
                        answer = str(eval(showValue))
                        display.set(answer)

                    def clr():
                        clearscreen = ""
                        v.set(clearscreen)
                        display.set(clearscreen)

                    l1 = Label(root, text="EXPRESSION: ", bg="white").grid(row=0, column=0, padx=10, pady=10)
                    l2 = Label(root, text="ANSWER", bg="white").grid(row=1, column=0, padx=10, pady=10)
                    entry1 = Entry(root, width=30, textvariable=v).grid(row=0, column=1, padx=10, pady=10)
                    entry2 = Entry(root, width=30, textvariable=display).grid(row=1, column=1, padx=10, pady=10)
                    btn1 = Button(root, text="View Answer", command=answer, bg="light green")
                    btn1.grid(row=3, column=0, padx=10, pady=10)
                    btn2 = Button(root, text="clear", command=clr, bg="red").grid(row=3, column=1, padx=10, pady=10)

                    root.mainloop()  # math tab ends here

                # chat screen starts
                # greeting_list = ["hello", "hello,how are you", "good day", "how are you", "nice to meet you"]
                # greeting_reply = ["Hello iam  a chatbot", "Hello sir or maam", "Today i welcome you"]
                # website_link = ["www.google.com", "www.youtube.com", "www.yahoo.com", "www.amazon.com", "www.gmail.com"]

                window.geometry("390x630")
                window.title("heyyy!! I am a chatbot")
                window.configure(bg='black')

                def show(e):
                    try:
                        text = str(value.get())
                        tolower = text.lower()
                        toreplace = tolower.replace("-", " ")
                        send = "Me:- {}".format(toreplace)
                        txt.insert(END, "\n" + send)
                        mylist = []
                        qq = "select * from infotable where question = %s"
                        cur.execute(qq, (toreplace,))
                        v = cur.fetchall()
                        v0 = v[0][0]
                        v1 = v[0][1]
                        v2 = v[0][2]
                        v3 = v[0][3]
                        mylist.append(v1)
                        mylist.append(v2)
                        mylist.append(v3)

                        if (toreplace in v0):
                            randomvalue = random.choice(mylist)
                            txt.insert(END, "\n" + "Elsa:- {}".format(randomvalue))
                            ts.speak(randomvalue)
                            os.remove("voice.mp3")
                    except:
                        if(toreplace == "clear the screen"):
                            txt.delete(1.0, END)
                            ts.speak("Screen cleared")
                            os.remove("voice.mp3")
                        elif(toreplace == "exit"):
                            txt.insert(END, "\n" + "Elsa:- thank you for the support")
                            ts.speak("thank you for the support")
                            os.remove("voice.mp3")
                            windoww.quit()
                        else:
                            txt.insert(END, "\n" + "Elsa:- Woah, what are you typing?")
                            ts.speak("woah what are you typing")
                            os.remove("voice.mp3")
                    value.set("")
                    txt.yview(END)

                menubar = Menu(window)
                optionmenu = Menu(menubar, tearoff=0)
                optionmenu.add_command(label="clear", command=clear)
                optionmenu.add_command(label="search", command=search)
                optionmenu.add_command(label='send', command=show)
                # optionmenu.add_command(label="Save")
                optionmenu.add_separator()
                optionmenu.add_command(label="Exit", command=window.quit)
                menubar.add_cascade(label="Option", menu=optionmenu)

                perksmenu = Menu(menubar, tearoff=0)
                perksmenu.add_command(label="Maths", command=window1)
                # perksmenu.add_command(label="Daily news")
                # perksmenu.add_command(label="about")
                menubar.add_cascade(label="perks", menu=perksmenu)

                window.config(menu=menubar)



                def clear():
                    txt.delete(1.0, END)

                def voice():
                    try:
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print("Speak anything")
                            audio = r.listen(source)
                            text = r.recognize_google(audio)
                            tolower = text.lower()
                            toreplace = tolower.replace("-", " ")
                            print(text)
                            txt.insert(END, "\n" + "Me:- {}".format(toreplace))
                            mylist = []
                            qq = "select * from infotable where question = %s"
                            cur.execute(qq, (toreplace,))
                            v = cur.fetchall()
                            v0 = v[0][0]
                            v1 = v[0][1]
                            v2 = v[0][2]
                            v3 = v[0][3]
                            mylist.append(v1)
                            mylist.append(v2)
                            mylist.append(v3)
                            if (toreplace in v0):
                                randomvalue = random.choice(mylist)
                                txt.insert(END, "\n" + "Elsa:- {}".format(randomvalue))
                                ts.speak(randomvalue)
                                os.remove("voice.mp3")

                    except:
                        if (text == "clear the screen"):
                            txt.delete(1.0, END)
                            ts.speak("Screen cleared")
                            os.remove("voice.mp3")
                        elif(text == "exit"):
                            txt.insert(END, "\n" + "Elsa:- thank you for the support")
                            ts.speak("thank you for the support")
                            os.remove("voice.mp3")
                            windoww.quit()
                        else:
                            txt.insert(END, "\n" + "Elsa:- Woah what are saying")
                            ts.speak("woah what are you saying")
                            os.remove("voice.mp3")

                value = StringVar()
                label = Label(window, text="Elsa", bg="black", fg="white", font=("Lobster", 20, "bold"))
                label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

                txt = scrolledtext.ScrolledText(window, undo=True, bg="light yellow", height=25, bd=5, width=39)
                txt['font'] = ('consolas', '12')
                txt.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

                e1 = Entry(window, textvariable=value, width=45, bd=3)
                e1.focus_set()
                e1.insert(0, 'Type a message...')
                e1.grid(row=3, column=0, padx=2, pady=2,ipady=17)
                # btn = Button(window, text="send", bg="red", fg="white", width=6, command=show)
                # btn.grid(row=3, column=1, padx=2, pady=2)
                btn2 = Button(window, text="VOICE",font=("lobster",12), bg="red",fg="white", width=12, command = voice)
                btn2.grid(row=3, column=3,padx=2,pady=2,ipady=8)

                e1.bind("<Return>" , show)

                window.maxsize(390,630)
                # winn.destroy()
                print("Window Displaying...")
                window.mainloop()
                windoww.destroy()
                print("window stopped")

            else:
                messagebox.showinfo("Login failed","no user found!")

                print("oops")
        except:
            if((emid.get()== "") and (passs.get()=="")):
                messagebox.showinfo("No Input?","Please Enter Your Details!")
                winn.quit()
                windoww.deiconify()
                print("oops")

            else:
                messagebox.showinfo("Login failed", "no user found!")
                winn.quit()
                windoww.deiconify()
                print("oops")


    winn = Toplevel(windoww)
    winn.title("login-page")
    winn.configure(bg='black')

    emid = StringVar()
    passs = StringVar()

    def cllr():
        cllrscr = ""
        emid.set(cllrscr)
        passs.set(cllrscr)


    l0 = Label(winn, text="-----------Please Log in-----------", fg="yellow", bg="black", font=("Lobster", 13, "bold"))
    l0.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
    l1 = Label(winn, text="Email: ", bg="white").grid(row=1, column=0, padx=10, pady=10, sticky=W)
    l2 = Label(winn, text="Password: ", bg="white").grid(row=2, column=0, padx=10, pady=10, sticky=W)

    entry1 = Entry(winn, width=30, textvariable=emid).grid(row=1, column=1, padx=10, pady=10)
    entry2 = Entry(winn, width=30, textvariable=passs).grid(row=2, column=1, padx=10, pady=10)

    btn1 = ttk.Button(winn, text="Log in", command=mainwindow).grid(row=3, column=0, padx=10, pady=10)
    btn2 = ttk.Button(winn, text="clear", command=cllr).grid(row=3, column=1, padx=10, pady=10)


    winn.mainloop()

b1 = ttk.Button(windoww, text="Login", command=login).pack(padx=4, pady=4)
b2 = ttk.Button(windoww, text="signup", command=signup).pack(padx=4, pady=4)

windoww.mainloop()
