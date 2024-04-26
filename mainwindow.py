from pathlib import Path
import tkinter as tk
from tkinter import Frame, Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("Video Compressor App")
window.iconbitmap("")
window.geometry("950x560")
window.configure(bg = "#060B24")

class MainWindow:

    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        canvas = Canvas(
            master,
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
            125.96499633789062,
            64.42745971679688,
            image=self.image_image_1
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
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
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
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
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
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
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
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
            584.0672607421875,
            284.4524688720703,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = canvas.create_image(
            59.79998779296875,
            352.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = canvas.create_image(
            58.79998779296875,
            289.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_5 = canvas.create_image(
            59.79998779296875,
            226.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.image_6 = canvas.create_image(
            59.79998779296875,
            163.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        self.image_7 = canvas.create_image(
            340.49969482421875,
            85.39244079589844,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        self.image_8 = canvas.create_image(
            585.3896484375,
            193.2123260498047,
            image=self.image_image_8
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("image_9.png"))
        self.image_9 = canvas.create_image(
            585.32958984375,
            232.13230895996094,
            image=self.image_image_9
        )

        self.image_image_10 = PhotoImage(
            file=relative_to_assets("image_10.png"))
        self.image_10 = canvas.create_image(
            813.7293090820312,
            524.6370239257812,
            image=self.image_image_10
        )

        self.image_image_11 = PhotoImage(
            file=relative_to_assets("image_11.png"))
        self.image_11 = canvas.create_image(
            134.3824462890625,
            524.6370239257812,
            image=self.image_image_11
        )

        self.image_image_12 = PhotoImage(
            file=relative_to_assets("image_12.png"))
        self.image_12 = canvas.create_image(
            806.689208984375,
            88.37741088867188,
            image=self.image_image_12
        )

        self.image_image_13 = PhotoImage(
            file=relative_to_assets("image_13.png"))
        self.image_13 = canvas.create_image(
            467.79998779296875,
            328.0,
            image=self.image_image_13
        )

        self.image_image_14 = PhotoImage(
            file=relative_to_assets("image_14.png"))
        self.image_14 = canvas.create_image(
            684.7999877929688,
            327.0,
            image=self.image_image_14
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        button_5.place(
            x=381.86212158203125,
            y=396.837158203125,
            width=178.20233154296875,
            height=43.42745590209961
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
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        button_6.place(
            x=596.0044555664062,
            y=396.837158203125,
            width=178.20233154296875,
            height=43.42745590209961
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
        self.image_15 = canvas.create_image(
            173.79998779296875,
            468.0,
            image=self.image_image_15
        )

        self.image_image_16 = PhotoImage(
            file=relative_to_assets("image_16.png"))
        self.image_16 = canvas.create_image(
            93.79998779296875,
            468.0,
            image=self.image_image_16
        )

e = MainWindow(window)
window.resizable(False, False)
window.mainloop()
