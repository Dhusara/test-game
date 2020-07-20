from tkinter import*
from random import*

sticks = 25

window = Tk()
window.geometry = ('600x300')

title = Label(window, text='Выберите число от 1 до 3', font=('Arial Bold', 10))
title.pack()

title2 = Label(window, text='Победит тот, у кого будет четное кол-во спичек.', font=('Arial Bold', 10))
title2.pack()

entry = Entry(window, width=15)
entry.pack()

match = Label(window, text=sticks*'| ', font=('Arial Bold', 25))
match.pack()

number = Label(window, text=str(sticks), font=('Arial Bold', 25))
number.pack()

def user():
    global sticks
    a = int(entry.get())
    my_sticks = 0 + a
    if (a in [1, 2, 3]) and (sticks - a) >= 0:
        sticks = sticks - a
        match.config(text = sticks * '| ')
        number.config(text = str(sticks))
        title.config(text = 'Введите число 1 - 3')

def computer():
    global sticks
    if sticks < 25:
        p = randint(1, 3)
        computer_sticks = 0 + p
        if sticks - p >= 0:
            sticks = sticks - p
            match.config(text = sticks * '| ')
            number.config(text = str(sticks))

def end():
    global sticks
    p = randint(1, 3)
    computer_sticks = 0 + p
    if sticks == 0 and computer_sticks % 2 == 1:
        number.config(text = 'Вы выиграли!', fg = 'green')
    else:
        number.config(text = 'Компьютер выиграл!', fg = 'red')

user_button = Button(window, text='Я', font=('Arial Bold', 10), width=40, command=user)
user_button.config(bg='#aaffff')
user_button.pack()

computer_button = Button(window, text='Компьютер', font=('Arial Bold', 10), width=40, command=computer)
computer_button.config(bg='#ffaaaa')
computer_button.pack()

end_button = Button(window, text='Итог', font=('Arial Bold', 10), width=40, command=end)
end_button.pack()

window.mainloop()

