#--------------------------------
#Author : Phakjira Ratchatanich
#ID : 1-66-07-0215-8
#SECTION : 127D
#--------------------------------

def displaymenu():
    #show menu
    print("==========================================")
    print("|     *** Area Calculator Program***     |")
    print("------------------------------------------")
    print("|     Shape code list :                  |")
    print("|          (R) Rectangle                 |")
    print("|          (T) Trapezoid                 |")
    print("|          (C) Circle                    |")
    print("------------------------------------------")
    menu = input("Select Code [R,T,C]: ")
    if menu.upper() == "R":#.upper() หากสิ่งที่ใส่มาเป็นตัวพิมพ์เล็กจะถูกconvertให้เป็นพิมพ์ใหญ่เพื่อให้ง่ายต่อการตรวจสอบ
        print("You select R = Rectangle")
    elif menu.upper() == "T":
        print("You select T = Trapezoid")
    elif menu.upper() == "C":
        print("You select T = Circle")
    return menu

def rectangle():
    #input and calculate area of rectangle
    print("== == == == == == == == == == == == == == == == == == == =")
    print("Area of Rectangle")
    print("== == == == == == == == == == == == == == == == == == == =")
    wid = float(input("Enter width: "))
    hei = float(input("Enter height: "))
    print("== == == == == == == == == == == == == == == == == == == =")
    area = wid*hei
    print("Area = %.2f"%area)
    print("== == == == == == == == == == == == == == == == == == == =")

def trapezoid():
    #input and calculate area of trapezoid
    print("== == == == == == == == == == == == == == == == == == == =")
    print("Area of Trapezoid")
    print("== == == == == == == == == == == == == == == == == == == =")
    fbase = float(input("Enter base1: "))
    sbase = float(input("Enter base2: "))
    hei = float(input("Enter height: "))
    print("== == == == == == == == == == == == == == == == == == == =")
    area = 1/2*(fbase+sbase)*hei
    print("Area = %.2f" % area)
    print("== == == == == == == == == == == == == == == == == == == =")

def circle():
    #input and calculate area of circle
    print("== == == == == == == == == == == == == == == == == == == =")
    print("Area of Trapezoid")
    print("== == == == == == == == == == == == == == == == == == == =")
    radius = float(input("Enter radius: "))
    print("== == == == == == == == == == == == == == == == == == == =")
    area = 22/7*(radius**2)
    print("Area = %.2f" % area)
    print("== == == == == == == == == == == == == == == == == == == =")

menu = displaymenu()

if menu.upper() == "R":
    rectangle()
elif menu.upper() == "T":
    trapezoid()
elif menu.upper() == "C":
    circle()
else:
    print("You select %s = Invalid shape code!"%menu.upper())
    print("Please try again.")