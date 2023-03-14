import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox, Menu
from Mahasiswa import *
from FrmPersegi import *
from FrmSegitiga import *
from FrmLingkaran import *
from FrmMahasiswa import *

class FrmDashboard:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("600x600")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        
    def new_window( self, number, _class):
        new = tk.Toplevel()
        new.transient()
        new.grab_set()
        _class(new, number)
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
       
        # create a menu
        file_menu = Menu(menubar)
        app_menu = Menu(menubar)
        data_menu = Menu(menubar)

        # Menu File
        file_menu.add_command(
            label='File Open', command=root.destroy
        )

        file_menu.add_command(
            label='Exit', command=root.destroy
        )

        # Menu App
        app_menu.add_command(
            label='App Persegi', command= lambda: self.new_window("Luas Persegi", FrmPersegi)
        )
        app_menu.add_command(
            label='App Segitiga', command= lambda: self.new_window("Luas Segitiga", FrmSegitiga)
        )
        app_menu.add_command(
            label='App Lingkaran', command= lambda: self.new_window("Luas Lingkaran", FrmLingkaran)
        )

        # Menu Data
        data_menu.add_command(
            label='Data Mahasiswa', command= lambda: self.new_window("Data Mahasiswa", FrmMahasiswa)
        )
        
        # add the File menu to the menubar
        menubar.add_cascade(
            label="File", menu=file_menu
        )
        menubar.add_cascade(
            label="App", menu=app_menu
        )
        menubar.add_cascade(
            label="Data", menu=data_menu
        )
     
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
    

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FrmDashboard(root, "Aplikasi Data Mahasiswa")
    root.mainloop() 