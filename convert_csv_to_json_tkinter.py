import pandas as pd 
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

#Main display box text/label (not a button)
label1 = tk.Label(root, text='File Conversion Tool', bg = 'lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150,60, window=label1)

def getCSV():
    global read_file
    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_csv(import_file_path)

#Button to import CSV
browseButton_CSV = tk.Button(text=' Import CSV File ', command = getCSV, bg = 'green', fg = 'white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_CSV)

def convert_to_JSON():
    global read_file
    export_file_path = filedialog.asksaveasfilename(defaultextension='.json')
    read_file.to_json(export_file_path)

#Button to convert CSV to JSON file and save it
saveAsButton_JSON = tk.Button(text='Convert CSV to JSON', command=convert_to_JSON, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_JSON)

def exitApplication():
    MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the app?', icon='warning')
    if MsgBox == 'yes':
        root.destroy()

#Button to exit app
exitButton = tk.Button(root, text=' Exit Application ', command=exitApplication, bg = 'red', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()