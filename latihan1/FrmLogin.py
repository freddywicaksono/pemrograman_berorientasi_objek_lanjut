import tkinter as tk
from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W, messagebox
from Users import *
from FrmPersegi import *

class FrmLogin:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # pasang Label
        Label(mainFrame, text='Username:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text="Password:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtUsername = Entry(mainFrame) 
        self.txtUsername.grid(row=0, column=1, padx=5, pady=5)
        
        self.txtPassword = Entry(mainFrame) 
        self.txtPassword.grid(row=1, column=1, padx=5, pady=5)  
        self.txtPassword.config(show='*')
        
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Login',
            command=self.onLogin)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang  
    def onLogin(self, event=None):
        u = self.txtUsername.get()
        p = self.txtPassword.get()
        A = Users()
        B =[]
        B = A.Login(u,p)
        
        if(B[0]=='True'):
            messagebox.showinfo("showinfo", "Login Is Valid\n" + "Login as " + B[1]) 
            self.new_window(0,FrmPersegi)  
            self.parent.withdraw()
        else:
            messagebox.showinfo("showinfo", "Login Not Valid")   
                        
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
    def new_window( self, number, _class):
        new = tk.Toplevel()
        new.transient()
        new.grab_set()
        _class(new, number)
        
if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmLogin(root, "Program Luas Lingkaran")
    root.mainloop() 