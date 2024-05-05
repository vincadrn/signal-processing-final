import tkinter as tk
from pages.StartPage import StartPage
from pages.HowPage import HowPage
from pages.CompressPage import CompressPage
from pages.AboutPage import AboutPage
from pages.TakeVideoPage import TakeVideoPage

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, HowPage, CompressPage, AboutPage, TakeVideoPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.title("Video Compressor Application")
    app.geometry("950x560")
    app.resizable(False, False)
    app.mainloop()