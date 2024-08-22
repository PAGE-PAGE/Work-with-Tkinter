from tkinter import ttk
from tkinter import *
import os
import json
import shutil
from tkinter import filedialog, messagebox

window = Tk()
window.title('File manger')
window.geometry('450x450')
window.wm_attributes('-alpha', 0.97)
window.attributes('-topmost', 0)
window.wm_iconbitmap('icon.ico')
window.resizable(False, False)
window['bg'] = '#990066'

# -------------------------------------------------------------------------------LABELS--------------------------------------------------------------------------------------------------------------------------------------------

result = Label(window,
               bg='#990066',
               text="",
               fg='#464451',
               font=('Comic Sans MC', '100', 'bold'))
result.place(x=314, y=310)

Name = Label(window,
             bg='#990066',
             text="⟪AParfin's file mover⟫",
             fg='#464451',
             font=('Comic Sans MC', '30', 'bold'))
Name.place(x=14, y=18)

# ------------------------------------------------------------------------------FUNCTIONS--------------------------------------------------------------------------------------------------------------------------------------------


def saving(source, distinction):
    with open('Test.json', 'r') as file:
        dict2 = json.load(file)
    dict2["entry1"] = source
    dict2["entry2"] = distinction
    with open('Test.json', 'w') as file:
        json.dump(dict2, file, ensure_ascii=False, indent=4)


def file_moving():
    global source
    source = source_entry.get()
    global distinction
    distinction = distinction_entry.get()
    if not os.path.exists(source):
        result.config(text="✕")
        return
    if not os.path.exists(distinction):
        result.config(text="✕")
        return
    try:
        for item in os.listdir(source):
            s = os.path.join(source, item)
            d = os.path.join(distinction, item)
            shutil.move(s, d)
        result.config(text="✓")
        saving(source, distinction)
    except:
        result.config(text="✕")


def reset():
    source_entry.delete(0, END)
    distinction_entry.delete(0, END)
    source_entry.insert(0, distinction)
    distinction_entry.insert(0, source)


def source_selection():
    folder_selection = filedialog.askdirectory()
    source_entry.delete(0, END)
    source_entry.insert(0, folder_selection)


def select_distinction():
    folder_selection = filedialog.askdirectory()
    distinction_entry.delete(0, END)
    distinction_entry.insert(0, folder_selection)


# ------------------------------------------------------------------------------ENTRIES-------------------------------------------------------------------------------------------------------------------------------------------

source_entry = Entry(window,
                     bg='#464451',
                     fg='#CD9575',
                     font=('Comic Sans MC', '20', 'bold'),
                     highlightcolor='#FFEFD5')
source_entry.place(x=15, y=110, width=330)

distinction_entry = Entry(window,
                          bg='#464451',
                          fg='#CD9575',
                          font=('Comic Sans MC', '20', 'bold'),
                          highlightcolor='#FFEFD5')
distinction_entry.place(x=15, y=210, width=330)

# ------------------------------------------------------------------------------BUTTONS------------------------------------------------------------------------------------------------------------------------------------------

select_source_button = Button(window,
                              bg='#464451',
                              text='Select',
                              fg='#CD9575',
                              font=('Comic Sans MC', '15', 'bold'),
                              highlightcolor='#FFEFD5',
                              command=source_selection)
select_source_button.place(x=360, y=107)

select_distinction_button = Button(window,
                                   bg='#464451',
                                   text='Select',
                                   fg="#CD9575",
                                   font=('Comic Sans MC', '15', 'bold'),
                                   highlightcolor='#FFEFD5',
                                   command=select_distinction)
select_distinction_button.place(x=360, y=207)

file_moving_button = Button(window,
                            bg='#464451',
                            text='⟪Move⟫',
                            fg="#CD9575",
                            font=('Comic Sans MC', '35', 'bold'),
                            highlightcolor='#FFEFD5',
                            command=file_moving)
file_moving_button.place(x=14, y=300)

reset = Button(window,
               bg='#464451',
               text='Reset',
               fg="#CD9575",
               font=('Comic Sans MC', '15', 'bold'),
               highlightcolor='#FFEFD5',
               command=reset)
reset.place(x=362, y=157)
# ------------------------------------------------------------------------------FILE SAVING------------------------------------------------------------------------------------------------------------------------------------------
try:
    with open('Test.json', 'r') as file:
        dict2 = json.load(file)
        source_entry.insert(0, dict2["entry1"])
        distinction_entry.insert(0, dict2["entry2"])
except:
    print('File does not exist')

window.mainloop()
