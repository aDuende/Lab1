from tkinter import*
from tkinter import messagebox
 
def mainwindow():
    root = Tk()
    root.title("Sales Dashboard")
    root.geometry("900x650")
    root.configure(bg='#FFFFFF')
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=8)
    root.rowconfigure(2, weight=2)
    root.columnconfigure(0, weight=6)
    root.columnconfigure(1, weight=3)
    root.iconbitmap("CS311_Lab/img/git.png")
    return(root)
 
def createframe(root) :
    top = Frame(root,bg='#FFFFFF')
    top.rowconfigure(0,weight=1)
    top.columnconfigure((0,1),weight=1)
    top.grid(row=0,columnspan=2,sticky='news')
   
    left = Frame(root,bg='#FFFFFF')
    left.rowconfigure((0,1,2),weight=1)
    left.columnconfigure((0,1,2,3),weight=1)
    left.grid(row=1,column=0,sticky='news')
   
    right = Frame(root,bg='#4FBDBA')
    right.rowconfigure(0,weight=1)
    right.columnconfigure(0,weight=1)
    right.grid(row=1,column=1,sticky='news')
   
    bottom = Frame(root,bg='#53BCC4')                        
    bottom.rowconfigure(0,weight=1)
    bottom.columnconfigure((0,1,2,3),weight=1)    
    bottom.grid(row=2,columnspan=2,sticky='news')
     
    return(root, top, left, right, bottom)
 
def widgettop(top):
    head = Label(top,text="Sales Dashboard by Phakjira",bg="#A9DDFF",font=("Arial",14,"bold"))
    head.grid(row= 0 ,columnspan=2,sticky="news")
 
def widgetleft(left):
    box1= Text(left,width=55,height=30)
    box1= Text(left, width=18, height=7, bg='#28a745', fg='white', bd=0)
    box1.tag_config("tag-center-bold", justify='center',font=('Verdana',11,'bold'))
    box1.tag_config("tag-center", justify='center',font=('Verdana',10))
    box1.insert(INSERT, '\nRevenue\n', 'tag-center-bold')
    box1.insert(INSERT, '\n917,000\n', 'tag-center')
    box1.grid(row=0,column=0,sticky='nw',padx=1,pady=1)
    box1.config(state="disabled")
     
    box2= Text(left,width=55,height=30)
    box2= Text(left, width=18, height=7, bg='#FDED03', fg='white', bd=0)
    box2.tag_config("tag-center-bold", justify='center',font=('Verdana',11,'bold'))
    box2.tag_config("tag-center", justify='center',font=('Verdana',10))
    box2.insert(INSERT, '\nOrder\n', 'tag-center-bold')
    box2.insert(INSERT, '\n898\n', 'tag-center')
    box2.grid(row=0,column=1,sticky='n',padx=1,pady=1)
    box2.config(state="disabled")
 
    box3= Text(left,width=55,height=30)
    box3= Text(left,width=18, height=7, bg='#DA1B1B', fg='white', bd=0)
    box3.tag_config("tag-center-bold", justify='center',font=('Verdana',11,'bold'))
    box3.tag_config("tag-center", justify='center',font=('Verdana',10))
    box3.insert(INSERT, '\nAvg. Order Value\n', 'tag-center-bold')
    box3.insert(INSERT, '\n1,021\n', 'tag-center')
    box3.grid(row=0,column=2,sticky='n',padx=1,pady=1)
    box3.config(state="disabled")
 
    box4= Text(left,width=55,height=30)
    box4= Text(left, width=18, height=7, bg='#56E4FD', fg='white', bd=0)
    box4.tag_config("tag-center-bold", justify='center',font=('Verdana',11,'bold'))
    box4.tag_config("tag-center", justify='center',font=('Verdana',10))
    box4.insert(INSERT, '\nCustomers\n', 'tag-center-bold')
    box4.insert(INSERT, '\n819\n', 'tag-center')
    box4.grid(row=0,column=3,sticky='n',padx=1,pady=1)
    box4.config(state="disabled")

    name = Label(left,text="Top channel",font=("Arial",12,"bold"),bg="#FFFFFF") 
    name.grid(row=0,column=0,sticky="s")

    channelpic = Label(left,image=img1,bg="#FFFFFF")
    channelpic.grid(row=1,columnspan=2,sticky="n")

    name2 = Label(left,text="Best Seller",font=("Arial",12,"bold"),bg="#FFFFFF") 
    name2.grid(row=0,column=2,sticky="ws")

    newf = Label(left,bg="#FFFFFF")
    newf.grid(row=1,column=2,columnspan=2,sticky="news")

    topic1 = Label(newf,text="1.Le Chiquito Bag",font=("Arial",10),bg="#FFFFFF")
    topic1.grid(row=1,column=0,pady=5,sticky="w")
    topic2 = Label(newf,text="2. Fendi FF Mask",font=("Arial",10),bg="#FFFFFF")
    topic2.grid(row=2,column=0,pady=5,sticky="w")
    topic3 = Label(newf,text="3.Raito Racer Sneakers",font=("Arial",10),bg="#FFFFFF")
    topic3.grid(row=3,column=0,pady=5,sticky="w")
    topic4 = Label(newf,text="4.Carly Mini Bag",font=("Arial",10),bg="#FFFFFF")
    topic4.grid(row=4,column=0,pady=5,sticky="w")
    topic4 = Label(newf,text="5.Eva Shoulder Bag- Ivory Croc",font=("Arial",10),bg="#FFFFFF")
    topic4.grid(row=5,column=0,pady=5,sticky="w")

 
def widgetright(right):
    device = LabelFrame(right,text="Device",bg="#FFFFFF")
    device.grid(rowspan=2,column=0,sticky="news")
 
    devicepic = Label(right,image=img2,bg="#FFFFFF")
    devicepic.grid(row=0)

def widgetbottom(bottom):
    btn1 =Button(bottom,text="Click me 1",compound="center",bg="#53BCC4",border=0,image=img3,command=fnclick1)
    btn1.grid(row=0,column=0,sticky="w")
 
    btn2 =Button(bottom,text="Click me 2",compound="center",bg="#53BCC4",border=0,image=img3,command=fnclick2)
    btn2.grid(row=0,column=1,sticky="w")
 
    btn3 =Button(bottom,text="Click me 3",compound="center",bg="#53BCC4",border=0,image=img3,command=fnclick3)
    btn3.grid(row=0,column=2,sticky="w")

    btn4 =Button(bottom,text="Exit Program",compound="center",bg="#53BCC4",border=0,image=img3,command=quit)
    btn4.grid(row=0,column=3,sticky="w")
    
 

def fnclick1():
    messagebox.showinfo("Phakjira said", "Click Me 1 clicked")
def fnclick2():
    messagebox.showinfo("Phakjira said", "Click Me 2 clicked")
def fnclick3():
    messagebox.showinfo("Phakjira said", "Click Me 3 clicked")

root = mainwindow()
 
root,top,left,right,bottom = createframe(root)
img1 = PhotoImage(file="CS311_Lab/img/chanels.png")
img2 = PhotoImage(file="CS311_Lab/img/device.png")
img3 = PhotoImage(file="CS311_Lab/img/button.png")


widgettop(top)
widgetleft(left)
widgetright(right)
widgetbottom(bottom)
root.mainloop()