import tkinter as tk
from tkinter import messagebox
from users import login_user
from dashboard import open_dashboard


def show_login(root):
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry("300x250")

    tk.Label(
        login_window,
        text="Login",
        font=("Arial", 18)
    ).pack(pady=15)

    tk.Label(
        login_window,
        text="Username"
    ).pack()

    username_entry = tk.Entry(login_window)
    username_entry.pack()

    tk.Label(
        login_window,
        text="Password"
    ).pack()

    password_entry = tk.Entry(
        login_window,
        show="*"
    )
    password_entry.pack()

    def login():
        username = username_entry.get()
        password = password_entry.get()

        if login_user(username, password):
            messagebox.showinfo(
                "Success",
                "Login successful!"
            )

            login_window.destroy()
            open_dashboard(root, username)

        else:
            messagebox.showerror(
                "Error",
                "Invalid username or password."
            )

    tk.Button(
        login_window,
        text="Login",
        command=login
    ).pack(pady=20)