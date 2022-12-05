import tkinter


# creating calc frame
def iCalc(source, side):
    storeObj = tkinter.Frame()


class App(tkinter.Frame):
    def __init__(self):
        tkinter.Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=True, fill=tkinter.BOTH)
        self.master.title('Calculator')


if __name__ == '__main__':
    App().mainloop()
