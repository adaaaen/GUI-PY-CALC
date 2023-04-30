# Call tkinter LIBRARY
from tkinter import*

# SET-UP a WINDOW
root = Tk()

root.config(bg="gray", cursor="hand2")

root.title("CALCULATOR")

root.resizable(0,0)

# declare a null variable name OPERATOR
operator = ""

# ADDING ACTION IN BUTTON
  
   # FOR NUMBER & OPERATION BUTTONS

def press(num):
    global operator
    operator = operator + str(num)
    input_text.set(operator)

   # FOR EQUAL BUTTON

def equalpress():
    global operator
    total = str(eval(operator))
    input_text.set(total)
    operator = ""

   # FOR CLEAR BUTTON

def clear():
    global operator
    operator = ""
    input_text.set("")

# declare a StringVar function in input_text
input_text = StringVar()

# Make a ENTRY to display INPUT
display_text = Entry(root, font=("arial", 30, "bold"), textvariable=input_text, insertwidth=4, bd=30, bg="black",fg="white", justify=RIGHT).grid(columnspan=4)

# make  BUTTONS FOR 1st row

 # 7 BUTTON

btn_7 = Button(root, padx=16, font=("arial", 25, "bold"), bd=16, text="7", fg="black", bg="white",activebackground="#e0b1c5",activeforeground="black",command=lambda: press(7))

 # 8 BUTTON

btn_8 = Button(root, padx=16, font=("arial", 25, "bold"), bd=16, text="8", fg="black", bg="white",activebackground="#e0b1c5",activeforeground="black",command=lambda: press(8))

 # 9 BUTTON

btn_9 = Button(root, padx=16, font=("arial", 25, "bold"), bd=16, text="9", fg="black", bg="white",activebackground="#e0b1c5",activeforeground="black",command=lambda: press(9))

 # ÷ BUTTON

btn_DIV = Button(root, padx=16, font=("arial", 25, "bold"), bd=16, text="÷", fg="white", bg="#474b52",activebackground="#e0b1c5",activeforeground="black",command=lambda: press("/"))

    # GRID ALIGNMENT FOR 7 8 9 ÷ BUTTONS

btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_DIV.grid(row=2, column=3)

# 4 BUTTON

btn_4 = Button(root, padx=16, font=("arial", 25, "bold"), bd=16, text="4", fg="black", bg="white",activebackground="#e0b1c5",activeforeground="black",command=lambda: press(4))

 # 5 BUTTON

btn_5 = Button(root, padx=16, font=("arial", 25, "bold"), bd=16, text="5", fg="black", bg="white",activebackground="#e0b1c5",activeforeground="black",command=lambda: press(5))

 # 6 BUTTON

btn_6 = Button(root, padx=16, font=("arial", 25, "bold"), bd=16, text="6", fg="black", bg="white",activebackground="#e0b1c5",activeforeground="black",command=lambda: press(6))

 # + BUTTON

btn_PLS = Button(root, padx=16, font=("arial", 25, "bold"), bd=16, text="+", fg="white", bg="#474b52",activebackground="#e0b1c5",activeforeground="black",command=lambda: press("+"))

    # GRID ALIGNMENT FOR 4 5 6 + BUTTONS

btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)
btn_PLS.grid(row=3, column=3)

# 1 BUTTON

btn_1 = Button(root, padx=16, font=("arial", 25, "bold"), bd=16, text="1", fg="black", bg="white",activebackground="#e0b1c5",activeforeground="black",command=lambda: press(1))

 # 2 BUTTON

btn_2 = Button(root, padx=16, font=("arial", 25, "bold"), bd=16, text="2", fg="black", bg="white",activebackground="#e0b1c5",activeforeground="black",command=lambda: press(2))

 # 9 BUTTON

btn_3 = Button(root, padx=16, font=("arial", 25, "bold"), bd=16, text="3", fg="black", bg="white",activebackground="#e0b1c5",activeforeground="black",command=lambda: press(3))

 # ÷ BUTTON

btn_MNS = Button(root, padx=16, font=("arial", 25, "bold"), bd=16, text="- ", fg="white", bg="#474b52",activebackground="#e0b1c5",activeforeground="black",command=lambda: press("-"))

    # GRID ALIGNMENT FOR 1 2 3 - BUTTONS

btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)
btn_MNS.grid(row=4, column=3)

# 0 BUTTON

btn_0 = Button(root, padx=16, font=("arial", 25, "bold"), bd=16, text="0", fg="white", bg="#474b52",activebackground="#e0b1c5",activeforeground="black",command=lambda: press(0))

 # CLEAR BUTTON

btn_CLR = Button(root, padx=16, font=("arial", 25, "bold"), bd=16, text="C", fg="black", bg="orange",activebackground="#e0b1c5",activeforeground="black",command=clear)

 # = BUTTON

btn_EQL = Button(root, padx=16, font=("arial", 25, "bold"), bd=16, text="=", fg="white", bg="#474b52",activebackground="#e0b1c5",activeforeground="black",command=equalpress)

 # x BUTTON

btn_MUL = Button(root, padx=16, font=("arial", 25, "bold"), bd=16, text="x", fg="white", bg="#474b52",activebackground="#e0b1c5",activeforeground="black",command=lambda: press("*"))

    # GRID ALIGNMENT FOR 0 C = x BUTTONS

btn_0.grid(row=5, column=0)
btn_CLR.grid(row=5, column=1)
btn_EQL.grid(row=5, column=2)
btn_MUL.grid(row=5, column=3)

# for run the window when user quit
root.mainloop()
