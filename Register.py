from tkinter import ttk
from tkinter import *
from time import sleep

window = Tk()
window.title('Timer By AParfin')
window.geometry('450x450')
window.wm_attributes('-alpha', 0.9)
window.attributes('-topmost', 0)
window.wm_iconbitmap('icon.ico')
window.resizable(False, False)
window['bg'] = '#458098'

take1 = Label(window,
              text="{Register}",
              bg='#458098',
              fg='#2B3641',
              font=('Comic Sans MC', '30', 'bold'))
take1.place(x=110, y=40)

group1 = BooleanVar()
group1.set(True)
flag = Checkbutton(window,
                   text='Agree with all rules',
                   var=group1,
                   font=('Comic Sans MC', '10', 'bold'))
flag.place(x=150, y=380)

entry1 = Entry(window,
               fg='#4587B6',
               bg='#2B3641',
               font=('Comic Sans MC', '30', 'bold'),
               bd=5)
entry1.place(x=125, y=180, width=200)


def Pass():
    password = entry1.get()
    for i in password:
        if group1.get() == False or i in "@%&*№!?":
            print('Password is wrong')
            break
        else:
            print('Password is right')
            break


button1 = Button(window,
                 font=('Comic Sans MC', '18', 'bold'),
                 text='Done',
                 bg='#2B3641',
                 fg='#4587B6',
                 highlightcolor='#2B11B5',
                 command=Pass)
button1.place(x=185, y=290)

mainloop()
