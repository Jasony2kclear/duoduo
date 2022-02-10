import tkinter
from tkinter import *

a = 2


def Option_box1():
    def selection():
        """"""

    top = Tk()
    top.title("the path")

    radio = IntVar()

    canvas = Canvas(top, width=400, height=300)
    canvas.pack()

    import turtle as t
    theScreen = t.TurtleScreen(canvas)

    theScreen.bgcolor("light blue")

    t = t.RawTurtle(theScreen)

    t.hideturtle()
    t.speed(10)

    t.up()
    t.goto(76, 60)
    t.down()

    t.circle(15)

    t.up()
    t.goto(60, 48)
    t.down()
    t.forward(40)
    t.right(120)
    t.forward(100)
    t.setheading(180)
    t.forward(20)
    t.setheading(0)
    t.right(45)
    t.forward(20)

    t.up()
    t.goto(60, 48)
    t.down()

    t.right(10)
    t.forward(100)
    t.right(125)
    t.forward(20)
    t.setheading(0)
    t.right(45)
    t.forward(20)

    t.up()
    t.goto(60, 48)
    t.down()

    t.right(10)
    t.forward(15)
    t.right(75)
    t.forward(90)
    t.right(90)
    t.forward(20)

    t.up()
    t.forward(35)
    t.down()
    t.begin_fill()
    t.color('black')
    t.circle(6)
    t.end_fill()

    #################################################################################################

    R1 = Radiobutton(top, text="速度滑冰", variable=radio, value=1, font=20, foreground="brown", command=selection)
    R1.pack(anchor=W)

    R2 = Radiobutton(top, text="短道速滑", variable=radio, value=2, font=20, command=selection)
    R2.pack(anchor=W)

    R3 = Radiobutton(top, text="花样滑冰", variable=radio, value=3, font=20, foreground="blue", command=selection)
    R3.pack(anchor=W)

    label = Label(top)
    label.pack()

    def myMessage():
        if radio.get() == 3:
            import tkinter
            img_gif = tkinter.PhotoImage(file='be.gif')
            label_img = tkinter.Label(top, image=img_gif)
            label_img.place(x=100, y=200)
            #            label_img.pack(side="left")
            top.mainloop()
        else:
            import tkinter
            img_gif = tkinter.PhotoImage(file='叉叉1.gif')
            label_img = tkinter.Label(top, image=img_gif)
            label_img.place(x=100, y=200)
            #            label_img.pack(side="left")
            top.mainloop()

    def myMessage1():
        exit()

    tkinter.Button(top, text="提交", font=20, foreground="green", command=myMessage).pack()
    tkinter.Button(top, text="退出", font=20, foreground="red", command=myMessage1).pack(side="left")

    def Option_box2():
        pass
    tkinter.Button(top, text="下一题", foreground="dark blue", font=20, command=Option_box2).pack()
    top.mainloop()

