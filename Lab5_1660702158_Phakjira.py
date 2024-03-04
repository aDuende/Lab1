from tkinter import*

def createwindow():
    root = Tk()
    root.geometry("600x600")
    root.title("Calculator by Phakjira")
    
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=5)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
    return root
    
def creatframe(root):
    top = Frame(root,bg=("#FFB145"))
    top.rowconfigure(0,weight=1)
    top.columnconfigure(0,weight=1)
    top.grid(row=0,columnspan=4,sticky="news")
    
    left = Frame(root,bg=("#A1A1A1"))
    left.rowconfigure((0,1,2,3,4),weight=1)#divided to 4 row
    left.columnconfigure((0,1),weight=1)#2 column
    left.grid(row=1,column=0,sticky="news")
    
    right = Frame(root,bg="#0D0D0D")
    right.rowconfigure((0,1,2,3,4),weight=1)
    right.columnconfigure((0,1),weight=1)
    right.grid(row=1,column=1,sticky="news")
    
    
    return root,top,left,right

def btn_click(num) :
    total = output.get()
    if num == "=":
        ans = eval(total)
        output.set(ans)
    elif num == "Ac":
        output.set(0)
    elif num == "Clear": 
        output.set(0)  
    else :
          if total == "0" and total != ".":
               output.set(num)
          else :
              output.set(total+num)

def widgettop(top):
    showans = Entry(top,text="0",bg="#FFB145",font=("Times", "36", "bold"), textvariable=output)
    showans.grid()
    
def widgetleft(left):
    btac = Button(left,text="Ac",font=("Times", "24", "bold"),bg="#7ABDFF",command=lambda:btn_click("Ac"))#AC
    btac.grid(row=0,column=0,sticky ='news')
    
    btclear = Button(left,text="Clear",font=("Times", "24", "bold"),bg="#7ABDFF",command=lambda:btn_click("Clear"))#Clear
    btclear.grid(row=0,column=1,sticky ='news')
    
    bt7 = Button(left,text="7",font=("Times", "24", "bold"),command = lambda:btn_click ("7"))#7
    bt7.grid(row=1,column=0,sticky ='news')
    
    bt8 = Button(left,text="8",font=("Times", "24", "bold"),command = lambda:btn_click ("8"))#8
    bt8.grid(row=1,column=1,sticky ='news')
    
    bt4 = Button(left,text="4",font=("Times", "24", "bold"),command = lambda:btn_click ("4"))#4
    bt4.grid(row=2,column=0,sticky ='news')
    
    bt5 = Button(left,text="5",font=("Times", "24", "bold"),command = lambda:btn_click ("5"))#5
    bt5.grid(row=2,column=1,sticky ='news')
    
    bt1 = Button(left,text="1",font=("Times", "24", "bold"),command = lambda:btn_click ("1"))#1
    bt1.grid(row=3,column=0,sticky ='news')
    
    bt2 = Button(left,text="2",font=("Times", "24", "bold"),command = lambda:btn_click ("2"))#2
    bt2.grid(row=3,column=1,sticky ='news')
 
    bt0= Button(left,text="0",font=("Times", "24", "bold"),command = lambda:btn_click ("0"))#0
    bt0.grid(row=4,columnspan=2,sticky ='news')
    
    
def widgetright(right):
    btpercent = Button(right,text="%",font=("Times", "24", "bold"),command = lambda:btn_click ("%"))#%
    btpercent.grid(row=0,column=0,sticky ='news')
    
    btdivide = Button(right,text="/",font=("Times", "24", "bold"),command = lambda:btn_click ("/"))#/
    btdivide.grid(row=0,column=1,sticky ='news')
    
    bt9= Button(right,text="9",font=("Times", "24", "bold"),command = lambda:btn_click ("9"))#9
    bt9.grid(row=1,column=0,sticky ='news')
    
    btx = Button(right,text="x",font=("Times", "24", "bold"),command = lambda:btn_click ("*"))#x
    btx.grid(row=1,column=1,sticky ='news')
    
    bt6= Button(right,text="6",font=("Times", "24", "bold"),command = lambda:btn_click ("6"))#6
    bt6.grid(row=2,column=0,sticky ='news')
    
    btminus = Button(right,text="-",font=("Times", "24", "bold"),command = lambda:btn_click ("-"))#-
    btminus.grid(row=2,column=1,sticky ='news')
    
    bt3= Button(right,text="3",font=("Times", "24", "bold"),command = lambda:btn_click ("3"))#3
    bt3.grid(row=3,column=0,sticky ='news')
    
    btplus = Button(right,text="+",font=("Times", "24", "bold"),command = lambda:btn_click ("+"))#+
    btplus.grid(row=3,column=1,sticky ='news')
    
    btfullstop= Button(right,text=".",font=("Times", "24", "bold"),command = lambda:btn_click ("."))#.
    btfullstop.grid(row=4,column=0,sticky ='news')
    
    btequal= Button(right,text="=",font=("Times", "24", "bold"),command = lambda:btn_click ("="))#=
    btequal.grid(row=4,column=1,sticky ='news')
 

root = createwindow()
total = 0
output = StringVar()
output.set("0")
root,top,left,right = creatframe(root)
widgettop(top)
widgetleft(left)
widgetright(right)
root.mainloop()