from tkinter import *

class Application(Frame):
    """A GUI applictaion with there buttons. """
    def __init__(self, master):
        """ Initialise the Frame """
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create button, Text and Entry widgets"""
        self.instruction = Label(self, text = "Enter the Password")
        self.instruction.grid(row = 0 , column = 0, columnspan = 2, sticky =W)

        self.password = Entry(self)
        self.password.grid(row = 1 , column = 1, sticky =W)

        self.button = Button(self, text="Submit", command = self.reveal)
        self.button.grid(row = 2 , column = 0, sticky =W)

        self.text = Text(self, width=35, height = 5, wrap =WORD)
        self.text.grid(row = 3 , column = 0, columnspan = 2, sticky =W)

    def reveal(self):
        """Desplay message based on the password type in"""
        content = self.password.get()

        if content == 'password':
            message = "You have Access to special modules......Now....."
        else:
            message = "Wrong Password.. Access Denied"

        self.text.delete(0.0, END)
        self.text.insert(0.0,message)

root = Tk()
root.title("Password")
root.geometry()
app = Application(root)

root.mainloop()
