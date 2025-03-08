from choose import ChooseStudent
import tkinter as tk
from timer import Timer


class Main:
    def __init__(self):
        # 初始化窗口
        self.top = tk.Tk()
        self.top.title(f"课堂小助手 {VIERSION}")
        width = self.top.winfo_screenwidth()
        height = self.top.winfo_screenheight()
        self.top.geometry(
            "%dx%d+%d+%d"
            % (
                width // 2,
                height // 2,
                width // 4,
                height // 4,
            )
        )
        self.bun1 = tk.Button(self.top, command=ChooseStudent, text="随机选人")
        self.bun1.pack()
        self.bun2 = tk.Button(self.top, command=Timer, text="计时器")
        self.bun2.pack()


VIERSION = "Alpha-0.3"

if __name__ == "__main__":
    Main()
    tk.mainloop()
