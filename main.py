from tkinter import *
from tkinter import messagebox
from Game import *
from SQLcode import SQLmanagement
from os import path
# create main menu window
class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("WELCOME!")
        self.master.config(bg = "blue")
        # set file path and create image
        self.picture = PhotoImage(file = "Images\\sasad.gif")
        self.logo = Label(self.master, image = self.picture)
        self.logo.grid(row = 0, column = 3, rowspan = 2)
        # create login button
        self.login_button = Button(self.master, text = "Log In", bg = "blue", fg = "white", width = 20, command = self.login)
        self.login_button.grid(row=0, column=0)
        #create register button
        self.register_button = Button(self.master, text="Register", bg="blue", fg="white", width = 20, command = self.register)
        self.register_button.grid(row = 1, column = 0)

    # call login and register classes
    def login(self):
        root = Tk()
        Log(root)
        root.mainloop()

    def register(self):
        root = Tk()
        Reg(root)
        root.mainloop()

    def load_data(self):
        self.game_folder = path.dirname(__file__)
        self.filename = path.join(self.game_folder, "")



# create login window
class Window:
    def __init__(self, master):
        self.master = master
        master.geometry("300x100")
        master.config(bg = "blue")
        # create username text
        self.username = Label(self.master, text = "Username:", bg = "blue", fg = "white")
        self.username.grid(row = 0, column = 0)
        # create username entry box
        self.userEntry = Entry(self.master, width = 20)
        self.userEntry.grid(row = 0, column = 1)
        # create password text
        self.password = Label(self.master, text = "Password:", bg = "blue", fg = "white")
        self.password.grid(row = 1, column = 0)
        # create password entry box
        self.passEntry = Entry(self.master, width = 20)
        self.passEntry.grid(row = 1, column = 1)

# create register window
class Log(Window):
    def __init__(self, master):
        super().__init__(master)
        # create login button
        self.buttonlog = Button(self.master, text = "Log In", command = self.login_function)
        self.buttonlog.grid(row = 2, column = 0, columnspan = 2)

    # interact with SQL class and open menu window
    def login_function(self):
        username = self.userEntry.get()
        password = self.passEntry.get()
        login_db = SQLmanagement(username, password, "login")
        if login_db.login_user():
            root = Toplevel()
            GameMenu(root)
            root.mainloop()
        login_db.close_connection()
class Reg(Window):
    def __init__(self, master):
        super().__init__(master)
        # create register button
        self.buttonlog = Button(self.master, text = "Register", command = self.register_function)
        self.buttonlog.grid(row = 2, column = 0, columnspan = 2)

    # interact with SQL class and destroy window
    def register_function(self):
        username = self.userEntry.get()
        password = self.passEntry.get()
        login_db = SQLmanagement(username, password, "register")
        self.master.destroy()
        login_db.close_connection()

class GameMenu:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x600")
        # set file path and create image
        self.picture = PhotoImage(file = "Images\\sala.png")
        self.logo = Label(self.master, image = self.picture)
        self.logo.grid(row = 0, column = 3, rowspan = 2)
        # create level button
        self.stalking = Button(self.master, text = "The Stalking", command = self.stalk)
        self.stalking.grid(row = 0, column = 0)
        # create level button
        self.haunting = Button(self.master, text = "The Haunting", command = self.haunt)
        self.haunting.grid(row = 1, column = 0)
        # create level button
        self.questions = Button(self.master, text = "???", command = self.question)
        self.questions.grid(row = 2, column = 0)

    # call main game class
    def stalk(self):
        Main()
    def haunt(self):
        pass
    def question(self):
        pass
# run first window
def main():
    root = Tk()
    Menu(root)
    root.mainloop()

main()