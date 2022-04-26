import tkinter as tk
from tkinter import ttk

import sys
import os
from tkinter import *
from tkinter import messagebox,filedialog, scrolledtext
from turtle import bgcolor, color
import numpy as np
from PIL import Image, ImageTk
import cv2



class Application(tk.Frame):
    def _init_(self,master):
        super()._init_(master)
        self.pack()

        self.master.geometry("800x600")
        self.master.title("Pic2Pick")
        

        self.create_widgets()



    def create_widgets(self):


        #Canvas
        self.canvas1 = tk.Canvas(self)
        self.canvas1.configure(width=800, height=480, bg='white')
        self.canvas1.grid(column=1, row=0)
        self.canvas1.grid(padx=0, pady=0)


        #ToolBar
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu = Menu(menubar)
        menubar.configure( font=("Mistral",15), fg='black')
        menubar.add_command(label="Upload", command=self.loadImage)
        menubar.add_command(label="Clear", command=self.clearImage)
        menubar.add_command(label="Help", command=self.help)
        menubar.add_command(label="Quit", command=self.quit_app)

        #LogMessage

        



    # Event Call Back
    def help(self):
        helpPop = Toplevel(self.master)
        helpPop.geometry("350x500")
        helpPop.title("Help")
        Label(helpPop, text="help", font=('Mistral 18 bold')).place(x=150,y=80)
    def loadImage(self):

        #self.folder_name = filedialog.askdirectory()
        self.filename = filedialog.askopenfilename()
        #print(self.folder_name)
        print(self.filename)

        self.image_bgr = cv2.imread(self.filename)
        self.height, self.width = self.image_bgr.shape[:2]
        print(self.height, self.width)
        if self.width > self.height:
            self.new_size = (640,480)
        else:
            self.new_size = (480,480)

        self.image_bgr_resize = cv2.resize(self.image_bgr, self.new_size, interpolation=cv2.INTER_AREA)
        self.image_rgb = cv2.cvtColor( self.image_bgr_resize, cv2.COLOR_BGR2RGB )  #Since imread is BGR, it is converted to RGB

       # self.image_rgb = cv2.cvtColor(self.image_bgr, cv2.COLOR_BGR2RGB) #Since imread is BGR, it is converted to RGB
        self.image_PIL = Image.fromarray(self.image_rgb) #Convert from RGB to PIL format
        self.image_tk = ImageTk.PhotoImage(self.image_PIL) #Convert to ImageTk format
        self.canvas1.create_image(320,240, image=self.image_tk)


    def clearImage(self):
        self.canvas1.delete("all")
    
    def quit_app(self):
        self.Msgbox = tk.messagebox.askquestion("Exit Applictaion", "Are you sure?", icon="warning")
        if self.Msgbox == "yes":
            self.master.destroy()
        else:
            tk.messagebox.showinfo("Return", "you will now return to application screen")



def main():
    root = tk.Tk()
    app = Application(master=root)#Inherit
    app.mainloop()

if _name_ == "_main_":
    main()