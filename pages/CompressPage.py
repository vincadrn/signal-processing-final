from pathlib import Path
from tkinter import Canvas, Button, OptionMenu, PhotoImage, StringVar, filedialog
import tkinter as tk
import sys

sys.path.append("..")

from transcode import Transcoder


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"..\assets\compressPage")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class CompressPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.transcoder = Transcoder()
        self.save_path = ""
        self.video_path = ""

        self.controller = controller
        self.filetypes = (
            ('AVI files', '*.avi'),
            ('MP4 files', '*.mp4'),
            ('All files', '*.*')
        )

        # Dropdown menu options 
        self.quality_options = [ 
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
        ]

        self.output_format_options = [
            "avi",
            "mov",
            "mkv"
        ]

        # datatype of menu text 
        self.clicked_quality = StringVar()
        self.clicked_output_format =  StringVar()
        
        # initial menu text 
        self.clicked_quality.set( "5" )
        self.clicked_output_format.set( "avi" ) 

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

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            584.0672607421875,
            284.4499969482422,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            380.499755859375,
            85.39244079589844,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            390.800048828125,
            127.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            583.800048828125,
            388.0,
            image=self.image_image_5
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

        self.dropdown_quality = OptionMenu(
            self, 
            self.clicked_quality, 
            *self.quality_options 
            ) 

        self.dropdown_quality.place(
            x=420.800048828125,
            y=417.0,
            width=60.0,
            height=43.0
        )
        
        self.dropdown_output_format = OptionMenu(
            self, 
            self.clicked_output_format, 
            *self.output_format_options 
            ) 

        self.dropdown_output_format.place(
            x=680.800048828125,
            y=417.0,
            width=60.0,
            height=43.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            master=self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.transcode_start(),
            relief="flat"
        )
        self.button_1.place(
            x=528.800048828125,
            y=417.0,
            width=111.0,
            height=43.0
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
            command=lambda: self.open_save_directory(),
            relief="flat"
        )
        self.button_2.place(
            x=480.800048828125,
            y=182.0,
            width=207.0,
            height=43.0
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

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            master=self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.input_video_path(),
            relief="flat"
        )
        self.button_3.place(
            x=529.800048828125,
            y=250.0,
            width=109.0,
            height=109.0
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
            command=lambda: controller.show_frame("StartPage"),
            relief="flat"
        )
        self.button_4.place(
            x=0.199951171875,
            y=111.0,
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


        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            master=self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("HowPage"),
            relief="flat"
        )
        self.button_5.place(
            x=0.199951171875,
            y=174.0,
            width=259.0,
            height=30.0
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


        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            master=self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("CompressPage"),
            relief="flat"
        )
        self.button_6.place(
            x=0.199951171875,
            y=237.0,
            width=259.0,
            height=30.0
        )

        self.button_image_hover_6 = PhotoImage(
            file=relative_to_assets("button_hover_6.png"))

        def button_6_hover(e):
            self.button_6.config(
                image=self.button_image_hover_6
            )
        def button_6_leave(e):
            self.button_6.config(
                image=self.button_image_6
            )

        self.button_6.bind('<Enter>', button_6_hover)
        self.button_6.bind('<Leave>', button_6_leave)


        self.button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.button_7 = Button(
            master=self,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("AboutPage"),
            relief="flat"
        )
        self.button_7.place(
            x=0.199951171875,
            y=367.0,
            width=259.0,
            height=30.0
        )

        self.button_image_hover_7 = PhotoImage(
            file=relative_to_assets("button_hover_7.png"))

        def button_7_hover(e):
            self.button_7.config(
                image=self.button_image_hover_7
            )
        def button_7_leave(e):
            self.button_7.config(
                image=self.button_image_7
            )

        self.button_7.bind('<Enter>', button_7_hover)
        self.button_7.bind('<Leave>', button_7_leave)


        self.button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.button_8 = Button(
            master=self,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("TakeVideoPage"),
            relief="flat"
        )
        self.button_8.place(
            x=0.199951171875,
            y=300.0,
            width=259.0,
            height=30.0
        )

        self.button_image_hover_8 = PhotoImage(
            file=relative_to_assets("button_hover_8.png"))

        def button_8_hover(e):
            self.button_8.config(
                image=self.button_image_hover_8
            )
        def button_8_leave(e):
            self.button_8.config(
                image=self.button_image_8
            )

        self.button_8.bind('<Enter>', button_8_hover)
        self.button_8.bind('<Leave>', button_8_leave)
        
        self.button_analyze_image = PhotoImage(
            file=relative_to_assets("Button_Analyze.png"))
        self.button_analyze = Button(
            master=self,
            image=self.button_analyze_image,
            state=tk.DISABLED,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.inputStartAnalyze(),
            relief="flat"
        )
        self.button_analyze.place(
            x=280.199951171875,
            y=280.0,
            width=217.12,
            height=44.0
        )

        self.Button_Analyze_Image_Hover = PhotoImage(
            file=relative_to_assets("Button_Analyze_hover.png"))

        def button_analyze_hover(e):
            self.button_analyze.config(
                image=self.Button_Analyze_Image_Hover
            )
        def button_analyze_leave(e):
            self.button_analyze.config(
                image=self.button_analyze_image
            )

        self.button_analyze.bind('<Enter>', button_analyze_hover)
        self.button_analyze.bind('<Leave>', button_analyze_leave)


        self.image_image_17 = PhotoImage(
            file=relative_to_assets("image_17.png"))
        self.image_17 = self.canvas.create_image(
            58.60009765625,
            382.0,
            image=self.image_image_17
        )

        self.image_image_18 = PhotoImage(
            file=relative_to_assets("image_18.png"))
        self.image_18 = self.canvas.create_image(
            59.60009765625,
            315.0,
            image=self.image_image_18
        )

        self.image_image_19 = PhotoImage(
            file=relative_to_assets("image_19.png"))
        self.image_19 = self.canvas.create_image(
            58.60009765625,
            252.0,
            image=self.image_image_19
        )

        self.image_image_20 = PhotoImage(
            file=relative_to_assets("image_20.png"))
        self.image_20 = self.canvas.create_image(
            59.60009765625,
            189.0,
            image=self.image_image_20
        )

        self.image_image_21 = PhotoImage(
            file=relative_to_assets("image_21.png"))
        self.image_21 = self.canvas.create_image(
            59.60009765625,
            126.0,
            image=self.image_image_21
        )
    
    def open_save_directory(self):
        self.save_path = filedialog.asksaveasfilename(filetypes=self.filetypes, title="Input save directory")

        if self.save_path == "" :
            self.image_image_10 = PhotoImage(
                file=relative_to_assets("image_10.png"))
            self.image_10 = self.canvas.create_image(
                580.800048828125,
                170.0,
                image=self.image_image_10
            )

            try:
                self.canvas.delete(self.image_11)

            except:
                None
        
        else :
            self.image_image_11 = PhotoImage(
                file=relative_to_assets("image_11.png"))
            self.image_11 = self.canvas.create_image(
                580.800048828125,
                170.0,
                image=self.image_image_11
            )

            try:
                self.canvas.delete(self.image_10)

            except:
                None

        print(self.save_path)

    def input_video_path(self):
        self.video_path = filedialog.askopenfilename(filetypes=self.filetypes, title="Input your video")

        if self.video_path == "" :
            self.image_image_8 = PhotoImage(
                file=relative_to_assets("image_8.png"))
            self.image_8 = self.canvas.create_image(
                719.800048828125,
                305.0,
                image=self.image_image_8
            )
            
            try:
                self.canvas.delete(self.image_9)

            except:
                None

        else:
            self.image_image_9 = PhotoImage(
                file=relative_to_assets("image_9.png"))
            self.image_9 = self.canvas.create_image(
                688.800048828125,
                305.0,
                image=self.image_image_9
            )

            try:
                self.canvas.delete(self.image_8)

            except:
                None

        print(self.video_path)

    def transcode_start(self):
        success = self.transcoder.transcode(self.save_path, self.video_path, dest_container=self.clicked_output_format.get(), quality=int(self.clicked_quality.get()))

        print(self.clicked_quality.get())

        if success:
            self.image_image_7 = PhotoImage(
                file=relative_to_assets("image_7.png"))
            self.image_7 = self.canvas.create_image(
                583.800048828125,
                472.0,
                image=self.image_image_7
            )
            self.button_analyze.config(state=tk.ACTIVE)

        else:
            self.image_image_6 = PhotoImage(
                file=relative_to_assets("image_6.png"))
            self.image_6 = self.canvas.create_image(
                580.800048828125,
                472.0,
                image=self.image_image_6
            )

        print(self.video_path)

    def inputStartAnalyze(self):
        self.analyze_path = filedialog.asksaveasfilename(filetypes=self.filetypes, title="Input analyze directory")

        if self.analyze_path == "" :
            self.image_failed_prompt = PhotoImage(
                file=relative_to_assets("PromptFailedAnalysis.png"))
            self.failed_prompt = self.canvas.create_image(
                380.800048828125,
                340.0,
                image=self.image_failed_prompt
            )

            try:
                self.canvas.delete(self.success_prompt)

            except:
                None
        
        else :
            self.image_success_prompt = PhotoImage(
                file=relative_to_assets("PromptSuccessAnalysis.png"))
            
            self.startAnalyze() # Masukkin process framenya disini

            self.success_prompt = self.canvas.create_image(
                380.800048828125,
                340.0,
                image=self.image_success_prompt
            )

            try:
                self.canvas.delete(self.failed_prompt)

            except:
                None

        print(self.save_path)

    def startAnalyze(self):
        None # Masukkin disini processnya