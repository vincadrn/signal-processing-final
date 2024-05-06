from pathlib import Path
from tkinter import Canvas, Button, Label, PhotoImage, filedialog
import tkinter as tk

from webcam import WebcamManager


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"..\assets\takeVideoPage")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class TakeVideoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.save_path = ""

        self.filetypes = (
            ('AVI files', '*.avi'),
            ('MOV files', '*.mov'),
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
        image_1 = self.canvas.create_image(
            125.965087890625,
            64.42745971679688,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            584.067138671875,
            284.4524688720703,
            image=self.image_image_2
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            master=self,
            image=button_image_1,
            state=tk.DISABLED,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.turn_off_command(),
            relief="flat"
        )
        self.button_1.place(
            x=387.800048828125,
            y=411.0,
            width=207.0,
            height=30.0
        )

        button_image_hover_1 = PhotoImage(
            file=relative_to_assets("button_hover_1.png"))

        def button_1_hover(e):
            self.button_1.config(
                image=button_image_hover_1
            )
        def button_1_leave(e):
            self.button_1.config(
                image=button_image_1
            )

        self.button_1.bind('<Enter>', button_1_hover)
        self.button_1.bind('<Leave>', button_1_leave)


        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            master=self,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            state=tk.DISABLED,
            command=lambda: self.turn_on_command(),
            relief="flat"
        )
        self.button_2.place(
            x=600.800048828125,
            y=411.0,
            width=207.0,
            height=30.0
        )

        button_image_hover_2 = PhotoImage(
            file=relative_to_assets("button_hover_2.png"))

        def button_2_hover(e):
            self.button_2.config(
                image=button_image_hover_2
            )
        def button_2_leave(e):
            self.button_2.config(
                image=button_image_2
            )

        self.button_2.bind('<Enter>', button_2_hover)
        self.button_2.bind('<Leave>', button_2_leave)


        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            master=self,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_save_directory(),
            relief="flat"
        )
        self.button_3.place(
            x=480.800048828125,
            y=448.0,
            width=207.0,
            height=30.0
        )

        button_image_hover_3 = PhotoImage(
            file=relative_to_assets("button_hover_3.png"))

        def button_3_hover(e):
            self.button_3.config(
                image=button_image_hover_3
            )
        def button_3_leave(e):
            self.button_3.config(
                image=button_image_3
            )

        self.button_3.bind('<Enter>', button_3_hover)
        self.button_3.bind('<Leave>', button_3_leave)


        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            448.499755859375,
            85.39244079589844,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            344.800048828125,
            127.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(
            813.729248046875,
            524.6370239257812,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_6 = self.canvas.create_image(
            134.382568359375,
            524.6370239257812,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        image_7 = self.canvas.create_image(
            811.800048828125,
            88.37741088867188,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        image_8 = self.canvas.create_image(
            173.800048828125,
            468.0,
            image=self.image_image_8
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("image_9.png"))
        image_9 = self.canvas.create_image(
            93.800048828125,
            468.0,
            image=self.image_image_9
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            master=self,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("StartPage"),
            relief="flat"
        )
        button_4.place(
            x=0.199951171875,
            y=111.0,
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


        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            master=self,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("HowPage"),
            relief="flat"
        )
        button_5.place(
            x=0.199951171875,
            y=174.0,
            width=259.0,
            height=30.0
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
            command=lambda: controller.show_frame("CompressPage"),
            relief="flat"
        )
        button_6.place(
            x=0.199951171875,
            y=237.0,
            width=259.0,
            height=30.0
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


        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        button_7 = Button(
            master=self,
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("AboutPage"),
            relief="flat"
        )
        button_7.place(
            x=0.199951171875,
            y=300.0,
            width=259.0,
            height=30.0
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


        button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        button_8 = Button(
            master=self,
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("TakeVideoPage"),
            relief="flat"
        )
        button_8.place(
            x=0.199951171875,
            y=367.0,
            width=259.0,
            height=30.0
        )

        button_image_hover_8 = PhotoImage(
            file=relative_to_assets("button_hover_8.png"))

        def button_8_hover(e):
            button_8.config(
                image=button_image_hover_8
            )
        def button_8_leave(e):
            button_8.config(
                image=button_image_8
            )

        button_8.bind('<Enter>', button_8_hover)
        button_8.bind('<Leave>', button_8_leave)


        self.image_image_10 = PhotoImage(
            file=relative_to_assets("image_10.png"))
        image_10 = self.canvas.create_image(
            58.60009765625,
            382.0,
            image=self.image_image_10
        )

        self.image_image_11 = PhotoImage(
            file=relative_to_assets("image_11.png"))
        image_11 = self.canvas.create_image(
            59.60009765625,
            315.0,
            image=self.image_image_11
        )

        self.image_image_12 = PhotoImage(
            file=relative_to_assets("image_12.png"))
        image_12 = self.canvas.create_image(
            58.60009765625,
            252.0,
            image=self.image_image_12
        )

        self.image_image_13 = PhotoImage(
            file=relative_to_assets("image_13.png"))
        image_13 = self.canvas.create_image(
            59.60009765625,
            189.0,
            image=self.image_image_13
        )

        self.image_image_14 = PhotoImage(
            file=relative_to_assets("image_14.png"))
        image_14 = self.canvas.create_image(
            59.60009765625,
            126.0,
            image=self.image_image_14
        )

        # self.image_image_15 = PhotoImage(
        #     file=relative_to_assets("image_15.png"))
        # image_15 = self.canvas.create_image(
        #     585.800048828125,
        #     278.0,
        #     image=self.image_image_15
        # )
        self.cam_container = Label(
            master=self,
            text="Camera",
        )
        self.cam_container.place(
            x=365.800048828125,
            y=165.0,
            height=224,
            width=453,
            anchor="nw",
        )
    
    def turn_on_command(self):
        print("Camera turn on")
        self.webcam.start_capture()
        
    def turn_off_command(self):
        print("Camera turn off")
        self.webcam.stop_capture()
        
        # destroy webcam object
        self.webcam = None

    def open_save_directory(self):
        self.save_path = filedialog.asksaveasfilename(filetypes=self.filetypes, title="Input save directory")
        if self.save_path:
            self.button_2.config(state=tk.NORMAL)
            self.webcam = WebcamManager(camfeed_container=self.cam_container, start_button=self.button_2, stop_button=self.button_1, dest_path=self.save_path)

        print(self.save_path)