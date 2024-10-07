from tkinter import *

def etryEvent(event):
    lab2.config(text = '당신의 이름은 '+\
        entry.get() +' 입니다.')
    
win = Tk()
win.title('ex 6-3')
win.geometry('250x100')
lab = Label(win, text=' 이름 입력 : ')
lab.grid(row=1, column=1)
entry = Entry(win, width = 20)
frame = Frame(win)
btn = Button(frame, text = '확인', command= etryEvent)
entry.grid(row=1, column=2)
lab2 = Label(win, text='', height=3)
lab2.grid(row=2, column=1, columnspan=2)
win.mainloop()
