import tkinter


# creating calc frame
def iCalc(source, side):
    storeObj = tkinter.Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand=True, fill=tkinter.BOTH)

    return storeObj


# creating button object
def button(source, side, text, command=None):
    storeObj = tkinter.Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=True, fill=tkinter.BOTH)

    return storeObj


class App(tkinter.Frame):
    def __init__(self):
        tkinter.Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=True, fill=tkinter.BOTH)
        self.master.title('Calculator')

        # adding display widget to frame
        display = tkinter.StringVar()
        tkinter.Entry(self, relief=tkinter.RIDGE, textvariable=display,
                      justify='right', bd=30, bg='powder blue').pack(side=tkinter.TOP,
                                                                     expand=tkinter.YES,
                                                                     fill=tkinter.BOTH)
        for clearButton in (["C"]):
            erase = iCalc(self, tkinter.TOP)
            for ichar in clearButton:
                button(erase, tkinter.LEFT, ichar,
                       lambda storeObj=display, q=ichar: storeObj.set(''))

        for numButton in ("789/", '456*', '123-', '0.+'):
            functionNum = iCalc(self, tkinter.TOP)
            for iEquals in numButton:
                button(functionNum, tkinter.LEFT, iEquals, lambda
                    storeObj=display, q=iEquals: storeObj
                       .set(storeObj.get() + q))


if __name__ == '__main__':
    App().mainloop()
