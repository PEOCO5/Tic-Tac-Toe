from tkinter import *
from TicTacToe.TkinterNumbers import Numbers
from PIL import Image, ImageTk


class Game(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.master.title('Tic-Tac-Toe')
        self.master.geometry('310x610')
        self.master.config(bg='magenta')
        self.master.resizable(width=False, height=False)

        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

        self.file = Menu(self.menu)
        self.file.add_command(label='Exit', command=self.game_exit, accelerator='Ctrl + W')
        self.master.bind('<Command-w>', self.game_exit)
        self.file.add_command(label='New Game', command=self.new_game, accelerator='Ctrl + N')
        self.master.bind('<Command-n>', self.new_game)
        self.menu.add_cascade(label='File', menu=self.file)

        self.canvas1 = Canvas(self.master, width=310, height=200, bg='black', bd=0)
        self.canvas1.place(x=0, y=410)
        self.score1 = Numbers.zero(self.canvas1, 60, 470 - 410, 130, 540 - 410, color='#AE7921', width=2)
        self.score01 = 0
        self.score2 = Numbers.zero(self.canvas1, 180, 470 - 410, 250, 540 - 410, color='#AE7921', width=2)
        self.score02 = 0

        self.canvas = None
        self.buttons = {}
        for i in range(1, 10):
            self.buttons[i] = NONE
        self.button_action = [self.but1, self.but2, self.but3, self.but4, self.but5, self.but6, self.but7, self.but8,
                              self.but9]
        self.count = 1

        self.start_game()

    @staticmethod
    def game_exit(event=None):
        exit()

    def start_game(self):
        self.count = 1

        self.canvas = Canvas(self.master, width=310, height=410, bg='black', bd=0)
        self.canvas.place(x=0, y=0)
        self.canvas.create_line(0, 310, 310, 310, fill='white')

        # Board
        self.canvas.create_line(105, 0o5, 105, 305, fill='red')
        self.canvas.create_line(205, 0o5, 205, 305, fill='red')
        self.canvas.create_line(0o5, 105, 305, 105, fill='red')
        self.canvas.create_line(0o5, 205, 305, 205, fill='red')

        # Hidden Buttons for 'X's and 'O's
        for i in self.buttons:
            self.buttons[i] = Button(self.master, width=8, height=4, bg='black', bd=0,
                                     command=self.button_action[i - 1])

        self.buttons[1].place(x=22, y=18)
        self.buttons[2].place(x=123, y=18)
        self.buttons[3].place(x=228, y=18)
        self.buttons[4].place(x=22, y=123)
        self.buttons[5].place(x=123, y=123)
        self.buttons[6].place(x=228, y=123)
        self.buttons[7].place(x=22, y=225)
        self.buttons[8].place(x=123, y=225)
        self.buttons[9].place(x=228, y=225)

        # Score Board Buttons
        self.canvas1.create_line(155.5, 0, 155.5, 200, fill='white', width=2)
        Button(self.master, text='     +1     ', bg='light green', bd=0, command=self.increase1).place(x=70, y=440)
        Button(self.master, text='     +1     ', bg='light green', bd=0, command=self.increase2).place(x=190, y=440)
        Button(self.master, text='     -1     ', bg='#FF6267', bd=0, command=self.decrease1).place(x=70, y=550)
        Button(self.master, text='     -1     ', bg='#FF6267', bd=0, command=self.decrease2).place(x=190, y=550)

        # Restart Game Button
        restart_game = Button(self.master, text='Restart Game', command=self.restart_game, bg='magenta')
        restart_game.place(x=115, y=350)

    @staticmethod
    def new_game(event=None):
        Game(Tk()).mainloop()

    def restart_game(self):
        self.canvas.place_forget()
        self.start_game()

    def create_x(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, fill='#88ECFF', width=3)
        self.canvas.create_line(x2, y1, x1, y2, fill='#88ECFF', width=3)

    def create_o(self, x1, y1, x2, y2):
        self.canvas.create_oval(x1, y1, x2, y2, outline='#4AFF80', width=3)

    def but1(self):
        self.buttons[1].place_forget()
        if self.count % 2 == 0:
            self.create_o(20, 20, 90, 90)
        else:
            self.create_x(20, 20, 90, 90)
        self.count += 1

    def but2(self):
        self.buttons[2].place_forget()
        if self.count % 2 == 0:
            self.create_o(120, 20, 190, 90)
        else:
            self.create_x(120, 20, 190, 90)
        self.count += 1

    def but3(self):
        self.buttons[3].place_forget()
        if self.count % 2 == 0:
            self.create_o(220, 20, 290, 90)
        else:
            self.create_x(220, 20, 290, 90)
        self.count += 1

    def but4(self):
        self.buttons[4].place_forget()
        if self.count % 2 == 0:
            self.create_o(20, 120, 90, 190)
        else:
            self.create_x(20, 120, 90, 190)
        self.count += 1

    def but5(self):
        self.buttons[5].place_forget()
        if self.count % 2 == 0:
            self.create_o(120, 120, 190, 190)
        else:
            self.create_x(120, 120, 190, 190)
        self.count += 1

    def but6(self):
        self.buttons[6].place_forget()
        if self.count % 2 == 0:
            self.create_o(220, 120, 290, 190)
        else:
            self.create_x(220, 120, 290, 190)
        self.count += 1

    def but7(self):
        self.buttons[7].place_forget()
        if self.count % 2 == 0:
            self.create_o(20, 220, 90, 290)
        else:
            self.create_x(20, 220, 90, 290)
        self.count += 1

    def but8(self):
        self.buttons[8].place_forget()
        if self.count % 2 == 0:
            self.create_o(120, 220, 190, 290)
        else:
            self.create_x(120, 220, 190, 290)
        self.count += 1

    def but9(self):
        self.buttons[9].place_forget()
        if self.count % 2 == 0:
            self.create_o(220, 220, 290, 290)
        else:
            self.create_x(220, 220, 290, 290)
        self.count += 1

    def increase1(self):
        if self.score01 == 0:
            self.canvas1.create_rectangle(59, 469 - 410, 131, 541 - 410, fill='black')
            self.score1 = Numbers.one(self.canvas1, 60, 470 - 410, 130, 540 - 410, color='#AE7921', width=2)
            self.score01 += 1
        elif self.score01 == 1:
            self.canvas1.create_rectangle(59, 469 - 410, 131, 541 - 410, fill='black')
            self.score1 = Numbers.two(self.canvas1, 60, 470 - 410, 130, 540 - 410, color='#AE7921', width=2)
            self.score01 += 1
        elif self.score01 == 2:
            self.canvas1.create_rectangle(59, 469 - 410, 131, 541 - 410, fill='black')
            self.score1 = Numbers.three(self.canvas1, 60, 470 - 410, 130, 540 - 410, color='#AE7921', width=2)
            self.score01 += 1
        elif self.score01 == 3:
            self.canvas1.create_rectangle(59, 469 - 410, 131, 541 - 410, fill='black')
            self.score1 = Numbers.four(self.canvas1, 60, 470 - 410, 130, 540 - 410, color='#AE7921', width=2)
            self.score01 += 1
        elif self.score01 == 4:
            self.canvas1.create_rectangle(59, 469 - 410, 131, 541 - 410, fill='black')
            self.score1 = Numbers.five(self.canvas1, 60, 470 - 410, 130, 540 - 410, color='#AE7921', width=2)
            self.score01 += 1

    def increase2(self):
        if self.score02 == 0:
            self.canvas1.create_rectangle(179, 469 - 410, 251, 541 - 410, fill='black')
            self.score2 = Numbers.one(self.canvas1, 180, 470 - 410, 250, 540 - 410, color='#AE7921', width=2)
            self.score02 += 1
        elif self.score02 == 1:
            self.canvas1.create_rectangle(179, 469 - 410, 251, 541 - 410, fill='black')
            self.score2 = Numbers.two(self.canvas1, 180, 470 - 410, 250, 540 - 410, color='#AE7921', width=2)
            self.score02 += 1
        elif self.score02 == 2:
            self.canvas1.create_rectangle(179, 469 - 410, 251, 541 - 410, fill='black')
            self.score2 = Numbers.three(self.canvas1, 180, 470 - 410, 250, 540 - 410, color='#AE7921', width=2)
            self.score02 += 1
        elif self.score02 == 3:
            self.canvas1.create_rectangle(179, 469 - 410, 251, 541 - 410, fill='black')
            self.score2 = Numbers.four(self.canvas1, 180, 470 - 410, 250, 540 - 410, color='#AE7921', width=2)
            self.score02 += 1
        elif self.score02 == 4:
            self.canvas1.create_rectangle(179, 469 - 410, 251, 541 - 410, fill='black')
            self.score2 = Numbers.five(self.canvas1, 180, 470 - 410, 250, 540 - 410, color='#AE7921', width=2)
            self.score02 += 1

    def decrease1(self):
        if self.score01 == 5:
            self.canvas1.create_rectangle(59, 469 - 410, 131, 541 - 410, fill='black')
            self.score1 = Numbers.four(self.canvas1, 60, 470 - 410, 130, 540 - 410, color='#AE7921', width=2)
            self.score01 -= 1
        elif self.score01 == 4:
            self.canvas1.create_rectangle(59, 469 - 410, 131, 541 - 410, fill='black')
            self.score1 = Numbers.three(self.canvas1, 60, 470 - 410, 130, 540 - 410, color='#AE7921', width=2)
            self.score01 -= 1
        elif self.score01 == 3:
            self.canvas1.create_rectangle(59, 469 - 410, 131, 541 - 410, fill='black')
            self.score1 = Numbers.two(self.canvas1, 60, 470 - 410, 130, 540 - 410, color='#AE7921', width=2)
            self.score01 -= 1
        elif self.score01 == 2:
            self.canvas1.create_rectangle(59, 469 - 410, 131, 541 - 410, fill='black')
            self.score1 = Numbers.one(self.canvas1, 60, 470 - 410, 130, 540 - 410, color='#AE7921', width=2)
            self.score01 -= 1
        elif self.score01 == 1:
            self.canvas1.create_rectangle(59, 469 - 410, 131, 541 - 410, fill='black')
            self.score1 = Numbers.zero(self.canvas1, 60, 470 - 410, 130, 540 - 410, color='#AE7921', width=2)
            self.score01 -= 1

    def decrease2(self):
        if self.score02 == 5:
            self.canvas1.create_rectangle(179, 469 - 410, 251, 541 - 410, fill='black')
            self.score2 = Numbers.four(self.canvas1, 180, 470 - 410, 250, 540 - 410, color='#AE7921', width=2)
            self.score02 -= 1
        elif self.score02 == 4:
            self.canvas1.create_rectangle(179, 469 - 410, 251, 541 - 410, fill='black')
            self.score2 = Numbers.three(self.canvas1, 180, 470 - 410, 250, 540 - 410, color='#AE7921', width=2)
            self.score02 -= 1
        elif self.score02 == 3:
            self.canvas1.create_rectangle(179, 469 - 410, 251, 541 - 410, fill='black')
            self.score2 = Numbers.two(self.canvas1, 180, 470 - 410, 250, 540 - 410, color='#AE7921', width=2)
            self.score02 -= 1
        elif self.score02 == 2:
            self.canvas1.create_rectangle(179, 469 - 410, 251, 541 - 410, fill='black')
            self.score2 = Numbers.one(self.canvas1, 180, 470 - 410, 250, 540 - 410, color='#AE7921', width=2)
            self.score02 -= 1
        elif self.score02 == 1:
            self.canvas1.create_rectangle(179, 469 - 410, 251, 541 - 410, fill='black')
            self.score2 = Numbers.zero(self.canvas1, 180, 470 - 410, 250, 540 - 410, color='#AE7921', width=2)
            self.score02 -= 1


Game(Tk()).mainloop()
