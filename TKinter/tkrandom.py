__author__ = 'jinfeng'

from Tkinter import *
import random

class Application(Frame):
    def say_hi(self):
        randint = random.randrange(10)
        print randint
        self.readme['fg'] = 'blue'
        self.readme['text'] = randint

    def createWidgets(self):
        self.readme = Label(self)
        self.readme["text"] = '0'
        self.readme["fg"] = 'red'
        self.readme.pack(padx = 30, pady = 30)

        self.hi_there = Button(self)
        self.hi_there["text"] = "Run",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left", "padx":"40", "pady":"40"})


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

if __name__ == '__main__':
    root = Tk()
    app = Application(master = root)
    app.mainloop()