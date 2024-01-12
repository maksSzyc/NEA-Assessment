import sqlite3
from tkinter import *
from tkinter import messagebox
class SQLmanagement:
    def __init__(self, password_input, username_input, setting):
        # create user_info table
        self.password = password_input
        self.username = username_input
        self.conn = sqlite3.connect("login.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS User_info (
                                username VARCHAR(20),
                                password VARCHAR(20),
                                User_ID INTEGER PRIMARY KEY)""")
        self.conn.commit()

        # make sure login or register is happening
        if setting == "login":
            self.login_user()
        elif setting == "register":
            self.register_user()

    # check for existing usernames and insert new ones into table
    def register_user(self):
        self.cursor.execute("SELECT * FROM User_info WHERE username=?", (self.username,))
        existing_user = self.cursor.fetchone()

        if existing_user:
            messagebox.showerror("Registration Error", "Username already exists!")
        else:
            self.cursor.execute("INSERT INTO User_info (username, password) VALUES (?, ?)", (self.username, self.password))
            self.conn.commit()
            messagebox.showinfo("Registration Successful", "Registration successful!")

    # check for existing username and password combinations
    def login_user(self):
        self.cursor.execute("SELECT * FROM User_info WHERE username=? AND password=?", (self.username, self.password))
        logged_user = self.cursor.fetchone()

        if logged_user:
            return True
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

    # close database connection
    def close_connection(self):
        self.conn.close()