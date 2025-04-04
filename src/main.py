from choose import ChooseStudent
import tkinter as tk
from timer import Timer


class Main:
    def __init__(self):
        # 初始化窗口
        self.top = tk.Tk()
        self.top.title(f"课堂小助手 {VERSION}")
        self.width = self.top.winfo_screenwidth()
        self.height = self.top.winfo_screenheight()
        self.top.geometry(
            "%dx%d+%d+%d"
            % (
                self.width // 2,
                self.height // 2,
                self.width // 4,
                self.height // 4,
            )
        )
        self.count = 0
        self.bun1 = tk.Button(
            self.top, command=lambda: ChooseStudent(self), text="随机选人"
        )
        self.bun1.pack()
        self.bun2 = tk.Button(self.top, command=lambda: Timer(self), text="计时器")
        self.bun2.pack()

        # 拦截主窗口的关闭事件
        self.top.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.top.withdraw()

        def try_close():
            if self.count > 0:
                self.top.after(100, try_close)  # 每100毫秒检查一次
            else:
                self.top.destroy()

        try_close()


VERSION = "Alpha-0.4"

if __name__ == "__main__":
    Main()
    tk.mainloop()
