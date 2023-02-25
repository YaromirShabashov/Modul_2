from random import *
from tkinter import *
root = Tk()
root.title("Задача №9")
root.geometry("400x400")
values_of_a = [1, 2, 3]
a = choice(values_of_a)
x = randint(0, 150)
y = randint(0, 150)
side = randint(0, 150)
canvas_width, canvas_height = 300, 300
canvas=Canvas(root, width=canvas_width, height=canvas_height, bg='black')
canvas.pack()
clicks = 0
def func():
 global clicks, a, x, y, side, color_figure
 clicks += 1
 if a == 1:
    square = canvas.create_rectangle(x, y, x+side, y+side, fill='blue')
 if a == 2:
    circle = canvas.create_oval(x, y, x+side, y+side, fill='blue')
 if a == 3:
    x_1 = randint(0, 300)
    x_2 = randint(0, 300)
    x_3 = randint(0, 300)
    y_1 = randint(0, 300)
    y_2 = randint(0, 300)
    y_3 = randint(0, 300)   
    triangle = canvas.create_polygon(x_1, x_2, x_3, y_1, y_2, y_3, fill='blue')
 if clicks >= 2:
    a = choice(values_of_a)
    x = randint(0, 150)
    y = randint(0, 150)
    side = randint(0, 150)
    canvas.delete("all")
    if a == 1:
       square = canvas.create_rectangle(x, y, x+side, y+side, fill='blue')
    if a == 2:
       circle = canvas.create_oval(x, y, x+side, y+side, fill='blue')
    if a == 3:
       x_1 = randint(0, 300)
       x_2 = randint(0, 300)
       x_3 = randint(0, 300)
       y_1 = randint(0, 300)
       y_2 = randint(0, 300)
       y_3 = randint(0, 300)   
       triangle = canvas.create_polygon(x_1, x_2, x_3, y_1, y_2, y_3, fill='blue')
button_1 = Button(text='Пуск', command=func)
button_1.pack()
root.mainloop()
