from tkinter import *
import random
root = Tk()
canvas = Canvas(root, width = 200, height = 200, bg = 'yellow')
canvas.pack()
def put():
    global b
    b=Button(root, text='Нажми', activebackground='red', command=rand).pack()
def rand():
    a = random.randint(1,3)
    if a == 1:
        canvas.delete('all') 
        c = canvas.create_rectangle(15, 15, 190, 110)    
    elif a == 2:
        canvas.delete('all') 
        b = canvas.create_oval(15, 15, 190, 110)      
    elif a == 3:
        canvas.delete('all') 
        z = canvas.create_polygon(15, 15, 190, 110, 50, 120, fill='yellow', outline='black')
root.title('Приложение')
root.geometry('1000x700')
root.resizable(width = False, height = False)
put()
root.mainloop()