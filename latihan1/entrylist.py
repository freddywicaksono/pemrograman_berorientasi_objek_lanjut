import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Entry App")
        
        # create a dictionary to store data
        self.data = {}
        
        # create a label and entry widget for name
        tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # create a label and entry widget for age
        tk.Label(root, text="Age:").grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(root)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # create a button to save data
        tk.Button(root, text="Save", command=self.save_data).grid(row=2, column=1, padx=5, pady=5)
        
        # create a TreeView widget to display data
        self.tree = ttk.Treeview(root, columns=("name", "age"))
        self.tree.heading("name", text="Name")
        self.tree.heading("age", text="Age")
        self.tree.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
    def save_data(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        
        # save data to dictionary
        self.data[name] = age
        
        # clear entry widgets
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        
        # update TreeView with new data
        self.tree.insert("", tk.END, text=name, values=(age,))
        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
