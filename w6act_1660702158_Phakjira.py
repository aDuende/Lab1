from tkinter import *

def mainwindow() :
  root = Tk()
  
  x = root.winfo_screenwidth()/2 - (w/2)
  y = root.winfo_screenheight()/2 - (h/2)
  root.geometry("%dx%d+%d+%d"%(w,h,x,y))
  root.title("W6-Act created by Phakjira")
  root.option_add('*font','Garamond 16 bold')
  menubar = Menu(root)
  # Windows OS
  menubar.add_command(label="Test Score",command=menuscore)
  menubar.add_command(label="Grading",command=grading)
  menubar.add_command(label="Exit",command=root.quit)
  # macOS
  """
  filemenu = Menu(menubar, tearoff=0)
  filemenu.add_command(label="Test Score")
  filemenu.add_command(label="Grading")
  filemenu.add_command(label="Exit")
  menubar.add_cascade(label="File", menu=filemenu)
  """
  
  root.config(bg="pink",menu=menubar)
  root.resizable(False, False)
  return root

def menuscore():
  frm1 = Frame(root,bg="lightgreen")
  frm1.place(x=0,y=0,width=w,height=h)
  frm1.columnconfigure((0,1),weight=1)

  Label(frm1,text="Midterm :").grid(row=0,column=0,pady=20,sticky="e")
  Entry(frm1,width=15,textvariable=midVar,justify="right").grid(row=0,column=1,pady=15)

  Label(frm1,text="Final :").grid(row=1,column=0,pady=20,sticky="e")
  Entry(frm1,width=15,textvariable=finalVar,justify="right").grid(row=1,column=1,pady=15)

  Label(frm1,text="Quiz :").grid(row=2,column=0,pady=20,sticky="e")
  Entry(frm1,width=15,textvariable=quizVar,justify="right").grid(row=2,column=1,pady=15)

  Label(frm1,text="Project :").grid(row=3,column=0,pady=20,sticky="e")
  Entry(frm1,width=15,textvariable=projVar,justify="right").grid(row=3,column=1,pady=15)

  Button(frm1,text="Grade calc",command=grading).grid(row=4,columnspan=2)



def grading() :
  frame2 = Frame(root,bg='lightblue')
  frame2.place(x=0,y=0,width=500,height=500)
  frame2.columnconfigure((0,1),weight=1)
  sum = 0

  # sum score
  midscore = midVar.get()  
  finalscore = finalVar.get()
  quizscore = quizVar.get()
  projscore = projVar.get()
  sum = midscore + finalscore + quizscore + projscore

  Label(frame2,text="Midterm :").grid(row=0,column=0,pady=20,sticky="e")
  Label(frame2,text=midscore).grid(row=0,column=1,pady=15,sticky="w")

  Label(frame2,text="Final :").grid(row=1,column=0,pady=20,sticky="e")
  Label(frame2,text=finalscore).grid(row=1,column=1,pady=15,sticky="w")

  Label(frame2,text="Quiz :").grid(row=2,column=0,pady=20,sticky="e")
  Label(frame2,text=quizscore).grid(row=2,column=1,pady=15,sticky="w")

  Label(frame2,text="Project :").grid(row=3,column=0,pady=20,sticky="e")
  Label(frame2,text=projscore).grid(row=3,column=1,pady=15,sticky="w")

  # display widget
  showgrade = StringVar()
  gradeLB = Label(frame2, textvariable=showgrade,bg='lightblue')
  gradeLB.grid(row=4,columnspan=2,sticky="news")
  grade = ""
  if sum > -1 and sum < 101 : #checking normal score, if over score then notify an error
    if sum > 79 :
      grade = "A (Excellent)"
      gradeLB['fg'] = 'blue'
      gradeLB['bg'] = 'yellow'
    elif sum > 69 :
      grade = "B"
      gradeLB['fg'] = 'blue'
      gradeLB['bg'] = 'lightgreen'
    elif sum > 59 :
      grade = "C"
      gradeLB['fg'] = 'blue'
      gradeLB['bg'] = 'orange'
    elif sum > 49 :
      grade = "D"
      gradeLB['fg'] = 'orange'
      gradeLB['bg'] = 'blue'
    else :
      grade = "F (Try again)"
      gradeLB['fg'] = 'white'
      gradeLB['bg'] = 'red'

    #show grade infomation on widget Lable
    showgrade.set("**** The total score = %d ,Grade = %s ****"%(sum,grade))  
  else :
    grade = "Total score is out of range (0-100) !!! "
    gradeLB['fg'] = 'red'
    gradeLB['bg'] = 'black'
    #show grade infomation on widget Lable
    showgrade.set(grade)

w = 500
h = 500
root = mainwindow() 
testlist = ['Midterm','Final','Quiz','Project'] #for enumerate
spy = [DoubleVar() for i in testlist]#for enumerate
midVar = DoubleVar()
finalVar = DoubleVar()
quizVar = DoubleVar()
projVar =DoubleVar()
root.mainloop()