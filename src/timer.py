import tkinter as tk
import time
import tkinter.messagebox as mes
from tkinter.simpledialog import askinteger
import os.path as path
import simpleaudio as sa


class Timer:
    def __init__(self, parent):
        parent.count += 1
        # 初始化窗口
        self.parent = parent
        self.window = tk.Toplevel(parent.top)
        self.window.title("计时器")
        self.width = parent.width
        self.height = parent.height
        self.window.geometry(
            "%dx%d+%d+%d"
            % (
                self.width // 2,
                self.height // 2,
                self.width // 4,
                self.height // 4,
            )
        )
        self.remainingTime = 0
        self.displayTime = tk.StringVar(self.window, value="00:00:00")
        self.startTime = 0
        self.isRunning = False
        self.timeLabel = tk.Label(
            self.window, textvariable=self.displayTime, font=("Arial", 100)
        )
        self.buttonFrame = tk.Frame(self.window)
        self.startButton = tk.Button(self.buttonFrame, command=self.start, text="开始")
        self.stopButton = tk.Button(self.buttonFrame, command=self.stop, text="暂停")
        self.setButton = tk.Button(
            self.buttonFrame,
            command=self.getTime,
            text="设置时间",
        )
        self.timeLabel.pack()
        self.buttonFrame.pack()
        self.startButton.pack(side=tk.LEFT, padx=5)
        self.stopButton.pack(side=tk.LEFT, padx=5)
        self.setButton.pack(side=tk.LEFT, padx=5)
        self.window.protocol("WM_DELETE_WINDOW", self.onClosing)

    def getTime(self):
        if self.isRunning:
            self.showError("请先暂停计时器")
            return
        userInput = askinteger(
            "设置时间", "请输入时间(分钟)", minvalue=1, parent=self.window
        )
        if userInput is not None:
            self.remainingTime = userInput * 60
            self.displayTime.set(
                time.strftime(
                    "%H:%M:%S",
                    time.gmtime(self.remainingTime),
                )
            )

    def start(self):
        if self.remainingTime == 0:
            self.showError("请先设置时间")
            return
        if self.isRunning:
            return
        self.isRunning = True
        self.startTime = time.time()
        self.updater()

    def stop(self):
        if not self.isRunning:
            return
        self.isRunning = False
        self.remainingTime = self.remainingTime - (time.time() - self.startTime)

    def updater(self):
        if self.isRunning:
            if time.time() - self.startTime < self.remainingTime:
                self.displayTime.set(
                    time.strftime(
                        "%H:%M:%S",
                        time.gmtime(
                            self.remainingTime - (time.time() - self.startTime)
                        ),
                    )
                )
                self.window.after(1000, self.updater)
            else:
                self.finish()

    def finish(self):
        self.isRunning = False
        self.remainingTime = 0
        self.displayTime.set("00:00:00")
        audio = path.normpath(
            path.join(path.dirname(__file__), "../assets/audio/timer/finish.wav")
        )
        sa.WaveObject.from_wave_file(audio).play()

    def onClosing(self):
        sa.stop_all()
        self.parent.count -= 1
        self.window.destroy()

    def showError(self, text: str):
        mes.showerror("错误", text, parent=self.window)
