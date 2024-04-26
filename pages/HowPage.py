from pathlib import Path
from tkinter import Canvas, Button, PhotoImage
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"..\assets\howPage")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class HowPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
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

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            master=self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("StartPage"),
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=148.0,
            width=259.0,
            height=30.0
        )

        self.button_image_hover_1 = PhotoImage(
            file=relative_to_assets("button_hover_1.png"))

        def button_1_hover(e):
            self.button_1.config(
                image=self.button_image_hover_1
            )
        def button_1_leave(e):
            self.button_1.config(
                image=self.button_image_1
            )

        self.button_1.bind('<Enter>', button_1_hover)
        self.button_1.bind('<Leave>', button_1_leave)


        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            master=self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("HowPage"),
            relief="flat"
        )
        self.button_2.place(
            x=0.0,
            y=211.0,
            width=259.0,
            height=30.0
        )

        self.button_image_hover_2 = PhotoImage(
            file=relative_to_assets("button_hover_2.png"))

        def button_2_hover(e):
            self.button_2.config(
                image=self.button_image_hover_2
            )
        def button_2_leave(e):
            self.button_2.config(
                image=self.button_image_2
            )

        self.button_2.bind('<Enter>', button_2_hover)
        self.button_2.bind('<Leave>', button_2_leave)


        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            master=self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 in howpage clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=0.0,
            y=274.0,
            width=259.0,
            height=30.0
        )

        self.button_image_hover_3 = PhotoImage(
            file=relative_to_assets("button_hover_3.png"))

        def button_3_hover(e):
            self.button_3.config(
                image=self.button_image_hover_3
            )
        def button_3_leave(e):
            self.button_3.config(
                image=self.button_image_3
            )

        self.button_3.bind('<Enter>', button_3_hover)
        self.button_3.bind('<Leave>', button_3_leave)


        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            master=self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked in how page"),
            relief="flat"
        )
        self.button_4.place(
            x=0.0,
            y=337.0,
            width=259.0,
            height=30.0
        )

        self.button_image_hover_4 = PhotoImage(
            file=relative_to_assets("button_hover_4.png"))

        def button_4_hover(e):
            self.button_4.config(
                image=self.button_image_hover_4
            )
        def button_4_leave(e):
            self.button_4.config(
                image=self.button_image_4
            )

        self.button_4.bind('<Enter>', button_4_hover)
        self.button_4.bind('<Leave>', button_4_leave)


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
            59.79998779296875,
            352.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            58.79998779296875,
            289.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            59.79998779296875,
            226.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            59.79998779296875,
            163.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            357.49969482421875,
            85.39244079589844,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(
            495.79998779296875,
            127.0,
            image=self.image_image_8
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("image_9.png"))
        self.image_9 = self.canvas.create_image(
            593.7999877929688,
            250.0,
            image=self.image_image_9
        )

        self.image_image_10 = PhotoImage(
            file=relative_to_assets("image_10.png"))
        self.image_10 = self.canvas.create_image(
            813.7293090820312,
            524.6370239257812,
            image=self.image_image_10
        )

        self.image_image_11 = PhotoImage(
            file=relative_to_assets("image_11.png"))
        self.image_11 = self.canvas.create_image(
            134.3824462890625,
            524.6370239257812,
            image=self.image_image_11
        )

        self.image_image_12 = PhotoImage(
            file=relative_to_assets("image_12.png"))
        self.image_12 = self.canvas.create_image(
            819.7999877929688,
            88.37741088867188,
            image=self.image_image_12
        )

        self.image_image_13 = PhotoImage(
            file=relative_to_assets("image_13.png"))
        self.image_13 = self.canvas.create_image(
            563.7999877929688,
            390.0,
            image=self.image_image_13
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            master=self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("StartPage"),
            relief="flat"
        )
        self.button_5.place(
            x=474.79998779296875,
            y=445.837158203125,
            width=178.20233154296875,
            height=43.42745590209961
        )

        self.button_image_hover_5 = PhotoImage(
            file=relative_to_assets("button_hover_5.png"))

        def button_5_hover(e):
            self.button_5.config(
                image=self.button_image_hover_5
            )
        def button_5_leave(e):
            self.button_5.config(
                image=self.button_image_5
            )

        self.button_5.bind('<Enter>', button_5_hover)
        self.button_5.bind('<Leave>', button_5_leave)


        self.image_image_14 = PhotoImage(
            file=relative_to_assets("image_14.png"))
        self.image_14 = self.canvas.create_image(
            173.79998779296875,
            468.0,
            image=self.image_image_14
        )

        self.image_image_15 = PhotoImage(
            file=relative_to_assets("image_15.png"))
        self.image_15 = self.canvas.create_image(
            93.79998779296875,
            468.0,
            image=self.image_image_15
        )