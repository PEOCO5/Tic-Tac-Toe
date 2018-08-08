class Numbers:
    @staticmethod
    def zero(canvas, x1, y1, x2, y2, color='black', width=1):
        canvas.create_oval(x1, y1, x2, y2, outline=color, width=width)
        canvas.create_oval(x1 + (1 / 7 * (x2 - x1)), y1 + (1 / 7 * (y2 - y1)), x1 + (6 / 7 * (x2 - x1)),
                           y1 + (6 / 7 * (y2 - y1)), outline=color, width=width)

    @staticmethod
    def one(canvas, x1, y1, x2, y2, color='black', width=1):
        canvas.create_line(x1, y2, x2, y2, fill=color, width=width)
        canvas.create_line(x1, y2, x1, y2 - (1 / 5 * (y2 - y1)), fill=color, width=width)
        canvas.create_line(x1, y2 - (1 / 5 * (y2 - y1)), x1 + ((x2 - x1) * 35416 / 99999), y2 - (1 / 5 * (y2 - y1)),
                           fill=color, width=width)
        canvas.create_line(x2, y2, x2, y2 - (1 / 5 * (y2 - y1)), fill=color, width=width)
        canvas.create_line(x2, y2 - (1 / 5 * (y2 - y1)), x2 - ((x2 - x1) * 35416 / 99999), y2 - (1 / 5 * (y2 - y1)),
                           fill=color, width=width)
        canvas.create_line(x1 + ((x2 - x1) * 35416 / 99999), y2 - (1 / 5 * (y2 - y1)), x1 + ((x2 - x1) * 35416 / 99999),
                           y1 + (1 / 5 * (y2 - y1)), fill=color, width=width)
        canvas.create_line(x2 - ((x2 - x1) * 35416 / 99999), y2 - (1 / 5 * (y2 - y1)), x2 - ((x2 - x1) * 35416 / 99999),
                           y1, fill=color, width=width)
        canvas.create_line(x1 + (35416 / 99999 * (x2 - x1)), y1 + (1 / 5 * (y2 - y1)),
                           x1 + (3 / 8 * (35416 / 99999 * (x2 - x1))), y1 + (1 / 5 * (y2 - y1)),
                           fill=color, width=width)
        canvas.create_line(x1 + (3 / 8 * (35416 / 99999 * (x2 - x1))), y1 + (1 / 5 * (y2 - y1)),
                           x1 + (3 / 8 * (35416 / 99999 * (x2 - x1))), y1 + (1 / 10 * (y2 - y1)), fill=color,
                           width=width)
        canvas.create_line(x1 + (3 / 8 * (35416 / 99999 * (x2 - x1))), y1 + (1 / 10 * (y2 - y1)),
                           x1 + ((x2 - x1) * 35416 / 99999), y1, fill=color, width=width)
        canvas.create_line(x1 + ((x2 - x1) * 35416 / 99999), y1, x2 - ((x2 - x1) * 35416 / 99999), y1, fill=color,
                           width=width)

    @staticmethod
    def two(canvas, x1, y1, x2, y2, color='black', width=1):
        canvas.create_line(x1, y2, x2, y2, fill=color, width=width)
        canvas.create_line(x1, y2, x1, y2 - (1 / 5 * (y2 - y1)), fill=color, width=width)
        canvas.create_line(x2, y2, x2, y2 - (1 / 5 * (y2 - y1)), fill=color, width=width)
        canvas.create_line(x2, y2 - (1 / 5 * (y2 - y1)), x1 + (1 / 3 * (x2 - x1)), y2 - (1 / 5 * (y2 - y1)), fill=color,
                           width=width)
        midx, midy = x1 + (1 / 3 * (x2 - x1)), (y1 + (y2 - (3 / 10 * (y2 - y1)))) / 2
        canvas.create_arc(midx - (midx - x1), midy - (midy - y1), midx + (midx - x1), midy + (midy - y1), start=130,
                          extent=-190, style='arc', outline=color, width=width)
        canvas.create_arc(midx - (1 / 2 * (midx - (midx - (midx - x1)))),
                          midy - (1 / 2 * (midy - (midy - (midy - y1)))),
                          midx + (1 / 2 * (midx - (midx - (midx - x1)))),
                          midy + (1 / 2 * (midy - (midy - (midy - y1)))), start=130, extent=-180, style='arc',
                          outline=color, width=width)
        canvas.create_line(midx + 10, midy + 7, x1, y2 - (1 / 5 * (y2 - y1)), fill=color, width=width)
        canvas.create_line(x1 + (1 / 3 * (x2 - x1)), y2 - (1 / 5 * (y2 - y1)), midx + 14, midy + 20, fill=color,
                           width=width)
        canvas.create_line(midx - 8, midy - 9, midx - 17, midy - 19, fill=color, width=width)

    @staticmethod
    def three(canvas, x1, y1, x2, y2, color='black', width=1):
        canvas.create_line(x1, y2, x2 - (3 / 5 * (x2 - x1)), y2, fill=color, width=width)
        canvas.create_line(x1, y2 - (1 / 7 * (y2 - y1)), x2 - (3 / 5 * (x2 - x1)), y2 - (1 / 7 * (y2 - y1)), fill=color,
                           width=width)
        canvas.create_line(x1, y2, x1, y2 - (1 / 7 * (y2 - y1)), fill=color, width=width)
        canvas.create_line(x1, y2 - (3 / 7 * (y2 - y1)), x2 - (3 / 5 * (x2 - x1)), y2 - (3 / 7 * (y2 - y1)), fill=color,
                           width=width)
        canvas.create_line(x1, y2 - (4 / 7 * (y2 - y1)), x2 - (3 / 5 * (x2 - x1)), y2 - (4 / 7 * (y2 - y1)), fill=color,
                           width=width)
        canvas.create_line(x1, y2 - (3 / 7 * (y2 - y1)), x1, y2 - (4 / 7 * (y2 - y1)), fill=color, width=width)
        canvas.create_line(x1, y2 - (6 / 7 * (y2 - y1)), x2 - (3 / 5 * (x2 - x1)), y2 - (6 / 7 * (y2 - y1)), fill=color,
                           width=width)
        canvas.create_line(x1, y2 - (7 / 7 * (y2 - y1)), x2 - (3 / 5 * (x2 - x1)), y2 - (7 / 7 * (y2 - y1)), fill=color,
                           width=width)
        canvas.create_line(x1, y2 - (6 / 7 * (y2 - y1)), x1, y2 - (7 / 7 * (y2 - y1)), fill=color, width=width)
        midx, midy = x2 - (3 / 5 * (x2 - x1)), y2 - (3 / 7 * (y2 - y1)) - (1 / 2 * ((y2 - (3 / 7 * (y2 - y1))) -
                                                                                    (y2 - (1 / 7 * (y2 - y1)))))
        canvas.create_arc(midx - ((x2 - (1 / 5 * (x2 - x1))) - midx), midy - (midy - (y2 - (3 / 7 * (y2 - y1)))) - 1,
                          midx + ((x2 - (1 / 5 * (x2 - x1))) - midx), midy + ((y2 - (1 / 7 * (y2 - y1))) - midy),
                          start=90, extent=-180, style='arc', outline=color, width=width)
        midx, midy = x2 - (3 / 5 * (x2 - x1)), y2 - (6 / 7 * (y2 - y1)) - (1 / 2 * ((y2 - (6 / 7 * (y2 - y1))) -
                                                                                    (y2 - (4 / 7 * (y2 - y1)))))
        canvas.create_arc(midx - ((x2 - (1 / 5 * (x2 - x1))) - midx), midy - (midy - (y2 - (6 / 7 * (y2 - y1)))) - 1,
                          midx + ((x2 - (1 / 5 * (x2 - x1))) - midx), midy + ((y2 - (4 / 7 * (y2 - y1))) - midy),
                          start=90, extent=-180, style='arc', outline=color, width=width)
        midx, midy = x2 - (3 / 5 * (x2 - x1)), y2 - (1 / 2 * (y2 - (y2 - (4 / 7 * (y2 - y1)))))
        canvas.create_arc(midx - (x2 - midx), midy - (y2 - midy) - 1, midx + (x2 - midx),
                          midy + (midy - (y2 - (4 / 7 * (y2 - y1)))), start=48, extent=-140, style='arc', outline=color,
                          width=width)
        midx, midy = x2 - (3 / 5 * (x2 - x1)), y2 - (3 / 7 * (y2 - y1)) - (1 / 2 * ((y2 - (3 / 7 * (y2 - y1))) - y1))
        canvas.create_arc(midx - (x2 - midx), midy - ((y2 - (3 / 7 * (y2 - y1))) - midy) - 1, midx + (x2 - midx),
                          midy + (midy - y1), start=100, extent=-148, style='arc', outline=color,
                          width=width)

    @staticmethod
    def four(canvas, x1, y1, x2, y2, color='black', width=1):
        canvas.create_line(x1, y1, x1, y1 + (1 / 2 * (y2 - y1)), fill=color, width=width)
        canvas.create_line(x1 + (1 / 3 * (x2 - x1)), y1, x1 + (1 / 3 * (x2 - x1)), y1 + (1 / 4 * (y2 - y1)), fill=color,
                           width=width)
        canvas.create_line(x1 + (1 / 3 * (x2 - x1)), y1, x1, y1, fill=color, width=width)
        canvas.create_line(x1 + (1 / 3 * (x2 - x1)), y1 + (1 / 4 * (y2 - y1)), x1 + (2 / 3 * (x2 - x1)),
                           y1 + (1 / 4 * (y2 - y1)), fill=color, width=width)
        canvas.create_line(x1 + (2 / 3 * (x2 - x1)), y1 + (1 / 4 * (y2 - y1)), x1 + (2 / 3 * (x2 - x1)), y1, fill=color,
                           width=width)
        canvas.create_line(x1, y1 + (1 / 2 * (y2 - y1)), x1 + (2 / 3 * (x2 - x1)), y1 + (1 / 2 * (y2 - y1)), fill=color,
                           width=width)
        canvas.create_line(x1 + (2 / 3 * (x2 - x1)), y1 + (1 / 2 * (y2 - y1)), x1 + (2 / 3 * (x2 - x1)), y2, fill=color,
                           width=width)
        canvas.create_line(x1 + (2 / 3 * (x2 - x1)), y2, x2, y2, fill=color, width=width)
        canvas.create_line(x2, y1, x2, y2, fill=color, width=width)
        canvas.create_line(x2, y1, x1 + (2 / 3 * (x2 - x1)), y1, fill=color, width=width)

    @staticmethod
    def five(canvas, x1, y1, x2, y2, color='black', width=1):
        canvas.create_line(x1, y1, x2, y1, fill=color, width=width)
        canvas.create_line(x2, y1, x2, y1 + (1 / 4 * (y2 - y1)), fill=color, width=width)
        canvas.create_line(x2, y1 + (1 / 4 * (y2 - y1)), x1 + (1 / 4 * (x2 - x1)), y1 + (1 / 4 * (y2 - y1)), fill=color,
                           width=width)
        canvas.create_line(x1 + (1 / 4 * (x2 - x1)), y1 + (1 / 4 * (y2 - y1)), x1 + (1 / 4 * (x2 - x1)),
                           y1 + (1 / 2 * (y2 - y1)), fill=color, width=width)
        canvas.create_line(x1, y1, x1, y1 + (5 / 8 * (y2 - y1)), fill=color, width=width)
        midx, midy = x1 + (1 / 4 * (x2 - x1)), y2 - (1 / 2 * (y2 - (y1 + (1 / 2 * (y2 - y1)))))
        canvas.create_arc(midx - (x2 - midx), midy - (y2 - midy) - 2, midx + (x2 - midx),
                          midy + (midy - (y1 + (1 / 2 * (y2 - y1)))), start=90, extent=-200, style='arc', outline=color,
                          width=width)
        canvas.create_arc(midx - (1 / 2 * (midx - (midx - (x2 - midx)))),
                          midy - (1 / 2 * (midy - (midy - (y2 - midy)))),
                          midx + (1 / 2 * (midx - (midx - (x2 - midx)))),
                          midy + (1 / 2 * (midy - (midy - (y2 - midy)))), start=90, extent=-220, style='arc',
                          outline=color, width=width)
        canvas.create_line(x1 - 1, y1 + (5 / 8 * (y2 - y1)), midx, y1 + (5 / 8 * (y2 - y1)) + 1, fill=color,
                           width=width)
        canvas.create_line(x1, y2 - 1, x1, y2 - 10, fill=color, width=width)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
'''
from tkinter import *

root = Tk()
root.geometry('900x900')
root.bind('<Command - w>', exit)

test = Canvas(root, width=900, height=900, bg='black')
test.place(x=0, y=0)
test.create_line(0, 470, 900, 470, fill='green')
test.create_line(0, 540, 900, 540, fill='green')

Numbers.five(test, 60, 470, 130, 540, color='#AE7921', width=2)
root.mainloop()
'''
