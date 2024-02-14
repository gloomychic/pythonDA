from turtle import *
speed ('slowest')
pencolor('blue')
pensize (2)

for i in range(8):
    fd(120)
    rt(45)
    write(f'n={i+1}', font=("Calibri", 12,))

hideturtle()
mainloop()