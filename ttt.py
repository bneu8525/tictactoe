from tkinter import *


class TTT:
    def __init__(self, master):
        self.mymaster = master

        #leftside buttons
        self.leftsidebuttons = Frame(self.mymaster)
        self.leftsidebuttons.pack()

        self.topleftbutton = Button(self.leftsidebuttons, width=10, height=5, background="white")
        self.topleftbutton.pack(side=LEFT)
        self.topleftbutton.bind("<Button-1>", lambda event, obj=self.topleftbutton, square=1: self.tictac(event, obj,
                                                                                                          square))

        self.middleleftbutton = Button(self.leftsidebuttons, width=10, height=5, bg="white")
        self.middleleftbutton.pack(side=LEFT)
        self.middleleftbutton.bind("<Button-1>", lambda event, obj=self.middleleftbutton, square=2: self.tictac(event,
                                                                                                                obj,
                                                                                                                square))

        self.rightleftbutton = Button(self.leftsidebuttons, width=10, height=5, bg="white")
        self.rightleftbutton.pack(side=LEFT)
        self.rightleftbutton.bind("<Button-1>", lambda event, obj=self.rightleftbutton, square=3: self.tictac(event,
                                                                                                              obj,
                                                                                                              square))

        #Mid buttons
        self.midbuttons = Frame(self.mymaster)
        self.midbuttons.pack()

        self.topmid = Button(self.midbuttons, width=10, height=5, bg="white")
        self.topmid.pack(side=LEFT)
        self.topmid.bind("<Button-1>", lambda event, obj=self.topmid, square=4: self.tictac(event, obj, square))

        self.midmid = Button(self.midbuttons, width=10, height=5, bg="white")
        self.midmid.pack(side=LEFT)
        self.midmid.bind("<Button-1>", lambda event, obj=self.midmid, square=5: self.tictac(event, obj, square))

        self.botmid = Button(self.midbuttons, width=10, height=5, bg="white")
        self.botmid.pack(side=LEFT)
        self.botmid.bind("<Button-1>", lambda event, obj=self.botmid, square=6: self.tictac(event, obj, square))

        #Rightside buttons
        self.right = Frame(self.mymaster)
        self.right.pack()

        self.topright = Button(self.right, width=10, height=5, bg="white")
        self.topright.pack(side=RIGHT)
        self.topright.bind("<Button-1>", lambda event, obj=self.topright, square=9: self.tictac(event, obj, square))

        self.midright = Button(self.right, width=10, height=5, bg="white")
        self.midright.pack(side=RIGHT)
        self.midright.bind("<Button-1>", lambda event, obj=self.midright, square=8: self.tictac(event, obj, square))

        self.botright = Button(self.right, width=10, height=5, bg="white")
        self.botright.pack(side=RIGHT)
        self.botright.bind("<Button-1>", lambda event, obj=self.botright, square=7: self.tictac(event, obj, square))

        #retry the game
        self.retry = Frame(self.mymaster)
        self.retry.pack()

        self.retryb = Button(self.retry, width=30, height=2, bg="red", text="Replay?",
                             command=self.retrygame)
        self.retryb.pack()

        self.endgame = 0
        self.turn = 0
        self.redsquares = []
        self.bluesquares = []

    def tictac(self, event, obj, square):
        if obj["background"] == "white" and self.endgame == 0:
            if self.turn == 0:
                obj["background"] = "red"
                self.turn = 1
                self.redsquares.append(square)
            else:
                obj['background'] = "blue"
                self.turn = 0
                self.bluesquares.append(square)
            print("Red", self.redsquares)
            print("Blue", self.bluesquares)
        if len(self.redsquares) >= 3 and self.endgame == 0:
            value = 0
            for i in range(len(self.redsquares)):
                value = value + self.redsquares[i]
            if value == 6 or value == 15 or (value == 18 and 4 not in self.redsquares) or value == 24 or \
                    (value == 12 and 8 not in self.redsquares) or value == 13 or value == 29:
                print("Red wins")
                self.endgame = 1
        if len(self.bluesquares) >= 3 and self.endgame == 0:
            value = 0
            for i in range(len(self.bluesquares)):
                value = value + self.bluesquares[i]
            if value == 6 or value == 15 or (value == 12 and 8 not in self.redsquares) or \
                    (value == 18 and 4 not in self.redsquares) or value == 24 or value == 13 or value == 29:
                print("blue wins")
                self.endgame = 1

    def retrygame(self):
        if self.endgame == 1 or len(self.redsquares) + len(self.bluesquares) == 9:
            self.redsquares = []
            self.bluesquares = []
            self.mymaster.destroy()
            main()


def main():
    root = Tk()
    TTT(root)
    root.mainloop()

main()





