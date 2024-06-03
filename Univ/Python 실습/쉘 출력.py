from tkinter import *

def prtText():
    print(txt.get('1.0','end'))
def delText():
    txt.delete('1.0','end')
    
win = Tk()
win.title('텍스트 위젯')
txt = Text(win, width=30, height=5)
txt.grid(row=0, column=0, columnspan=2)
btn = Button(win, text='쉘 출력', command=prtText)
btn.grid(row=1, column=0)
btn2 = Button(win, text='삭제', command=delText)
btn2.grid(row=1, column=1)
win.mainloop()