# from tkinter import *

# root = Tk()
# # root.geometry("420x300")

# # lable_name=Label(root,text="name")
# # lable_name.pack()
# # name=Entry(root)
# # name.pack()
# # lable_age=Label(root,text="age")
# # lable_age.pack()
# # age=Entry(root)
# # age.pack()
# # lable_address=Label(root,text="address")
# # lable_address.pack()
# # address=Entry(root)
# # address.pack()
# # def submit():
# #     print(name.get())
# #     print(age.get())
# #     print(address.get())
        
# # button=Button(root,text="submit",command=submit)
# # button.pack()

# name_label = Label(root, text="Name")
# name_label.grid(column=0, row=0,padx=10, pady=10)

# name_entry = Entry(root)
# name_entry.grid(column=1, row=0, padx=10)

# def submit(sign):
#     print(sign)

# button = Button(root, text="SUBMIT", command=lambda : submit("+"))
# button.grid(row=1, column=0)
# root.mainloop()
# xp = "2+3//(2*4)"
# res = eval(xp)
# print(res)

from tkinter import *
window=Tk()
window.title("my window")
expression=""
def handleClick(button):
    global expression
    if len(expression)==0:
        if button.isdigit():
            if button!="0":

                expression=expression+button
                data.set(expression)
    else:
        
        
        expression=expression+button
        data.set(expression)
    
def handleEqual():
    global expression
    
    if expression[-1].isdigit():
        res=eval(expression)

        print(res)
    
        data.set(res)
        expression=""
#string=[start:end:stepsize]
def handleBackspace():
    global expression
    expression=expression[:-1]
    data.set(expression)
    print(expression)
data=StringVar()



input_box=Entry(window,font=28,textvariable=data)
input_box.grid(row=0,column=0,columnspan=4,pady=10)

button_one=Button(window, text="0",font=24,padx=10,pady=10,command=lambda:handleClick("0"))
button_one.grid(row=4,column=1,padx=10,pady=10)

button_one=Button(window,text="=",font=24,padx=10,pady=10,command=handleEqual)
button_one.grid(row=4,column=2,padx=10,pady=10)

button_one=Button(window,text="/",font=24,padx=10,pady=10,command=lambda:handleClick("/"))
button_one.grid(row=4,column=3,padx=10,pady=10)

button_one=Button(window,text="<=",font=24,padx=10,pady=10,command=lambda:handleClick("<="))
button_one.grid(row=4,column=0,padx=10,pady=10)

button_one=Button(window,text="1",font=24,padx=10,pady=10,command=lambda:handleClick("1"))
button_one.grid(row=3,column=0,padx=10,pady=10)

button_one=Button(window,text="2",font=24,padx=10,pady=10,command=lambda:handleClick("2"))
button_one.grid(row=3,column=1,padx=10,pady=10)


button_one=Button(window,text="3",font=24,padx=10,pady=10,command=lambda:handleClick("3"))
button_one.grid(row=3,column=2,padx=10,pady=10)

button_one=Button(window,text="4",font=24,padx=10,pady=10,command=lambda:handleClick("4"))
button_one.grid(row=2,column=0,padx=10,pady=10)

button_one=Button(window,text="5",font=24,padx=10,pady=10,command=lambda:handleClick("5"))
button_one.grid(row=2,column=1,padx=10,pady=10)
button_one=Button(window,text="6",font=24,padx=10,pady=10,command=lambda:handleClick("6"))
button_one.grid(row=2,column=2,padx=10,pady=10)

button_one=Button(window,text="7",font=24,padx=10,pady=10,command=lambda:handleClick("7"))
button_one.grid(row=1,column=0,padx=10,pady=10)

button_one=Button(window,text="8",font=24,padx=10,pady=10,command=lambda:handleClick("8"))
button_one.grid(row=1,column=1,padx=10,pady=10)

button_one=Button(window,text="9",font=24,padx=10,pady=10,command=lambda:handleClick("9"))
button_one.grid(row=1,column=2,padx=10,pady=10)

button_one=Button(window,text="cl",font=24,padx=10,pady=10,command=handleBackspace)
button_one.grid(row=4,column=0,padx=10,pady=10)

button_one=Button(window,text="+",font=24,padx=10,pady=10,command=lambda:handleClick("+"))
button_one.grid(row=3,column=3,padx=10,pady=10)

button_one=Button(window,text="-",font=24,padx=10,pady=10,command=lambda:handleClick("-"))
button_one.grid(row=2,column=3,padx=10,pady=10)

button_one=Button(window,text="*",font=24,padx=10,pady=10,command=lambda:handleClick("*"))
button_one.grid(row=1,column=3,padx=10,pady=10)
                
window.mainloop()
