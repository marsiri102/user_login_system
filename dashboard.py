import tkinter as tk
from tkinter import messagebox


def open_dashboard(root, username):
    dashboard = tk.Toplevel(root)
    dashboard.title("Dashboard")
    dashboard.geometry("400x300")

    tk.Label(
        dashboard,
        text=f"Welcome, {username}!",
        font=("Arial", 20)
    ).pack(pady=50)

    def logout():
        dashboard.destroy()

        messagebox.showinfo(
            "Logout",
            "You have been logged out."
        )

    tk.Button(
        dashboard,
        text="Logout",
        command=logout
    ).pack()