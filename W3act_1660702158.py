from tkinter import*
from tkinter import messagebox
 
def mainwindow():  
    root = Tk()
    root.title("GUI2: Design layout using Frame by Phakjira")
    root.geometry("600x500")
    root.configure(bg='lightgreen')
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=4)
    root.rowconfigure(2, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=4)
    return(root)
 
def createframe(root) :
    top = Frame(root,bg='#35858B') # กำหนด Frame top บน root
    top.rowconfigure(0,weight=1) # กำหนด top เป็น 1 rows
    top.columnconfigure((0,1),weight=1) # แบ่ง top เป็น 2 column
    top.grid(row=0,columnspan=2,sticky='news') # grid top บน root
    
    left = Frame(root,bg='#AEFEFF')
    left.rowconfigure((0,1,2),weight=1) # แบ่ง left เป็น 3 rows
    left.columnconfigure(0,weight=1) # แบ่ง left เป็น 3 column
    left.grid(row=1,column=0,sticky='news') # grid left บน root
    
    right = Frame(root,bg='#4FBDBA')
    right.rowconfigure((0,1,2),weight=1) # แบ่ง right เป็น 3 rows
    right.columnconfigure(0,weight=1) # แบ่ง right เป็น 3 column
    right.grid(row=1,column=1,sticky='news') # grid right บน root
    
    bottom = Frame(root,bg='#35858B')
    bottom.rowconfigure(0,weight=1) # แบ่ง bottom เป็น 1 rows
    bottom.columnconfigure(0,weight=1) # แบ่ง bottom เป็น 1 column     
    bottom.grid(row=2,columnspan=2,sticky='news') # grid bottom บน root
     
    return(root, top, left, right, bottom)
 
def widgettop(top):
    btn1 = Button(top, text="Click Me1",image =img1,compound='top',command=fnclick)
    btn1.grid(row=0, column=0,ipadx=20)
    btn2 = Button(top, text="Exit",image =img2,compound='top',command=quit)
    btn2.grid(row=0, column=1,ipadx=20)
 
def widgetleft(left):
    tag1 =Label(left,image=img3,bg="#AEFEFF")
    tag1.grid(row=0)
    tag2 =Label(left,image=img4,bg="#AEFEFF")
    tag2.grid(row=1)
    tag3 =Label(left,image=img5,bg="#AEFEFF")
    tag3.grid(row=2)
 
def widgetright(right):
    btn1 =Button(right,text="Select book1",command=fnclick1)
    btn1.grid(row=0,sticky="w",padx=20,ipadx=15,ipady=15)
 
    btn2 =Button(right,text="Select book2",command=fnclick2)
    btn2.grid(row=1,sticky="w",padx=20,ipadx=15,ipady=15)
 
    btn3 =Button(right,text="Select book3",command=fnclick3)
    btn3.grid(row=2,sticky="w",padx=20,ipadx=15,ipady=15)
 
def widgetbottom(bottom):
    lb1 = Label(bottom,text="Copyrights 2024 by Phakjira")
    lb1.grid(row=0,sticky="news")
 
def fnclick():
    messagebox.showinfo("xxx said", "Click me1 click")
def fnclick1():
    messagebox.showinfo("Admin", "Selected book1")
def fnclick2():
    messagebox.showinfo("Admin", "Selected book2")
def fnclick3():
    messagebox.showinfo("Admin", "Selected book3")
 
root = mainwindow()
img1 = PhotoImage(file='Picture/icon1.png')
img2 = PhotoImage(file='Picture/icon2.png')
img3 = PhotoImage(file="Picture/book1.png")
img4 = PhotoImage(file="Picture/book2.png")
img5 = PhotoImage(file="Picture/book3.png")
img6 = PhotoImage(file="Picture/flower2.png")
 
root,top,left,right,bottom = createframe(root)
widgettop(top)
widgetleft(left)
widgetright(right)
widgetbottom(bottom)
 
 
root.mainloop()