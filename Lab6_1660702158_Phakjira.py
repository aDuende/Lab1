from tkinter import*

def createwindow():
     root = Tk()
     x = root.winfo_screenwidth()/2 - (w/2)
     y = root.winfo_screenheight()/2 - (h/2)
     root.geometry("%dx%d+%d+%d"%(w,h,x,y))

     root.title("W6-Act created by Phakjira")
     root.option_add('font','Garamond 16 bold')

     menubar = Menu(root)
     menubar.add_command(label="Menu",command=menupage)
     menubar.add_command(label="Checkout",command=checkoutpage)
     menubar.add_command(label="Exit",command=root.quit)

     
     root.config(bg="pink",menu=menubar)
     root.resizable(FALSE,FALSE) #ห้ามไม่ให้เปลี่ยนขนาด

     return root
 
def firstpage():
     imheartf = Label(root,image=imaheart,bg="pink")
     imheartf.place(x=50,y=0,width=500,height=500)

     title = Label(root,text="...Welcome to my Restaurant...",bg="pink",font='Garamond  20 bold')
     title.place(x=130,y=500)

def menupage():
     frm1 = Frame(root,bg="yellow")
     frm1.place(x=0,y=0,width=w,height=h)
     frm1.columnconfigure((0,1),weight=1)

     Label(frm1,text="Strawberry Cake:",bg="yellow",font='Garamond  16 bold').grid(row=0,column=0)
     Label(frm1,image=imacake1,bg="yellow").grid(row=1,column=0)
     Label(frm1,text="Price 85",bg="yellow",font='Garamond  16 bold').grid(row=2,column=0)
     prizebox = Spinbox(frm1,justify=CENTER, from_=0,to=10,textvariable=amd,font='Garamond 14 bold').grid(row=3,column=0,ipady=5)

     Label(frm1,text="Cheese Cake:",bg="yellow",font='Garamond  16 bold').grid(row=4,column=0,pady=10)
     Label(frm1,image=imacake2 ,bg="yellow").grid(row=5,column=0)
     Label(frm1,text="Price 95",bg="yellow",font='Garamond  16 bold').grid(row=6,column=0)
     prizebox2 = Spinbox(frm1,justify=CENTER, from_=0,to=10,textvariable=amd1,font='Garamond 14 bold').grid(row=7,column=0,ipady=5)

     Label(frm1,text="Strawberry Mixed:",bg="yellow",font='Garamond  16 bold').grid(row=0,column=1)
     Label(frm1,image=imamixed1,bg="yellow").grid(row=1,column=1)
     Label(frm1,text="Price 120",bg="yellow",font='Garamond  16 bold').grid(row=2,column=1)
     prizebox3 = Spinbox(frm1,justify=CENTER, from_=0,to=10,textvariable=amd2,font='Garamond 14 bold').grid(row=3,column=1,ipady=5)

     Label(frm1,text="Orange Mixed:",bg="yellow",font='Garamond  16 bold').grid(row=4,column=1,pady=10)
     Label(frm1,image=imamixed2 ,bg="yellow").grid(row=5,column=1)
     Label(frm1,text="Price 140",bg="yellow",font='Garamond  16 bold').grid(row=6,column=1)
     prizebox4 = Spinbox(frm1,justify=CENTER, from_=0,to=10,textvariable=amd3,font='Garamond 14 bold').grid(row=7,column=1,ipady=5)
     
     return prizebox,prizebox2,prizebox3,prizebox4

def checkoutpage():
     frm2 = Frame(root,bg='lightgreen')
     frm2.place(x=0,y=0,width=w,height=h)
     frm2.columnconfigure((0,1,2,3),weight=1)


     straw = int(amd.get())*85  
     cheese = int(amd1.get())*95 
     strawmix = int(amd2.get())*120 
     oranmix = int(amd3.get())*140
     sum = straw+cheese+strawmix+oranmix

     Label(frm2,text="Menu list",font='Garamond  16 bold',bg='lightgreen').grid(row=0,column=0)
     Label(frm2,text="Amount",font='Garamond  16 bold',bg='lightgreen').grid(row=0,column=1)
     Label(frm2,text="Prices",font='Garamond  16 bold',bg='lightgreen').grid(row=0,column=2)
     Label(frm2,text="Total Bahts",font='Garamond  16 bold',bg='lightgreen').grid(row=0,column=3)

     Label(frm2,text="Strawberry Cake:",font='Garamond  16 bold',bg='lightgreen',fg='blue').grid(row=1,column=0)
     Label(frm2,textvariable=amd,bg="lightgreen",font='Garamond 14 bold').grid(row=1,column=1)
     Label(frm2,text="85",font='Garamond  16 bold',bg='lightgreen').grid(row=1,column=2)
     Label(frm2,text=straw,font='Garamond  16 bold',bg='lightgreen').grid(row=1,column=3)

     Label(frm2,text="Cheese Cake:",font='Garamond  16 bold',bg='lightgreen',fg='blue').grid(row=2,column=0)
     Label(frm2,textvariable=amd1,bg="lightgreen",font='Garamond 14 bold').grid(row=2,column=1)
     Label(frm2,text="95",font='Garamond  16 bold',bg='lightgreen').grid(row=2,column=2)
     Label(frm2,text=cheese,font='Garamond  16 bold',bg='lightgreen').grid(row=2,column=3)

     Label(frm2,text="Strawberry Mixed:",font='Garamond  16 bold',bg='lightgreen',fg='blue').grid(row=3,column=0)
     Label(frm2,textvariable=amd2,bg="lightgreen",font='Garamond 14 bold').grid(row=3,column=1)
     Label(frm2,text="120",font='Garamond  16 bold',bg='lightgreen').grid(row=3,column=2)
     Label(frm2,text=strawmix,font='Garamond  16 bold',bg='lightgreen').grid(row=3,column=3)

     Label(frm2,text="Orange Mixed:",font='Garamond  16 bold',bg='lightgreen',fg='blue').grid(row=4,column=0)
     Label(frm2,textvariable=amd3,bg="lightgreen",font='Garamond 14 bold').grid(row=4,column=1)
     Label(frm2,text="140",font='Garamond  16 bold',bg='lightgreen').grid(row=4,column=2)
     Label(frm2,text=oranmix,font='Garamond  16 bold',bg='lightgreen').grid(row=4,column=3)


     showtotal = StringVar()
     totalLB = Label(frm2, textvariable=showtotal,bg='lightgreen',font='Garamond  16 bold',fg='red')
     totalLB.grid(row=5,columnspan=4,sticky="news",pady=10)
     showtotal.set("Total Price = %.2f Bahts"%sum)
w = 600
h = 600

root = createwindow()

amd=IntVar()
amd1=IntVar()
amd2=IntVar()
amd3=IntVar()

imaheart = PhotoImage(file="CS311_Lab\W6\images\myshop.png")
imacake1 = PhotoImage(file="CS311_Lab\W6\images\cake1.png")
imacake2 = PhotoImage(file="CS311_Lab\W6\images\cake2.png")
imamixed1 = PhotoImage(file="CS311_Lab\W6\images\drink1.png")
imamixed2 = PhotoImage(file="CS311_Lab\W6\images\drink2.png")
firstpage()


root.mainloop()

