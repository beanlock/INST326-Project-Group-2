from tkinter import Frame, Label, Canvas, Entry, PhotoImage
from pathlib import Path

class MainFrame(Frame):
    def __init__(self, app_frames):
        super().__init__(app_frames.master)
        self.configure(bg='white')
        self.setup_ui()
    
    def setup_ui(self):
        ASSETS_PATH = Path(__file__).parent / Path("assets/main")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.canvas = Canvas(
            self,
            bg="#87AF86",
            height=1080,
            width=1920,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.pack(fill='both', expand=True)

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            960.0,
            562.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            master=self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=680.0,
            y=531.0,
            width=560.0,
            height=60.0
        )

        self.entry_1.insert(0,"Type to start your ReView journey")

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            960.0,
            286.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            1920.0,
            120.0,
            fill="#677F5B",
            outline=""
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            1856.0,
            60.0,
            image=self.image_image_2
        )     

