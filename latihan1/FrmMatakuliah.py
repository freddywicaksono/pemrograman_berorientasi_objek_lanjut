import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox

from Matakuliah import *
class FrmMatakuliah:

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
       Label(mainFrame, text='Kodemk:').grid(row=0, column=0,
           sticky=W, padx=5, pady=5)
       Label(mainFrame, text='Namamk:').grid(row=1, column=0,
           sticky=W, padx=5, pady=5)
       Label(mainFrame, text='Sks:').grid(row=2, column=0,
           sticky=W, padx=5, pady=5)
       Label(mainFrame, text='Kode_Prodi:').grid(row=3, column=0,
           sticky=W, padx=5, pady=5)


       # Textbox
       self.txtKODEMK = Entry(mainFrame)
       self.txtKODEMK.grid(row=0, column=1, padx=5, pady=5)
       self.txtKODEMK.bind("<Return>",self.onCari)
       self.txtNamamk = Entry(mainFrame)
       self.txtNamamk.grid(row=1, column=1, padx=5, pady=5)
       self.txtSks = Entry(mainFrame)
       self.txtSks.grid(row=2, column=1, padx=5, pady=5)
       self.txtKode_Prodi = Entry(mainFrame)
       self.txtKode_Prodi.grid(row=3, column=1, padx=5, pady=5)


       # Button
       self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
       self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
       self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
       self.btnClear.grid(row=1, column=3, padx=5, pady=5)
       self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
       self.btnHapus.grid(row=2, column=3, padx=5, pady=5)


       # define columns
       columns = ('idmk','kodemk','namamk','sks','kode_prodi')
       self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')

       # define headings
       self.tree.heading('idmk', text='IDMK')
       self.tree.column('idmk', width='50')
       self.tree.heading('kodemk', text='KODEMK')
       self.tree.column('kodemk', width='50')
       self.tree.heading('namamk', text='NAMAMK')
       self.tree.column('namamk', width='50')
       self.tree.heading('sks', text='SKS')
       self.tree.column('sks', width='50')
       self.tree.heading('kode_prodi', text='KODE_PRODI')
       self.tree.column('kode_prodi', width='50')
# ubahlah nilai width utk menyesuaikan lebarnya


       # set tree position
       
       self.tree.place(x=0, y=200, width=500) # ubahlah nilai y jika kotak entry > 6 sehingga tampilannya tdk menutupi kotak entry

   def onClear(self, event=None):
       self.txtKODEMK.delete(0,END)
       self.txtKODEMK.insert(END,'')
       self.txtNamamk.delete(0,END)
       self.txtNamamk.insert(END,'')
       self.txtSks.delete(0,END)
       self.txtSks.insert(END,'')
       self.txtKode_Prodi.delete(0,END)
       self.txtKode_Prodi.insert(END,'')
       self.btnSimpan.config(text='Simpan')
       self.onReload()
       self.ditemukan = False

   def onReload(self, event=None):
       A = Matakuliah()
       result = A.getAllData()
       for item in self.tree.get_children():
           self.tree.delete(item)
       array_list = []
       for row_data in result:
           array_list.append(row_data)

       for A in array_list:
           self.tree.insert('',END, values= A)

   def onCari(self, Event=None):
       kodemk = self.txtKODEMK.get()
       A = Matakuliah()
       res = A.getByKODEMK(kodemk)
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
       kodemk = self.txtKODEMK.get()
       A = Matakuliah()
       res = A.getByKODEMK(kodemk)

       self.txtNamamk.delete(0,END)
       self.txtNamamk.insert(END, A.namamk)
       self.txtSks.delete(0,END)
       self.txtSks.insert(END, A.sks)
       self.txtKode_Prodi.delete(0,END)
       self.txtKode_Prodi.insert(END, A.kode_prodi)
       self.btnSimpan.config(text='Update')

   def onSimpan(self, event=None):
       kodemk = self.txtKODEMK.get()
       namamk = self.txtNamamk.get()
       sks = self.txtSks.get()
       kode_prodi = self.txtKode_Prodi.get()
       A = Matakuliah()
       A.kodemk =  kodemk
       A.namamk =  namamk
       A.sks =  sks
       A.kode_prodi =  kode_prodi
       if(self.ditemukan==True):
           res = A.updateByKODEMK(kodemk)
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
       kodemk = self.txtKODEMK.get()
       A = Matakuliah()
       A.kodemk = kodemk
       if(self.ditemukan==True):
           res = A.deleteByKODEMK(kodemk)
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
   aplikasi = FrmMatakuliah(root, 'Aplikasi Data Matakuliah')
   root.mainloop()
