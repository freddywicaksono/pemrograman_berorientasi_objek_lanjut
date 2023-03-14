import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox

from Dosen import *
class FrmDosen:

   def __init__(self, parent, title):
       self.parent = parent
       self.parent.geometry("600x600")
       self.parent.title(title)
       self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
       self.ditemukan = None
       self.aturKomponen()
       self.onReload()

   def aturKomponen(self):
       mainFrame = Frame(self.parent, bd=10)
       mainFrame.pack(fill=BOTH, expand=YES)

       # Label
       Label(mainFrame, text='Nidn:').grid(row=0, column=0,
           sticky=W, padx=5, pady=5)
       Label(mainFrame, text='Nama_Lengkap:').grid(row=1, column=0,
           sticky=W, padx=5, pady=5)
       Label(mainFrame, text='Jk:').grid(row=2, column=0,
           sticky=W, padx=5, pady=5)
       Label(mainFrame, text='Telpon:').grid(row=3, column=0,
           sticky=W, padx=5, pady=5)
       Label(mainFrame, text='Email:').grid(row=4, column=0,
           sticky=W, padx=5, pady=5)
       Label(mainFrame, text='Prodi:').grid(row=5, column=0,
           sticky=W, padx=5, pady=5)


       # Textbox
       self.txtNIDN = Entry(mainFrame)
       self.txtNIDN.grid(row=0, column=1, padx=5, pady=5)
       self.txtNIDN.bind("<Return>",self.onCari)
       self.txtNama_Lengkap = Entry(mainFrame)
       self.txtNama_Lengkap.grid(row=1, column=1, padx=5, pady=5)
       self.txtJk = Entry(mainFrame)
       self.txtJk.grid(row=2, column=1, padx=5, pady=5)
       self.txtTelpon = Entry(mainFrame)
       self.txtTelpon.grid(row=3, column=1, padx=5, pady=5)
       self.txtEmail = Entry(mainFrame)
       self.txtEmail.grid(row=4, column=1, padx=5, pady=5)
       self.txtProdi = Entry(mainFrame)
       self.txtProdi.grid(row=5, column=1, padx=5, pady=5)


       # Button
       self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
       self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
       self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
       self.btnClear.grid(row=1, column=3, padx=5, pady=5)
       self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
       self.btnHapus.grid(row=2, column=3, padx=5, pady=5)


       # define columns
       columns = ('iddosen','nidn','nama_lengkap','jk','telpon','email','prodi')
       self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')

       # define headings
       self.tree.heading('iddosen', text='IDDOSEN')
       self.tree.column('iddosen', width='50')
       self.tree.heading('nidn', text='NIDN')
       self.tree.column('nidn', width='50')
       self.tree.heading('nama_lengkap', text='NAMA_LENGKAP')
       self.tree.column('nama_lengkap', width='50')
       self.tree.heading('jk', text='JK')
       self.tree.column('jk', width='50')
       self.tree.heading('telpon', text='TELPON')
       self.tree.column('telpon', width='50')
       self.tree.heading('email', text='EMAIL')
       self.tree.column('email', width='50')
       self.tree.heading('prodi', text='PRODI')
       self.tree.column('prodi', width='50')


       # set tree position
       self.tree.place(x=0, y=200)

   def onClear(self, event=None):
       self.txtNIDN.delete(0,END)
       self.txtNIDN.insert(END,'')
       self.txtNama_Lengkap.delete(0,END)
       self.txtNama_Lengkap.insert(END,'')
       self.txtJk.delete(0,END)
       self.txtJk.insert(END,'')
       self.txtTelpon.delete(0,END)
       self.txtTelpon.insert(END,'')
       self.txtEmail.delete(0,END)
       self.txtEmail.insert(END,'')
       self.txtProdi.delete(0,END)
       self.txtProdi.insert(END,'')
       self.btnSimpan.config(text='Simpan')
       self.onReload()
       self.ditemukan = False

   def onReload(self, event=None):
       A = Dosen()
       result = A.getAllData()
       for item in self.tree.get_children():
           self.tree.delete(item)
       array_list = []
       for row_data in result:
           array_list.append(row_data)

       for A in array_list:
           self.tree.insert('',END, values= A)

   def onCari(self, Event=None):
       nidn = self.txtNIDN.get()
       A = Dosen()
       res = A.getByNIDN(nidn)
       rec = A.affected
       if(rec>0):
           messagebox.showinfo("showinfo", "Data Ditemukan")
           self.TampilkanData()
           self.ditemukan = True
       else:
           messagebox.showwarning('showwarning', 'Data Tidak Ditemukan')
           self.ditemukan = False
       return res

   def TampilkanData(self, event=None):
       nidn = self.txtNIDN.get()
       A = Dosen()
       res = A.getByNIDN(nidn)

       self.txtNama_Lengkap.delete(0,END)
       self.txtNama_Lengkap.insert(END, A.nama_lengkap)
       self.txtJk.delete(0,END)
       self.txtJk.insert(END, A.jk)
       self.txtTelpon.delete(0,END)
       self.txtTelpon.insert(END, A.telpon)
       self.txtEmail.delete(0,END)
       self.txtEmail.insert(END, A.email)
       self.txtProdi.delete(0,END)
       self.txtProdi.insert(END, A.prodi)
       self.btnSimpan.config(text='Update')

   def onSimpan(self, event=None):
       nidn = self.txtNIDN.get()
       nama_lengkap = self.txtNama_Lengkap.get()
       jk = self.txtJk.get()
       telpon = self.txtTelpon.get()
       email = self.txtEmail.get()
       prodi = self.txtProdi.get()
       A = Dosen()
       A.nidn =  nidn
       A.nama_lengkap =  nama_lengkap
       A.jk =  jk
       A.telpon =  telpon
       A.email =  email
       A.prodi =  prodi
       if(self.ditemukan==True):
           res = A.updateByNIDN(nidn)
           ket = 'Diperbarui'
       else:
           res = A.simpan()
           ket = 'Disimpan'
       rec = A.affected
       if(rec>0):
           messagebox.showinfo('showinfo', 'Data Berhasil '+ket)
       else:
           messagebox.showwarning('showwarning', 'Data Gagal '+ket)
       self.onClear()
       return rec

   def onDelete(self, event=None):
       nidn = self.txtNIDN.get()
       A = Dosen()
       A.nidn = nidn
       if(self.ditemukan==True):
           res = A.deleteByNIDN(nidn)
           rec = A.affected
       else:
           messagebox.showinfo('showinfo', 'Data harus ditemukan dulu sebelum dihapus')
           rec = 0

       if(rec>0):
           messagebox.showinfo('showinfo', 'Data Berhasil dihapus')

       self.onClear()

   def onKeluar(self, event=None):
       self.parent.destroy()

if __name__ == '__main__':
   root = tk.Tk()
   aplikasi = FrmDosen(root, 'Aplikasi Data Dosen')
   root.mainloop()
