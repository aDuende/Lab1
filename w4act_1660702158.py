from tkinter import *
from tkinter import ttk
def mainwindow() :
    root = Tk()
    root.title("GUI3: Class Activity of Week4")
    root.geometry("600x500")
    root.configure(bg='lightgreen')
    root.option_add('*font', 'Calibri 14')
    img_icon = PhotoImage(file="image\logo.png")
    root.iconphoto(False,img_icon)
    
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=4)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=4)
    return(root)

def createframe(root) :
    top = Frame(root,bg='#694E4E')
    top.rowconfigure(0,weight=1)
    top.columnconfigure(0,weight=1)
    top.grid(row=0,columnspan=2,sticky='news')
    
    left = Frame(root,bg='#F3C5C5')
    left.rowconfigure((0,1,2,3),weight=1)
    left.columnconfigure(0,weight=1)
    left.grid(row=1,column=0,sticky='news')
    
    right = LabelFrame(root, text='Orders')
    right.rowconfigure((0,1,2,3),weight=1)
    right.columnconfigure((0,1),weight=1)
    right.grid(row=1,column=1,sticky='news')
    return(root,top,left,right)

def widgettop(top) : 
    btn1 = Button(top,text=" Exit",image=img_exit, compound='left', command=quit)
    btn1.grid(row=0,padx=20,ipadx=15, sticky='e')

def widgetleft(left) :
    tag1 = Label(left,image=pizza, bg='#F3C5C5')
    tag1.grid(row=0)
    tag2 = Label(left,image=size, bg='#F3C5C5')
    tag2.grid(row=1)
    tag3 = Label(left,image=frenchfries, bg='#F3C5C5')
    tag3.grid(row=2)
    btnc = Button(left,text="Checkout",compound='left', command=checkout)
    btnc.grid(row=3,ipadx=15, sticky='news')

def widgetright(right) :
    lb1 = Label(right, text='Select size: \nS:160,M:240,L:320')
    lb1.grid(row=0, column=0, sticky='e')
    sizelist = ["Small","Medium","Large"]
    spinsize = Spinbox(right,justify=CENTER,values=sizelist)
    spinsize.grid(row=0,column=1,sticky="w",padx=20,ipady=15)

    lb2 = Label(right, text='QTY: ')
    lb2.grid(row=1, column=0, sticky='e')
    spinquan = Spinbox(right,justify=CENTER, from_=0,to=10,textvariable=qty)
    spinquan.grid(row=1,column=1,sticky="w",padx=20,ipady=15)

    ff_check = Checkbutton(right,text="FF 50 baht",variable=ffVal)
    ff_check.grid(row=2,column=1,sticky="w",padx=20,ipady=15)

    lb3 = Label(right, text='Total: ')
    lb3.grid(row=3, column=0, sticky='e')
    ent_total = Label(right,justify=CENTER, bg="white",width=20,height=1)
    ent_total.grid(row=3,column=1,sticky="w",padx=20)
    return ff_check,spinsize,spinquan,ent_total

def checkout():
    total,ff_price = 0,0
    print(ffVal.get())
    if spinsize.get() == 'Small':
        pizzaprize = 160
    elif spinsize.get() == 'Medium':
        pizzaprize = 240
    elif spinsize.get() == 'Large':
        pizzaprize = 320
    
    quantity = int(spinquan.get())
    if ffVal.get() == 1:
        ff_price = 50
    else:
        ff_price = 0

    total = (pizzaprize*quantity)+ff_price
    strtotal = StringVar()
    strtotal.set("%0.2f"%total)
    ent_total["text"] = strtotal.get()
    ent_total["bg"] = "blue"
    ent_total["fg"] = "white"

root = mainwindow()

ffVal = IntVar()
qty=StringVar()

img_exit = PhotoImage(file='image/exit.png').subsample(2,2)
pizza = PhotoImage(file='image/pizza.png')
size = PhotoImage(file='image/pizza-size.png')
frenchfries = PhotoImage(file="image/frenchfries.png")

root,top,left,right = createframe(root)
widgettop(top)
widgetleft(left)
ff_check,spinsize,spinquan,ent_total=widgetright(right)
root.mainloop()