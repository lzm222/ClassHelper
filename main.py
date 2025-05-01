from src.choose import ChooseStudent
import tkinter as tk
from src.timer import Timer
import os

VERSION = "Beta-0.6"


class Main:
    def __init__(self):
        # 初始化窗口
        self.mainWindow = tk.Tk()
        self.window = self.mainWindow
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

def run():
    if os.name  == "nt":
        import src.wallpaperTimetable
    tk.mainloop()

if __name__ == "__main__":
    Main()
    run()
