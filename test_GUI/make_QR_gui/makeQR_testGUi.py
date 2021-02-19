import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import sys
import os
import time
import qrcode


def store():
    img=Image.open(r"C:\Users\HN4-00012\Pictures\qrcode_test.png")
    width, height = img.size
    img.show()

def maker():

    def create_qr():
        #global name
        #global number
        name = entry1.get()
        number = entry2.get()

        inqr = str(name) + number
        print(inqr)

        print(name)
        print(number)
        
        img = qrcode.make(inqr)

        print(type(img))
        print(img.size)

        img.show()
        img.save(r'C:\Users\HN4-00012\Pictures\qrcode_testqr.png')

    global name
    global number
    root = tk.Tk()
    root.title("store")
    root.geometry("500x500")


    frame1 = tk.Frame(root,pady=10)
    frame1.pack()
    label2 = tk.Label(frame1,font=("",14),text="名前")
    label2.pack(side="left")
    entry1 = tk.Entry(frame1,font=("",14),justify="center",width=15)
    entry1.pack(side="left")
    #name = entry1.get()
   # print(str(name))

    frame2 = tk.Frame(root,pady=10)
    frame2.pack()
    label3 = tk.Label(frame2,font=("",14),text="生年月日")
    label3.pack(side="left")
    entry2 = tk.Entry(frame2,font=("",14),justify="center",width=15)
    entry2.pack(side="left")
    #number = entry2.get()
    #print(number)

    

    
    
    button4 = tk.Button(root,text="登録",font=("",16),width=10,bg="gray",command=create_qr)
    button4.pack()

    

   







    


    

    

    








root = tk.Tk()
root.title("QR")
root.geometry("500x500")

button1 = tk.Button(root,text="【このお店のQR】",height=2,width=20,command=store)
button1.pack(side="right")


button2 = tk.Button(root,text="【あなた専用のQR】",height=2,width=20,command=maker)
button2.pack(side="left")

root.mainloop()


