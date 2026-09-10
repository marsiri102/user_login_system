import tkinter as tk
from PIL import Image, ImageTk

from database import create_database
from login import show_login
from register import show_register


def main():
    create_database()

    root = tk.Tk()
    root.title("User Login System")

    # Window size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = int(screen_width * 0.5)
    window_height = int(screen_height * 0.5)

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Background image
    image = Image.open("lost-and-found-software.png")
    image = image.resize((window_width, window_height))

    background_image = ImageTk.PhotoImage(image)

    # Canvas
    canvas = tk.Canvas(
        root,
        width=window_width,
        height=window_height,
        highlightthickness=0
    )

    canvas.pack(fill="both", expand=True)

    # Put image on canvas
    canvas.create_image(
        0,
        0,
        image=background_image,
        anchor="nw"
    )

    # Keep image from disappearing
    canvas.image = background_image

    # Title directly on background
    canvas.create_text(
        window_width // 2,
        int(window_height * 0.40),
        text="User Login System",
        font=("Arial", 22, "bold"),
        fill="white"
    )

    # Login button
    login_button = tk.Button(
        root,
        text="Login",
        width=20,
        command=lambda: show_login(root)
    )

    canvas.create_window(
        window_width // 2,
        int(window_height * 0.50),
        window=login_button
    )

    # Register button
    register_button = tk.Button(
        root,
        text="Register",
        width=20,
        command=lambda: show_register(root)
    )

    canvas.create_window(
        window_width // 2,
        int(window_height * 0.60),
        window=register_button
    )

    root.mainloop()


if __name__ == "__main__":
    main()