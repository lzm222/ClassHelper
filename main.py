from src.choose import ChooseStudent
import tkinter as tk
from src.timer import Timer
import os
import asyncio
from async_tkinter_loop import async_handler, async_mainloop
import src.config as config

if os.name  == "nt":
    import src.wallpaperTimetable as Ttable

VERSION = config.VERSION


class Main:
    def __init__(self, root):
        self.mainWindow = root
        self.window = root
        self.mainWindow.title(f"课堂小助手 {VERSION}")
        self.width = self.mainWindow.winfo_screenwidth()
        self.height = self.mainWindow.winfo_screenheight()
        self.mainWindow.geometry(
            "%dx%d+%d+%d"
            % (
                self.width // 2,
                self.height // 2,
                self.width // 4,
                self.height // 4,
            )
        )
        self.count = 0
        self.chooseStudentButton = tk.Button(
            self.mainWindow, command=lambda: ChooseStudent(self), text="随机选人"
        )
        self.chooseStudentButton.pack()
        self.timerButton = tk.Button(
            self.mainWindow, command=lambda: Timer(self), text="计时器"
        )
        self.timerButton.pack()
        if os.name == "nt":
            self.timerButton = tk.Button(
                self.mainWindow, 
                command=async_handler(Ttable.run), 
                text="桌面课表"
            )
            self.timerButton.pack()

        # 拦截主窗口的关闭事件
        self.mainWindow.protocol("WM_DELETE_WINDOW", self.onClosing)

    def onClosing(self):
        self.mainWindow.withdraw()

        def tryClose():
            if self.count > 0:
                self.mainWindow.after(100, tryClose)  # 每100毫秒检查一次
            else:
                self.mainWindow.destroy()

        tryClose()

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    async_mainloop(root)