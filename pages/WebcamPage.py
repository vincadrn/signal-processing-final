from tkinter import Canvas, Button, PhotoImage, filedialog, Text, Label
import tkinter as tk
import sys

sys.path.append("..")

from webcam import WebcamManager


class WebcamPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.save_path = ""

        self.cam_container = Label(
            master=self,
            text="label",
        )
        self.cam_container.place(
            x=0,
            y=0,
            height=144,
            width=176,
            anchor="nw",
        )

        self.save_prompt = Button(
            master=self,
            text="Save to ...",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_save_directory(),
            relief="flat"
        )
        self.save_prompt.place(
            x=100,
            y=200,
            width=207.0,
            height=43.0
        )

        self.turn_on_button = Button(
            master=self,
            text="Turn on and record",
            state=tk.DISABLED,
            borderwidth=0,
            highlightthickness=0,
            command=self.turn_on_command,
            relief="flat"
        )
        self.turn_on_button.place(
            x=300,
            y=100,
            width=111.0,
            height=43.0
        )

        self.turn_off_button = Button(
            master=self,
            text="Turn off and save",
            state=tk.DISABLED,
            borderwidth=0,
            highlightthickness=0,
            command=self.turn_off_command,
            relief="flat"
        )
        self.turn_off_button.place(
            x=500,
            y=100,
            width=111.0,
            height=43.0
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
        self.save_path = filedialog.asksaveasfilename(title="Input save directory")
        if self.save_path:
            self.turn_on_button.config(state=tk.NORMAL)
            self.webcam = WebcamManager(self.cam_container, self.turn_on_button, self.turn_off_button, self.save_path)

        print(self.save_path)
