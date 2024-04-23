from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
import login
import main
from review import *

class AppFrames:
    def __init__(self, master):
        self.master = master
        self.current_frame = None
        self.users = {"testudo":"inst"}
        self.switch_frame(login.LoginFrame)
    
    def verify_user(self, username, password):
        return self.users.get(username) == password
    
    def switch_frame(self, frame_class):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.pack(
            fill='both',
            expand=True
        )

if __name__ == "__main__":
    root = Tk()
    app = AppFrames(root)
    root.mainloop()