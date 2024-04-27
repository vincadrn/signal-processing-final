from pathlib import Path
from tkinter import Canvas, Button, PhotoImage
import tkinter as tk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"..\assets\aboutPage")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class AboutPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        canvas = Canvas(
            self,
            bg = "#060B24",
            height = 560,
            width = 950,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = canvas.create_image(
            125.965087890625,
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
        self.image_2 = canvas.create_image(
            584.067138671875,
            284.4524688720703,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = canvas.create_image(
            59.800048828125,
            352.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = canvas.create_image(
            58.800048828125,
            289.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_5 = canvas.create_image(
            59.800048828125,
            226.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.image_6 = canvas.create_image(
            59.800048828125,
            163.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        self.image_7 = canvas.create_image(
            344.499755859375,
            85.39244079589844,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        self.image_8 = canvas.create_image(
            414.800048828125,
            127.0,
            image=self.image_image_8
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("image_9.png"))
        self.image_9 = canvas.create_image(
            564.800048828125,
            271.0,
            image=self.image_image_9
        )

        self.image_image_10 = PhotoImage(
            file=relative_to_assets("image_10.png"))
        self.image_10 = canvas.create_image(
            813.729248046875,
            524.6370239257812,
            image=self.image_image_10
        )

        self.image_image_11 = PhotoImage(
            file=relative_to_assets("image_11.png"))
        self.image_11 = canvas.create_image(
            134.382568359375,
            524.6370239257812,
            image=self.image_image_11
        )

        self.image_image_12 = PhotoImage(
            file=relative_to_assets("image_12.png"))
        self.image_12 = canvas.create_image(
            808.800048828125,
            88.37741088867188,
            image=self.image_image_12
        )

        self.image_image_13 = PhotoImage(
            file=relative_to_assets("image_13.png"))
        self.image_13 = canvas.create_image(
            173.800048828125,
            468.0,
            image=self.image_image_13
        )

        self.image_image_14 = PhotoImage(
            file=relative_to_assets("image_14.png"))
        self.image_14 = canvas.create_image(
            93.800048828125,
            468.0,
            image=self.image_image_14
        )