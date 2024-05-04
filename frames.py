from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
import login
import main
import review
from review import *

class AppFrames:
    def __init__(self, master):
        self.master = master
        self.master.state('zoomed')
        self.current_frame = None
        self.users = UserDB()
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
    
    def register(self, username, password):
        success = self.users.register_user(username,password)
        return success
    

if __name__ == "__main__":
    root = Tk()
    app = AppFrames(root)
    root.mainloop()