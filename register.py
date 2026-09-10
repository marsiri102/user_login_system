import tkinter as tk
from tkinter import messagebox
from users import register_user


def show_register(root):
    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.geometry("300x300")

    tk.Label(
        register_window,
        text="Create Account",
        font=("Arial", 18)
    ).pack(pady=15)

    tk.Label(
        register_window,
        text="Username"
    ).pack()

    username_entry = tk.Entry(register_window)
    username_entry.pack()

    tk.Label(
        register_window,
        text="Password"
    ).pack()

    password_entry = tk.Entry(
        register_window,
        show="*"
    )
    password_entry.pack()

    tk.Label(
        register_window,
        text="Confirm Password"
    ).pack()

    confirm_entry = tk.Entry(
        register_window,
        show="*"
    )
    confirm_entry.pack()

    def register():
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_entry.get()

        if username == "" or password == "":
            messagebox.showerror(
                "Error",
                "Please fill in all fields."
            )
            return

        if password != confirm_password:
            messagebox.showerror(
                "Error",
                "Passwords do not match."
            )
            return

        if register_user(username, password):
            messagebox.showinfo(
                "Success",
                "Account created!"
            )
            register_window.destroy()

        else:
            messagebox.showerror(
                "Error",
                "Username already exists."
            )

    tk.Button(
        register_window,
        text="Register",
        command=register
    ).pack(pady=20)