from tkinter import *

def btnEvent():
    lab2.config(text='계산 결과 : ' + str(eval(entry.get())))


win = Tk()
win.title('수식 계산기')
lab = Label(win, text=' 수식 입력 : ')
lab.grid(row=1, column=1)
entry = Entry(win, width = 20)
entry.grid(row=1, column=2)
btn = Button(win, text='계산', command=btnEvent)
btn.grid(row=2, column=1, columnspan=2)
lab2 = Label(win, text=' ', height=3)
lab2.grid(row=3, column=1, columnspan=2)
win.mainloop()
