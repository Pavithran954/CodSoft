from tkinter import *
import random, string

root=Tk()
root.geometry("400x280")
root.title("Password Generator")

#icon
Image_icon=PhotoImage(file="password generator.png")
root.iconphoto(False,Image_icon)

#intro
title = StringVar()
label= Label(root,textvariable=title).pack()
title.set("The Strength of Password:")

def selection():
    selection=choice.get()

choice=IntVar()
R1=Radiobutton(root,text="POOR",variable=choice,value=1, command=selection).pack(anchor=CENTER)
R2=Radiobutton(root,text="AVERAGE",variable=choice,value=2, command=selection).pack(anchor=CENTER)
R3=Radiobutton(root,text="STRONG",variable=choice,value=3, command=selection).pack(anchor=CENTER)

labelchoice=Label(root)
labelchoice.pack()

lenlabel=Label(root)
labelchoice.pack()

lenlabel=StringVar()
lenlabel.set("Password Length")
lentitle=Label(root,textvariable=lenlabel).pack()

val=IntVar()
spinlength = Spinbox(root,from_=8, to_=24, textvariable=val, width=13).pack()

def callback():
    lsum.config(text=passgen())

passgenButton=Button(root,text="Generate Password", bd=5, height=2, command= callback,pady=3)
passgenButton.pack()
password=str(callback)

lsum=Label(root,text="")
lsum.pack(side=BOTTOM)

#logic
poor=string.ascii_uppercase+string.ascii_lowercase
average=string.ascii_uppercase+string.ascii_lowercase+string.digits
symbols="""~`!@#$%^&*()_+=[{]}:;',.><?|"""
advance=poor+average+symbols

def passgen():
    if choice.get()==1:
        return "".join(random.sample(poor,val.get()))
    elif choice.get()==2:
        return "".join(random.sample(average,val.get()))
    elif choice.get()==3:
        return "".join(random.sample(advance,val.get()))
    
root.mainloop()











































# import random

# lower = "abcdefghijklmnopqrstuvwxyz"
# upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numbers = "0123456789"
# symbols = "!@#$%^&*()_.?,<>;:{[]}-+="

# string = lower+upper+numbers+symbols
# length = int(input("Enter your Password Length: "))
# password = "".join(random.sample(string,length))

# print("Your new Password is: "+password)
