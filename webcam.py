import imageio.v3 as iio
import imageio
import threading
from PIL import Image, ImageTk
import numpy as np
from tkinter import Label, Button
import tkinter as tk
import tkinter.messagebox as messagebox
from enum import Enum
from typing import Literal


class Size(Enum):
    QCIF = (176, 144)
    CIF = (352, 288)
    _4CIF = (704, 576)


class WebcamManager:
    def __init__(
        self,
        camfeed_container: Label,
        start_button: Button,
        stop_button: Button,
        dest_path: str,
        codec: Literal["h261", "h263"] = "h263",
        output_size: tuple[int, int] = Size._4CIF.value,
    ):
        self.video_label = camfeed_container
        self.video_label.pack()

        self.is_capturing = False
        self.stop_thread = False

        self.start_button = start_button
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = stop_button
        self.stop_button.pack(side=tk.LEFT)

        self._dest_path = dest_path
        self._codec = codec
        self._output_size = output_size

    def start_capture(self):
        if not self.is_capturing:
            self.is_capturing = True
            self.stop_thread = False
            self.capture_thread = threading.Thread(target=self._capture_video, daemon=True)  # Create a new thread object
            self.capture_thread.start()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
        else:
            messagebox.showinfo("Info", "Already capturing!")

    def stop_capture(self):
        self.is_capturing = False
        self.stop_thread = True
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
    
    def _capture_video(self):
        try:
            video_reader = imageio.get_reader('<video0>')
            self.video_writer = iio.imopen(self._dest_path, "w", plugin="pyav")
            # the fps should not be hardcoded
            # however if the fps is matched to the input,
            # the playback would be way too fast
            self.video_writer.init_video_stream(self._codec, fps=12)
            for frame in video_reader:
                if self.is_capturing:
                    img_frame = Image.fromarray(frame)
                    self.video_writer.write_frame(np.array(img_frame.resize(self._output_size))) # save with actual size
                    frame = ImageTk.PhotoImage(img_frame.resize(Size.CIF.value)) # but display with resizing
                    self.video_label.config(image=frame)
                    self.video_label.image = frame
                else:
                    self.stop_capture()
                    break
        except Exception as e:
            messagebox.showinfo("Error", str(e))
        finally:
            self.stop_capture()
            video_reader.close()
            self.video_writer.close()
