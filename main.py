import tkinter


# creating calc frame
def iCalc(source, side):
    storeObj = tkinter.Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand=True, fill=tkinter.BOTH)

    return storeObj


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


if __name__ == '__main__':
    App().mainloop()
