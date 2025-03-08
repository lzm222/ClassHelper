import tkinter as tk
import time
import tkinter.messagebox as mes
from tkinter.simpledialog import askinteger
import os.path as path
import simpleaudio as sa


class Timer:
    def __init__(self):
        # 初始化窗口
        self.top = tk.Tk()
        self.top.title("计时器")
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
        self.input_time = 0
        self.set_time = tk.StringVar(self.top, value="00:00:00")
        self.start_time = 0
        self.status = False
        self.timer = tk.Label(self.top, textvariable=self.set_time, font=("Arial", 100))
        self.button_bar = tk.Frame(self.top)
        self.start_bun = tk.Button(self.button_bar, command=self.start, text="开始")
        self.stop_bun = tk.Button(self.button_bar, command=self.stop, text="暂停")
        self.set_bun = tk.Button(
            self.button_bar,
            command=self.get_time,
            text="设置时间",
        )
        self.timer.pack()
        self.button_bar.pack()
        self.start_bun.pack(side=tk.LEFT, padx=5)
        self.stop_bun.pack(side=tk.LEFT, padx=5)
        self.set_bun.pack(side=tk.LEFT, padx=5)
        self.top.protocol("WM_DELETE_WINDOW", self.on_closing)

    def get_time(self):
        if self.status:
            self.show_error("请先暂停计时器")
            return
        ret = askinteger("设置时间", "请输入时间(分钟)", minvalue=1)
        if ret != None:
            self.input_time = ret * 60
            self.set_time.set(
                time.strftime(
                    "%H:%M:%S",
                    time.gmtime(self.input_time),
                )
            )

    def start(self):
        if self.input_time == 0:
            self.show_error("请先设置时间")
            return
        if self.status:
            return
        self.status = True
        self.start_time = time.time()
        self.updater()

    def stop(self):
        if not self.status:
            return
        self.status = False
        self.input_time = self.input_time - (time.time() - self.start_time)

    def updater(self):
        if self.status:
            if time.time() - self.start_time < self.input_time:
                self.set_time.set(
                    time.strftime(
                        "%H:%M:%S",
                        time.gmtime(self.input_time - (time.time() - self.start_time)),
                    )
                )
                self.top.after(1000, self.updater)
            else:
                self.finish()

    def finish(self):
        self.status = False
        self.input_time = 0
        self.set_time.set("00:00:00")
        rel_path = ["assets", "audio", "timer", "finish.wav"]
        audio = path.join(path.dirname(path.abspath(__file__)), *rel_path)
        sa.WaveObject.from_wave_file(audio).play()

    def on_closing(self):
        sa.stop_all()
        self.top.destroy()

    def show_error(self, text: str):
        mes.showerror("错误", text, parent=self.top)
