from tkinter import Frame, Label

class MainFrame(Frame):
    def __init__(self, app_frames):
        super().__init__(app_frames.master)
        self.configure(bg='white')
        self.label = Label(self, text="Welcome to the Main Application Screen", bg='white')
        self.label.pack(expand=True)
