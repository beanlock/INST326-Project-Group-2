import tkinter as tk

def main_canvas():
    root = tk.Tk()
    root.title("Main Page")

    frame = tk.Frame(
        root, 
        width=1920,
        height = 1080
        )

    canvas = tk.Canvas(
        frame,
        bg='white',
        width=1920,
        height=1080
        )
    canvas.pack()

    canvas.create_text(
        1920/2,
        1080/2,
        text="Welcome to Main"
    )

    root.mainloop()