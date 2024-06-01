from tkinter import Canvas, Button, Label, filedialog, messagebox
import tkinter as tk
from imageio_ffmpeg import get_ffmpeg_exe
import subprocess
import os
from pathlib import Path
import pprint
import json

TOP_PATH = Path(__file__).resolve().parent.parent.absolute()
FFPROBE_PATH = os.path.join(TOP_PATH, "binaries", "ffprobe-win32-v4.1.exe")

class MetadataPage(tk.Frame):
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
        self.canvas.place(x=0, y=0)

        self.file_opener = Button(
            master=self,
            text="Pick a video",
            command=lambda: self.open_file(),
        )
        self.file_opener.place(
            x=100,
            y=100,
            width=178,
            height=43,
        )
        
        self.picked_file_name = Label(
            master=self,
        )
        self.picked_file_name.place(
            x=400,
            y=100,
            width=500,
            height=43,
        )

        self.run_trigger = Button(
            master=self,
            text="Run",
            command=lambda: self.process_and_dump_details(),
        )
        self.run_trigger.place(
            x=400,
            y=200,
            width=178,
            height=43,
        )
    
    def open_file(self):
        self.video_path = filedialog.askopenfilename(title="Input your video")

        self.video_name = "".join(self.video_path.split("/")[-1].split(".")[:-1])
        self.video_dir = "/".join(self.video_path.split("/")[:-1])
        self.picked_file_name.config(text=self.video_path)

        if True:
            pass
        else:
            pass
    
    def process_and_dump_details(self):
        output_dir = f"{self.video_dir}/{self.video_name}"
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        try:
            all_frames_with_mvs_dir = f"{output_dir}/mvs"
            if not os.path.exists(all_frames_with_mvs_dir):
                os.mkdir(all_frames_with_mvs_dir)

            p = subprocess.run(
                args=[
                    get_ffmpeg_exe(),
                    "-flags2",
                    "+export_mvs",
                    "-i",
                    self.video_path,
                    "-vf",
                    "codecview=mv=pf+bf+bb",
                    f"{all_frames_with_mvs_dir}/frame_%5d.bmp",
                ],
            )

            res = None
            with open(f"{output_dir}/metadata.json", "w") as metadata_file:
                p = subprocess.run(
                    args=[
                        FFPROBE_PATH,
                        "-show_frames",
                        "-print_format",
                        "json",
                        self.video_path,
                    ],
                    stdout=metadata_file,
                )

            with open(f"{output_dir}/metadata.json", "r") as metadata_file:
                res = json.load(metadata_file)

            if not res.get("frames") or len(res.get("frames")) <= 0:
                return
            
            for idx, info in enumerate(res.get("frames")):
                old_filename = f"{all_frames_with_mvs_dir}/frame_{idx+1:05d}.bmp"
                if not os.path.exists(old_filename):
                    messagebox.showinfo("Info", f"{old_filename} not found. Continuing ...")
                    continue

                os.replace(
                    old_filename,
                    f"{all_frames_with_mvs_dir}/frame_{idx+1:05d}_{info.get('pict_type')}_{info.get('pkt_size')}.bmp"
                ) 

            summary = {
                "Overall": {
                    "Total number of frame": len(res.get("frames")),
                    "Total packet size in bytes": sum(map(lambda i: int(i.get("pkt_size")), res.get("frames"))),
                },
                "Total unrecognized frame type": sum(map(lambda i: int(i.get("pict_type") not in ("I", "P", "B")), res.get("frames"))),
            }
            types = set(map(lambda i: i.get("pict_type"), res.get("frames")))
            for typ in types:
                temp = list(filter(lambda i: int(i.get("pict_type") == typ), res.get("frames")))
                packet_sizes = list(map(lambda i: int(i.get("pkt_size")), temp))
                summary.update({
                    f"{typ}-frame": {
                        "Number of frame": len(temp),
                        "Max size in byte": max(packet_sizes),
                        "Min size in byte": min(packet_sizes),
                        "Avg size in byte": sum(packet_sizes) / len(temp),
                    }
                })

            pprint.pprint(summary)

        except Exception as e:
            messagebox.showerror("Error", e)
