from utility.logger import Logger
from wx import App

from cut_videos.cut_video import Window

if __name__ == "__main__":
    with Logger():
        app = App(False)
        frame = Window()
        frame.Show()
        app.MainLoop()