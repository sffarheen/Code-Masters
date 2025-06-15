
import tkinter as tk
from tkinter import *
import random
import sqlite3 
import time
from PIL import Image, ImageTk
def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    login.title('Code Master - Login')
    
    user_name = StringVar()
    password = StringVar()
    
    login_canvas = Canvas(login,width=720,height=440,bg="#a3e3f5")
    login_canvas.pack()

    

    heading = Label(login_canvas,text="Login",fg="#dc5b7a",bg="#a3e3f5")
    heading.config(font=('BrickSans 60 bold'))
    heading.place(x=260,y=15)

    #USER NAME
    ulabel = Label(login_canvas,text="Username",fg='black',bg='#a3e3f5')
    ulabel.place(relx=0.21,rely=0.4)
    uname = Entry(login_canvas,bg='white',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)

    #PASSWORD
    plabel = Label(login_canvas,text="Password",fg='black',bg="#a3e3f5")
    plabel.place(relx=0.215,rely=0.5)
    pas = Entry(login_canvas,bg='white',fg='black',textvariable = password,show="●")
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)

    def check():
        for a,b,e,d in logdata:
            if b == uname.get() and e == pas.get():
                print(logdata)
                
                menu(a)
                break
        else:
            error = Label(login_canvas,text="Wrong Username or Password!",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_canvas,text='Login',padx=5,pady=5,width=5,command=check,fg="black",bg="#a6a6a6")
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.6)
    
    
    login.mainloop()

def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    sup.title('Code Master - Sign up')
    
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    email = StringVar()
    
    
    sup_canvas = Canvas(sup,width=720,height=440,bg="#a3e3f5")
    sup_canvas.pack()

  

    heading = Label(sup_canvas,text=" SIGN UP",fg="#dc5b7a",bg="#a3e3f5")
    heading.config(font=('BrickSans 40 bold'))
    heading.place(x=240,y=15)
    sub=Label(sup_canvas,text="Your coding journey starts here \n  sign up today!! ",fg="black",bg="#a3e3f5")
    sub.config(font=('LuluFontTH 15'))
    sub.place(x=225,y=80)
    #full name
    flabel = Label(sup_canvas,text="Full Name",fg="black",bg="#a3e3f5")
    flabel.place(relx=0.21,rely=0.4)
    fname = Entry(sup_canvas,bg='white',fg='black',textvariable = fname)
    fname.config(width=42)
    fname.place(relx=0.31,rely=0.4)

    #username
    ulabel = Label(sup_canvas,text="Username",fg="black",bg="#a3e3f5")
    ulabel.place(relx=0.21,rely=0.5)
    user = Entry(sup_canvas,bg='white',fg='black',textvariable = uname)
    user.config(width=42)
    user.place(relx=0.31,rely=0.5)
    
    
    #password
    plabel = Label(sup_canvas,text="Password",fg="black",bg="#a3e3f5")
    plabel.place(relx=0.215,rely=0.6)
    pas = Entry(sup_canvas,bg='white',fg='black',textvariable = passW,show="●")
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.6)
    
    
    
    #country
    emaillabel = Label(sup_canvas,text="E-mail",fg="black",bg="#a3e3f5")
    emaillabel.place(relx=0.217,rely=0.7)
    e = Entry(sup_canvas,bg='white',fg='black',textvariable = email)
    e.config(width=42)
    e.place(relx=0.31,rely=0.7)
    def addUserToDataBase():
        
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        email = e.get()
        
        if len(fname.get())==0 and len(user.get())==0 and len(pas.get())==0 and len(e.get())==0:
            error = Label(text="You haven't enter any field...Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(fname.get())==0 or len(user.get())==0 or len(pas.get())==0 or len(e.get())==0:
            error = Label(text="Please Enter all the fields",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
            
        elif len(user.get()) == 0 and len(pas.get()) == 0:
            error = Label(text="Username and password can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)

        elif len(user.get()) == 0 and len(pas.get()) != 0 :
            error = Label(text="Username can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
        elif len(user.get()) != 0 and len(pas.get()) == 0:
            error = Label(text="Password can't be empty",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
        
        else:
        
            conn = sqlite3.connect('quiz.db')
            create = conn.cursor()
            create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text,EMAIL text)')
            create.execute("INSERT INTO userSignUp VALUES (?,?,?,?)",(fullname,username,password,email)) 
            conn.commit()
            create.execute('SELECT * FROM userSignUp')
            z=create.fetchall()
            print(z)
            #L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
            conn.close()
            loginPage(z)
        
    def gotoLogin():
        conn = sqlite3.connect('quiz database.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
    
    #signup BUTTON
    sp = Button(sup_canvas,text='SIGN UP',padx=5,pady=5,width=5,command = addUserToDataBase, bg="#a6a6a6",fg="black")
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_canvas,text='LOGIN',padx=5,pady=5,width=5,command = gotoLogin,bg="#a6a6a6", fg="black")
    log.configure(width = 16,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.393,rely=0.9)

    sup.mainloop()

def menu(abcdefgh):
    login.destroy()
    global menu 
    menu = Tk()
    menu.title('Code Masters- Menu')
    
    
    menu_canvas = Canvas(menu,width=720,height=440,bg="#a3e3f5")
    menu_canvas.pack()



    
    
    wel =Label(menu_canvas,text='WELCOME',fg="#6532ca",bg="#a3e3f5") 
    wel.config(font=('Aperture 40'))
    wel.place(x=230,y=15)

    name=Label(menu_canvas,text='Code Masters 💡🧐',fg="#dc5b7a",bg="#a3e3f5") 
    name.config(font=('Aperture 30'))
    name.place(x=200,y=80)
    
    abcdefgh='Hi! '+ abcdefgh
    level34 = Label(menu_canvas,text=abcdefgh,bg="#a3e3f5",font="LuluFontTH 20",fg="#ffea31")
    level34.place(x=50,y=130)

    begin = Label(menu_canvas,text="LETS BEGIN...",bg="#a3e3f5",font="Bicubik 10 bold",fg="#00bf63")
    begin.place(x=100,y=170)

    level = Label(menu_canvas,text="SELECT YOUR PROGRAMMING LANGUAGE",bg="#a3e3f5",fg="black",font="Aperture 18")
    level.place(x=130,y=200)
    
    
    var = IntVar()
    easyR = Radiobutton(menu_canvas,text='Python',bg="#a3e3f5",font="calibri 16",fg="black",value=1,variable = var)
    easyR.place(x=160,y=230)
    
    mediumR = Radiobutton(menu_canvas,text='Java',bg="#a3e3f5",font="calibri 16",fg="black",value=2,variable = var)
    mediumR.place(x=160,y=260)
    
    hardR = Radiobutton(menu_canvas,text='C',bg="#a3e3f5",font="calibri 16",fg="black",value=3,variable = var)
    hardR.place(x=160,y=290)
    
    
    def navigate():
        
        x = var.get()
        print(x)
        if x == 1:
            menu.destroy()
            easy()
        elif x == 2:
            menu.destroy()
            medium()
        
        elif x == 3:
            menu.destroy()
            difficult()
        else:
            pass
    letsgo = Button(menu_canvas,text="DIVE IN",bg="#a6a6a6",fg="black",font="calibri 12",command=navigate)
    letsgo.place(relx=0.25,rely=0.8)
    menu.mainloop()
def easy():
    
    global e
    e = Tk()
    e.title('Code Masters- python')
    
    easy_canvas =Canvas(e,width=720,height=440,bg="#a3e3f5")
    easy_canvas.pack()

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            easy_canvas.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
    global score
    score = 0
    
    easyQ = [
                 [
                     "What is the output of \n print(type([]))?",
                      "<class 'list'>",
                      "<class 'tuple'>", 
                      "<class 'dict'>", 
                      "<class 'set'>"
                 ] ,
                 [
                     "What will be the output of the following Python expression if the value of x is 34? \nprint(“%f”%x)" ,
                    "34.00",
                    "34.000000",
                    "34.0000",
                    "34.00000000"
                     
                 ],
                [
                    "What will be the value of X in the following Python expression? \nX = 2+9*((3*12)-8)/10" ,
                    "30.8",
                    "27.2",
                    "28.4",
                    "30.0"
                ],
                [
                    "Which of these in not a core data type?" ,
                    "Tuples",
                    "Dictionary",
                    "Lists",
                    "Class"
                ],
                [
                    "Which of the following represents the bitwise XOR operator?" ,
                    "&",
                    "!",
                    "^",
                    "|"
                ]
            ]
    answer = [
                "<class 'list'>",
                "34.000000",
                "27.2",
                "Class",
                "^"
             ]
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(easy_canvas,text =easyQ[x][0],font="calibri 12",bg="#a3e3f5",fg="black")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(easy_canvas,text=easyQ[x][1],font="calibri 10",value=easyQ[x][1],variable = var,bg="#BADA55")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(easy_canvas,text=easyQ[x][2],font="calibri 10",value=easyQ[x][2],variable = var,bg="#BADA55")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(easy_canvas,text=easyQ[x][3],font="calibri 10",value=easyQ[x][3],variable = var,bg="#BADA55")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(easy_canvas,text=easyQ[x][4],font="calibri 10",value=easyQ[x][4],variable = var,bg="#BADA55")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(e)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                e.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =easyQ[x][0])
            
            a.configure(text=easyQ[x][1],value=easyQ[x][1])
      
            b.configure(text=easyQ[x][2],value=easyQ[x][2])
      
            c.configure(text=easyQ[x][3],value=easyQ[x][3])
      
            d.configure(text=easyQ[x][4],value=easyQ[x][4])
            
            li.remove(x)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(easy_canvas,command=calc,text="Submit", bg="#a6a6a6", fg="black")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(easy_canvas,command=display,text="Next", bg="#a6a6a6", fg="black")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
   # pre=Button(easy_frame,command=display, text="Previous", fg="white", bg="black")
   # pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    e.mainloop()
    
    
def medium():
    
    global m
    m = Tk()
    m.title("Code Master-java")
    
    med_canvas = Canvas(m,width=720,height=440,bg="#a3e3f5")
    med_canvas.pack()

  
    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            med_canvas.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    
    mediumQ = [
                [
                   "Which keyword is used to inherit a class in Java?",
                     "implements", 
                     "extends", 
                     "inherits", 
                     "instanceof"
                ],
                [
                     "Which of these is not a primitive data type in Java?",
                       "int",
                       "boolean", 
                       "float", 
                       "String"
                ],
                [
                     "Which method is the entry point for any Java program?",
                      "start()", 
                      "init()", 
                      "main()", 
                      "run()"
                ],
                [
                     "What is the size of an int in Java?",
                      "4 bytes", 
                      "2 bytes", 
                      "8 bytes", 
                      "Depends on system"

                ],
                [
                    "Which of the following is invalid?",
                    "_a = 1",
                    "__a = 1",
                    "__str__ = 1",
                    "none of the mentioned"
                ], 
            ]
    answer = [
            "extends",
            "String",
            "main()",
            "4 bytes",
            "none of the mentioned"
            ]
    
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(med_canvas,text =mediumQ[x][0],font="calibri 12",bg="#a3e3f5")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(med_canvas,text=mediumQ[x][1],font="calibri 10",value=mediumQ[x][1],variable = var,bg="#a3e3f5")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(med_canvas,text=mediumQ[x][2],font="calibri 10",value=mediumQ[x][2],variable = var,bg="#a3e3f5")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(med_canvas,text=mediumQ[x][3],font="calibri 10",value=mediumQ[x][3],variable = var,bg="#a3e3f5")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(med_canvas,text=mediumQ[x][4],font="calibri 10",value=mediumQ[x][4],variable = var,bg="#a3e3f5")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(m)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                m.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =mediumQ[x][0])
            
            a.configure(text=mediumQ[x][1],value=mediumQ[x][1])
      
            b.configure(text=mediumQ[x][2],value=mediumQ[x][2])
      
            c.configure(text=mediumQ[x][3],value=mediumQ[x][3])
      
            d.configure(text=mediumQ[x][4],value=mediumQ[x][4])
            
            li.remove(x)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        if (var.get() in answer):
            score+=1
        display()
    
    submit = Button(med_canvas,command=calc,text="Submit", bg="#a6a6a6", fg="black")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(med_canvas,command=display,text="Next", bg="#a6a6a6", fg="black")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
   # pre=Button(med_frame,command=display, text="Previous", fg="white", bg="black")
   # pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    m.mainloop()
def difficult():
    
       
    global h
    #count=0
    h = Tk()
    h.title('Quiz App - Hard Level')
    
    hard_canvas = Canvas(h,width=720,height=440,bg="#a3e3f5")
    hard_canvas.pack()

    

    
    def countDown():
        check = 0
        for k in range(10, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            hard_canvas.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    
    hardQ = [
                [
       "Which of the following is a valid C variable name?",
         "int", 
         "float", 
         "total_score", 
         "char*"
    ],
    [
        "Which header file is needed for printf()",
        "<stdlib.h>", 
        "<conio.h>", 
        "<stdio.h>", 
        "<string.h>"
    ],
    [
     "Which of the following is a Python tuple?",
        "[1, 2, 3]",
        "(1, 2, 3)",
        "{1, 2, 3}",
        "{}"   
    ],
    [
        "What is returned by math.ceil(3.4)?",
        "3",
        "4",
        "4.0",
        "3.0"
    ],
    [
        "What will be the output of print(math.factorial(4.5))?",
        "24",
        "120",
        "error",
        "24.0"
    ] 
            
]
    answer = [
            "total_score",
            "in",
            "(1,2,3)",
            "4",
            "error"
            ]
    
    li = ['',0,1,2,3,4]
    x = random.choice(li[1:])
    
    ques = Label(hard_canvas,text =hardQ[x][0],font="calibri 12",bg="#A0DB8E")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(hard_canvas,text=hardQ[x][1],font="calibri 10",value=hardQ[x][1],variable = var,bg="#008080",fg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(hard_canvas,text=hardQ[x][2],font="calibri 10",value=hardQ[x][2],variable = var,bg="#008080",fg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(hard_canvas,text=hardQ[x][3],font="calibri 10",value=hardQ[x][3],variable = var,bg="#008080",fg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(hard_canvas,text=hardQ[x][4],font="calibri 10",value=hardQ[x][4],variable = var,bg="#008080",fg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(h)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                h.destroy()
                showMark(score)
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =hardQ[x][0])
            
            a.configure(text=hardQ[x][1],value=hardQ[x][1])
      
            b.configure(text=hardQ[x][2],value=hardQ[x][2])
      
            c.configure(text=hardQ[x][3],value=hardQ[x][3])
      
            d.configure(text=hardQ[x][4],value=hardQ[x][4])
            
            li.remove(x)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        global score
        #count=count+1
        if (var.get() in answer):
            score+=1
        display()
    
   # def lastPage():
    #    h.destroy()
     #   showMark()
    
    submit = Button(hard_canvas,command=calc,text="Submit", fg="white", bg="black")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(hard_canvas,command=display,text="Next", fg="white", bg="black")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    #pre=Button(hard_frame,command=display, text="Previous", fg="white", bg="black")
    #pre.place(relx=0.75, rely=0.82, anchor=CENTER)
    
   # end=Button(hard_frame,command=showMark(m), text="End", fg="white", bg="black")
    # end.place(relx=0.8, rely=0.82, anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    h.mainloop()

def showMark(mark):
    sh = Tk()
    sh.title('Code Masters - Marks')
    #heading = Label(login_canvas,text="Login",fg="#dc5b7a",bg="#a3e3f5")
    lab = Label(sh,text="Score-tastic!",fg="#dc5b7a")
    lab.config(font=('BrickSans 40 bold'))
    lab.pack()


    st = "You Got: \n"+str(mark)+"/5"
    mlabel = Label(sh,text=st,fg="black")
    mlabel.config(font=('BrickSans 30 bold'))
    mlabel.pack()
    
    def callsignUpPage():
        sh.destroy()
        start()
    
    def myeasy():
        sh.destroy()
        easy()
    
    b24=Button(text="Re-attempt", command=myeasy, bg="black", fg="white")
    b24.pack()
    
    from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
    from matplotlib.backend_bases import key_press_handler
    from matplotlib.figure import Figure

    import numpy as np

    fig = Figure(figsize=(5, 4), dpi=100)
    labels = 'Marks Obtained','Total Marks'
    sizes = [int(mark),5-int(mark)]
    explode = (0.1,0)
    fig.add_subplot(111).pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=0)
    

    canvas = FigureCanvasTkAgg(fig, master=sh)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    b23=Button(text="Sign Out",command=callsignUpPage,fg="black", bg="#a3e3f5")
    b23.pack()
    
    sh.mainloop()

def start():
    global root
    root = tk.Tk()
    root.title('Welcome To Code Master')

    img = Image.open("code masters image.png")
    photo = ImageTk.PhotoImage(img)
    # label = tk.Label(root, image=photo)
    # label.image = photo
    # label.pack(pady=20)
# label=CTkButton(app,text="submit",image=tryy,text_color="black",fg_color="white",width=200,height=100,anchor="center",compound="top")
# label.place(x=30,y=300)
    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    btn = tk.Button(root, text='THINK IT! CLICK IT! WIN IT! NOW-->',image=photo,command=signUpPage, bg="#a3e3f5", fg="black",anchor="center",compound="top")
    btn.config(width=screen_width, height=screen_height)
    btn.pack()

    root.mainloop()
    
if __name__=='__main__':
    start()
