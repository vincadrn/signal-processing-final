from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, filedialog
import tkinter as tk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"..\assets\compressPage")
SAVE_PATH = ""
VIDEO_PATH = ""


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class CompressPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.filetypes = (
            ('MP4 files', '*.mp4'),
            ('All files', '*.*')
        )

        self.canvas = Canvas(
            self,
            bg = "#060B24",
            height = 560,
            width = 950,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            125.9649658203125,
            64.42745971679688,
            image=self.image_image_1
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            master=self,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("StartPage"),
            relief="flat"
        )
        button_1.place(
            x=0.0,
            y=148.0,
            width=259.0,
            height=30.0
        )

        button_image_hover_1 = PhotoImage(
            file=relative_to_assets("button_hover_1.png"))

        def button_1_hover(e):
            button_1.config(
                image=button_image_hover_1
            )
        def button_1_leave(e):
            button_1.config(
                image=button_image_1
            )

        button_1.bind('<Enter>', button_1_hover)
        button_1.bind('<Leave>', button_1_leave)


        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            master=self,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("HowPage"),
            relief="flat"
        )
        button_2.place(
            x=0.0,
            y=211.0,
            width=259.0,
            height=30.0
        )

        button_image_hover_2 = PhotoImage(
            file=relative_to_assets("button_hover_2.png"))

        def button_2_hover(e):
            button_2.config(
                image=button_image_hover_2
            )
        def button_2_leave(e):
            button_2.config(
                image=button_image_2
            )

        button_2.bind('<Enter>', button_2_hover)
        button_2.bind('<Leave>', button_2_leave)


        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            master=self,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("CompressPage"),
            relief="flat"
        )
        button_3.place(
            x=0.0,
            y=274.0,
            width=259.0,
            height=30.0
        )

        button_image_hover_3 = PhotoImage(
            file=relative_to_assets("button_hover_3.png"))

        def button_3_hover(e):
            button_3.config(
                image=button_image_hover_3
            )
        def button_3_leave(e):
            button_3.config(
                image=button_image_3
            )

        button_3.bind('<Enter>', button_3_hover)
        button_3.bind('<Leave>', button_3_leave)


        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            master=self,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("AboutPage"),
            relief="flat"
        )
        button_4.place(
            x=0.0,
            y=337.0,
            width=259.0,
            height=30.0
        )

        button_image_hover_4 = PhotoImage(
            file=relative_to_assets("button_hover_4.png"))

        def button_4_hover(e):
            button_4.config(
                image=button_image_hover_4
            )
        def button_4_leave(e):
            button_4.config(
                image=button_image_4
            )

        button_4.bind('<Enter>', button_4_hover)
        button_4.bind('<Leave>', button_4_leave)


        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            584.0672607421875,
            284.4524688720703,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            59.800048828125,
            352.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            58.800048828125,
            289.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            59.800048828125,
            226.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            59.800048828125,
            163.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            380.499755859375,
            85.39244079589844,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(
            390.800048828125,
            127.0,
            image=self.image_image_8
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("image_9.png"))
        self.image_9 = self.canvas.create_image(
            583.800048828125,
            388.0,
            image=self.image_image_9
        )

        self.image_image_12 = PhotoImage(
            file=relative_to_assets("image_12.png"))
        self.image_12 = self.canvas.create_image(
            813.729248046875,
            524.6370239257812,
            image=self.image_image_12
        )

        self.image_image_13 = PhotoImage(
            file=relative_to_assets("image_13.png"))
        self.image_13 = self.canvas.create_image(
            134.3824462890625,
            524.6370239257812,
            image=self.image_image_13
        )

        self.image_image_14 = PhotoImage(
            file=relative_to_assets("image_14.png"))
        self.image_14 = self.canvas.create_image(
            816.800048828125,
            88.37741088867188,
            image=self.image_image_14
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            master=self,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: startCompress(),
            relief="flat"
        )
        button_5.place(
            x=528.800048828125,
            y=417.0,
            width=111.0,
            height=43.0
        )

        button_image_hover_5 = PhotoImage(
            file=relative_to_assets("button_hover_5.png"))

        def button_5_hover(e):
            button_5.config(
                image=button_image_hover_5
            )
        def button_5_leave(e):
            button_5.config(
                image=button_image_5
            )

        button_5.bind('<Enter>', button_5_hover)
        button_5.bind('<Leave>', button_5_leave)


        button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        button_6 = Button(
            master=self,
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_save_directory(),
            relief="flat"
        )
        button_6.place(
            x=480.800048828125,
            y=182.0,
            width=207.0,
            height=43.0
        )

        button_image_hover_6 = PhotoImage(
            file=relative_to_assets("button_hover_6.png"))

        def button_6_hover(e):
            button_6.config(
                image=button_image_hover_6
            )
        def button_6_leave(e):
            button_6.config(
                image=button_image_6
            )

        button_6.bind('<Enter>', button_6_hover)
        button_6.bind('<Leave>', button_6_leave)


        self.image_image_15 = PhotoImage(
            file=relative_to_assets("image_15.png"))
        self.image_15 = self.canvas.create_image(
            173.800048828125,
            468.0,
            image=self.image_image_15
        )

        self.image_image_16 = PhotoImage(
            file=relative_to_assets("image_16.png"))
        self.image_16 = self.canvas.create_image(
            93.800048828125,
            468.0,
            image=self.image_image_16
        )

        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        button_7 = Button(
            master=self,
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.input_video_path()),
            relief="flat"
        )
        button_7.place(
            x=529.800048828125,
            y=250.0,
            width=109.0,
            height=109.0
        )

        button_image_hover_7 = PhotoImage(
            file=relative_to_assets("button_hover_7.png"))

        def button_7_hover(e):
            button_7.config(
                image=button_image_hover_7
            )
        def button_7_leave(e):
            button_7.config(
                image=button_image_7
            )

        button_7.bind('<Enter>', button_7_hover)
        button_7.bind('<Leave>', button_7_leave)
    
    def open_save_directory(self):
        SAVE_PATH = filedialog.asksaveasfilename(filetypes=self.filetypes, title="Input save directory")

        if SAVE_PATH == "" :
            self.image_image_11 = PhotoImage(
                file=relative_to_assets("image_10.png"))
            self.image_11 = self.canvas.create_image(
                583.800048828125,
                170.0,
                image=self.image_image_11
            )
        
        else :
            self.image_image_11 = PhotoImage(
                file=relative_to_assets("image_11.png"))
            self.image_11 = self.canvas.create_image(
                583.800048828125,
                170.0,
                image=self.image_image_11
            )

        print(SAVE_PATH)

    def input_video_path(self):
        VIDEO_PATH = filedialog.askopenfilename(filetypes=self.filetypes, title="Input your video")
        if VIDEO_PATH == "" :
            self.image_image_10 = PhotoImage(
                file=relative_to_assets("image_10.png"))
            self.image_10 = self.canvas.create_image(
                580.800048828125,
                472.0,
                image=self.image_image_10
            )

        else:
            self.image_image_10 = PhotoImage(
                file=relative_to_assets("image_11.png"))
            self.image_10 = self.canvas.create_image(
                580.800048828125,
                472.0,
                image=self.image_image_10
            )

        print(VIDEO_PATH)