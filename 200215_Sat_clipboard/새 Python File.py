# b1.config(bg='yellow')
# b1.config(bg='SystemButtonFace')
import pyperclip
import tkinter as tk
from tkinter import ttk
w = tk.Tk();text ='''공무내역을
입력해주세요.'''
w.title('Clipboard');#w.geometry('250x250')
#버튼부
b1 = tk.Button(w,text = '공무',relief='raised',font='bold 50')

#하단부
하단배경 = 'white'
f1 = tk.Frame(w,relief='solid',bd=1,bg=하단배경)
_l1 = tk.Label(f1,text='공무내역 :',bg=하단배경,justify='center')
l1 = tk.Entry(f1,text=text,relief='solid',bd=2,bg=하단배경,)

#함수부
def checking():
    temp_p=pyperclip.paste();text = l1.get()
    if temp_p == text:b1.config(bg='yellow',relief='sunken')
    else:b1.config(relief='raised',bg='SystemButtonFace')
    w.after(200,checking)
def push_after_button():text = l1.get();pyperclip.copy(text)
    
#arrangement
b1.config(command=push_after_button)
b1.pack(padx=15,pady=15)
f1.pack(fill=tk.BOTH)
# _l1.grid(column=1,row=1,sticky='w')
# l1.grid(column=2,row=1,sticky='e)
_l1.pack(side='left')
l1.pack(fill='both')
# print(l1.grid_bbox())
checking()
w.mainloop()
