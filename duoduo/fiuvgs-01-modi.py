import tkinter
from tkinter import *
from PIL import Image, ImageTk


a = 2

score=0

def Option_box1():
    def selection():
        """"""
    top = Tk()
    top.title("第1题，共3题")

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

    R1 = Radiobutton(top, text="曲棍球", variable=radio, value=1, font=20, foreground="brown", command=selection)
    R1.pack(anchor=W)

    R2 = Radiobutton(top, text="棒球", variable=radio, value=2, font=20, command=selection)
    R2.pack(anchor=W)

    R3 = Radiobutton(top, text="冰球", variable=radio, value=3, font=20, foreground="blue", command=selection)
    R3.pack(anchor=W)

    label = Label(top)
    label.pack()

    def myMessage():
        if radio.get() == 3:
            global score
            score += 1
            import tkinter
            #img_gif = tkinter.PhotoImage(file='right.gif')
            img_gif=ImageTk.PhotoImage(file="duoduo/right.jpg")
            #label_img = tkinter.Label(top, image=img_gif)
            canvas.create_image(200, 200, image=img_gif, anchor="center")
            #label_img.place(x=100, y=200)
            #label_img.pack(side="left")
            #top.mainloop()
            #exit()
        else:
            import tkinter
            img_gif = tkinter.PhotoImage(file='wrong.gif')
            label_img = tkinter.Label(top, image=img_gif)
            label_img.place(x=100, y=200)
            #            label_img.pack(side="left")
            top.mainloop()
            exit()

    def myMessage1():
        exit()

    tkinter.Button(top, text="提交", font=20, foreground="green", command=myMessage).pack()
    tkinter.Button(top, text="退出", font=20, foreground="red", command=myMessage1).pack(side="left")

    tkinter.Button(top, text="下一题", foreground="dark blue", font=20, command=top.destroy).pack()
    top.mainloop()

def Option_box2():
    def selection():
        """"""
    top = Tk()
    top.title("第2题，共3题")

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

    R1 = Radiobutton(top, text="曲棍球", variable=radio, value=1, font=20, foreground="brown", command=selection)
    R1.pack(anchor=W)

    R2 = Radiobutton(top, text="棒球", variable=radio, value=2, font=20, command=selection)
    R2.pack(anchor=W)

    R3 = Radiobutton(top, text="冰球", variable=radio, value=3, font=20, foreground="blue", command=selection)
    R3.pack(anchor=W)

    label = Label(top)
    label.pack()

    def myMessage():
        if radio.get() == 3:
            global score
            score += 1
            import tkinter
            img_gif = tkinter.PhotoImage(file='right.gif')
            label_img = tkinter.Label(top, image=img_gif)
            label_img.place(x=100, y=200)
            #            label_img.pack(side="left")
            top.mainloop()
            exit()
        else:
            import tkinter
            img_gif = tkinter.PhotoImage(file='wrong.gif')
            label_img = tkinter.Label(top, image=img_gif)
            label_img.place(x=100, y=200)
            #            label_img.pack(side="left")
            top.mainloop()
            exit()

    def myMessage1():
        exit()

    tkinter.Button(top, text="提交", font=20, foreground="green", command=myMessage).pack()
    tkinter.Button(top, text="退出", font=20, foreground="red", command=myMessage1).pack(side="left")

    tkinter.Button(top, text="下一题", foreground="dark blue", font=20, command=top.destroy).pack()
    top.mainloop()


def Option_box3():
    def selection():
        """"""
    top = Tk()
    top.title("第3题，共3题")

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

    R1 = Radiobutton(top, text="曲棍球", variable=radio, value=1, font=20, foreground="brown", command=selection)
    R1.pack(anchor=W)

    R2 = Radiobutton(top, text="棒球", variable=radio, value=2, font=20, command=selection)
    R2.pack(anchor=W)

    R3 = Radiobutton(top, text="冰球", variable=radio, value=3, font=20, foreground="blue", command=selection)
    R3.pack(anchor=W)

    label = Label(top)
    label.pack()

    def myMessage():
        if radio.get() == 3:
            global score
            score += 1
            import tkinter
            img_gif = tkinter.PhotoImage(file='right.gif')
            label_img = tkinter.Label(top, image=img_gif)
            label_img.place(x=100, y=200)
            #            label_img.pack(side="left")
            top.mainloop()
            exit()
        else:
            import tkinter
            img_gif = tkinter.PhotoImage(file='wrong.gif')
            label_img = tkinter.Label(top, image=img_gif)
            label_img.place(x=100, y=200)
            #            label_img.pack(side="left")
            top.mainloop()
            exit()

    def myMessage1():
        exit()
    def myMessage2():
        global score
        tkinter.messagebox.showinfo('最终成绩', '你的最终成绩是： '+str(score))
        exit()

    tkinter.Button(top, text="提交", font=20, foreground="green", command=myMessage).pack()
    tkinter.Button(top, text="退出", font=20, foreground="red", command=myMessage1).pack(side="left")

    tkinter.Button(top, text="交卷", foreground="dark blue", font=20, command=myMessage2).pack()
    top.mainloop()

# 总运行
Option_box1()
Option_box2()
Option_box3()