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

take1 = Label(window, text="AParfin's timer",
              bg='#2B3641',
              fg='#4587B6',
              font=('Comic Sans MC', '30', 'bold'),
              bd=1)
take1.place(x=90, y=40)

entry1 = Entry(window,
               fg='#4587B6',
               bg='#2B3641',
               font=('Comic Sans MC', '30', 'bold'),
               bd=5)
entry1.place(x=125, y=180, width=200)

take3 = Label(window,
              text="",
              bg='#2B3641',
              fg='#4587B6',
              font=('Comic Sans MC', '30', 'bold'))


def time():
    global work
    work = False
    time1 = int(entry1.get())
    take3.place(x=290, y=280)
    work = True
    time2(time1)


def time2(sec):
    if sec > 0 and work:
        take3.config(text=str(sec))
        sec -= 1
        window.after(1000, time2, sec)
    else:
        sec = 0
        take3.config(text="Stopped")


button1 = Button(window,
                 font=('Comic Sans MC', '18', 'bold'),
                 text='Start',
                 bg='#2B3641',
                 fg='#4587B6',
                 highlightcolor='#2B11B5',
                 command=time)
button1.place(x=185, y=270)


def a():
    global work
    print('printed')
    work = False


button1 = Button(window,
                 font=('Comic Sans MC', '18', 'bold'),
                 text='Stop',
                 bg='#2B3641',
                 fg='#4587B6',
                 highlightcolor='#2B11B5',
                 command=a)
button1.place(x=185, y=334)


def Getting():
    if group1.get() == True:
        print("You have registered")
    else:
        print("You can't disagree")


group1 = BooleanVar()
group1.set(False)
flag = Checkbutton(window,
                   text='Minutes',
                   bg="#2B3641",
                   fg='#4587B6',
                   var=group1)
flag.place(x=10, y=14)

window.mainloop()
# ------------------------------------------------------------------------------------------


# take4 = Label(window,
#               text="",
#               bg='#2B3641',
#               fg='#4587B6',
#               font=('Comic Sans MC', '8', 'bold'))


# def box1_1():
#     take4.config(text=box1.get())
#     take4.place(x=10, y=70)
#
#
# button1 = Button(window,
#                  font=('Comic Sans MC', '8', 'bold'),
#                  text='Print',
#                  bg='#2B3641',
#                  fg='#4587B6',
#                  highlightcolor='#2B11B5',
#                  command=box1_1)
# button1.place(x=10, y=10)
#
# box1 = ttk.Combobox(window,
#                     state="normal",
#                     font=('Comic Sans MC', '8', 'bold'),
#                     values=['button1', 'button2', 'button3', 'button4', 'button5', 'button6', 'button7', 'button8',
#                             'button9', 'button10'])
# box1.current(0)
# box1.place(x=10, y=40)
