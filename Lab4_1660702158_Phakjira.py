from tkinter import *
from tkinter import ttk
def mainwindow() :#CreaTE Frame
    root = Tk()
    root.title("GUI3: Class Activity of Week4")
    root.geometry("800x600")
    root.configure(bg='lightgreen')
    root.option_add('*font', 'Calibri 14')
    img_icon = PhotoImage(file="CS311_Lab\W4\images\cart.png")
    root.iconphoto(False,img_icon)
    
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=4)
    root.rowconfigure(2,weight=1)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=3)
    return(root)

def createframe(root) :
    top = Frame(root,bg='#FFDEFF')
    top.rowconfigure(0,weight=1)
    top.columnconfigure(0,weight=1)
    top.grid(row=0,columnspan=2,sticky='news')
    
    left = LabelFrame(root, text='Cake Menu',bg='#C0EDFF')
    left.rowconfigure((0,1,2,3),weight=1)
    left.columnconfigure((0,1),weight=1)
    left.grid(row=1,column=0,sticky='news')
    
    right = LabelFrame(root, text='Checkout',bg='#C1FFC6')
    right.rowconfigure((0,1,2,3),weight=1)
    right.columnconfigure((0,1),weight=1)
    right.grid(row=1,column=1,sticky='news')

    bottom =Frame(root,bg='#FFDEFF')
    bottom.rowconfigure(0,weight=1)
    bottom.columnconfigure(0,weight=1)
    bottom.grid(row=2,columnspan=2,sticky='news')
    return(root,top,left,right,bottom)

def widgettop(top) : 
    title = Label(top,text=("My cake shop"),anchor="center",bg="#F0CBF9",fg="#FDFFBB",font=("Arial",14,"bold"))
    title.grid(row=0,columnspan=2,sticky="news")

def widgetleft(left) :#Left Frame
    cakepic1 = Label(left,image=cake1,bg='#C0EDFF')
    cakepic1.grid(row=0,column=0,stick="w")
    title1 =Label(left,text=("Product :Wow1\nPrice 180 bahts"),bg='#C0EDFF')
    title1.grid(row=0,column=1,stick="n")
    prizelist = Spinbox(left,justify=CENTER, from_=0,to=10,textvariable=amd)
    prizelist.grid(row=0,column=1,padx=20,ipady=5)

    cakepic2 = Label(left,image=cake2,bg='#C0EDFF')
    cakepic2.grid(row=1,column=0,stick="w")
    title2 =Label(left,text=("Product :Wow2\nPrice 250 bahts"),bg='#C0EDFF')
    title2.grid(row=1,column=1,stick="n")
    prizelist2 = Spinbox(left,justify=CENTER, from_=0,to=10,textvariable=amd2)
    prizelist2.grid(row=1,column=1,padx=20,ipady=5)

    cakepic3 = Label(left,image=cake3,bg='#C0EDFF')
    cakepic3.grid(row=2,column=0,stick="w")
    title3 =Label(left,text=("Product :Wow3\nPrice 380 bahts"),bg='#C0EDFF')
    title3.grid(row=2,column=1,stick="n")
    prizelist3 = Spinbox(left,justify=CENTER, from_=0,to=10,textvariable=amd3)
    prizelist3.grid(row=2,column=1,padx=20,ipady=5)

    btnc = Button(left,text="Checkout",compound='left', command=checkout,image=check)
    btnc.grid(row=3,columnspan=2,ipadx=10, sticky='news')
    return prizelist,prizelist2,prizelist3

def widgetright(right) :#Right frame
    lb1 = Label(right, text='"Product :Wow1\nPrice 180 bahts"',bg='#C1FFC6')
    lb1.grid(row=0, column=0, sticky='e')
    total = Label(right,justify=CENTER, bg="white",width=20,height=1)
    total.grid(row=0,column=1,sticky="w",padx=20)

    lb2 = Label(right, text='Product :Wow2\nPrice 250 bahts',bg='#C1FFC6')
    lb2.grid(row=1, column=0, sticky='e')
    total2 = Label(right,justify=CENTER, bg="white",width=20,height=1)
    total2.grid(row=1,column=1,sticky="w",padx=20)

    lb3 = Label(right, text='Product :Wow3\nPrice 380 bahts',bg='#C1FFC6')
    lb3.grid(row=2, column=0, sticky='e')
    total3 = Label(right,justify=CENTER, bg="white",width=20,height=1)
    total3.grid(row=2,column=1,sticky="w",padx=20)

    lb4 = Label(right, text='Total: ',bg='#C1FFC6')
    lb4.grid(row=3, column=0, sticky='e')
    ent_total = Label(right,justify=CENTER, bg="white",width=20,height=1)
    ent_total.grid(row=3,column=1,sticky="w",padx=20)
    return ent_total,total,total2,total3
def widgetbottom(bottom):
    btn1 = Button(bottom,text=" Exit",image=img_exit, compound='left', command=quit)
    btn1.grid(row=0,padx=20,ipadx=15, sticky='e')

def checkout():#Compute Check out
    all = 0
    prize1 = int(prizelist.get()) * 180
    prize2 = int(prizelist2.get()) * 250
    prize3 = int(prizelist3.get()) * 380
    
    p1 = StringVar()
    p1.set("%0.2f" % prize1)

    p2 = StringVar()
    p2.set("%0.2f" % prize2)

    p3 = StringVar()
    p3.set("%0.2f" % prize3)

    total["text"] = p1.get()
    total2["text"] = p2.get()
    total3["text"] = p3.get()

    all = prize1 + prize2 + prize3
    strtotal = StringVar()
    strtotal.set("%0.2f"%all)
    ent_total["text"] = strtotal.get()
    
root = mainwindow()

amd=IntVar()
amd2=IntVar()
amd3=IntVar()

img_exit = PhotoImage(file='CS311_Lab\W4\images\exit.png').subsample(2,2)
cake1 = PhotoImage(file='CS311_Lab\W4\images\cake1.png')#Image
cake2 = PhotoImage(file='CS311_Lab\W4\images\cake2.png')
cake3 = PhotoImage(file='CS311_Lab\W4\images\cake3.png')
check = PhotoImage(file="CS311_Lab\W4\images\cart.png")
size = PhotoImage(file='CS311_Lab\W4\images\cart.png')
frenchfries = PhotoImage(file="CS311_Lab\W4\images\cart.png")

root,top,left,right,bottom = createframe(root)
widgettop(top)
prizelist,prizelist2,prizelist3=widgetleft(left)
widgetbottom(bottom)
ent_total,total,total2,total3=widgetright(right)
root.mainloop()