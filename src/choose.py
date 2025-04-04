import tkinter as tk
from random import choice
from random import seed
from tkinter import messagebox as mes
from time import time
import os.path as path
import simpleaudio as sa


class ChooseStudent:
    def __init__(self, father):
        seed(time())  # 随机种子
        self.namelist = []
        father.count += 1
        # 初始化窗口
        self.father = father
        self.top = tk.Toplevel(father.top)
        self.top.title("随机选人")
        self.top.wm_attributes("-topmost", True)
        self.width = father.width
        self.height = father.height
        self.top.geometry(
            "%dx%d+%d+%d"
            % (
                self.width // 8,
                self.height // 8,
                self.width - self.width // 8 - 40,
                self.height - self.height // 8 - 80,
            )
        )
        self.bun = tk.Button(self.top, command=self.choose, text="选人")
        self.bun.pack()
        self.top.protocol("WM_DELETE_WINDOW", self.on_closing)

    def fileIn(self):
        # 读取名单
        try:
            filepath = path.normpath(
                path.join(path.dirname(__file__), "../resource/namelist.txt")
            )
            with open(filepath, "r", encoding="utf-8") as f:
                self.namelist = f.read().split("\n")
            if self.namelist[0] == "":
                raise FileNotFoundError
        except FileNotFoundError:
            mes.showerror("错误", "数据获取失败", parent=self.top)
            return False
        return True

    def show(self, name):
        # 设置消息框
        dialog = tk.Toplevel(self.top)
        dialog.title("结果")
        dialog.geometry(
            "%dx%d+%d+%d"
            % (
                self.width // 2,
                self.height // 2,
                self.width // 4,
                self.height // 4,
            )
        )
        # 自定义字体
        font = ("黑体", 150)
        # 显示结果
        label = tk.Label(dialog, text=name, font=font)
        label.pack(expand=True, anchor="center")
        audio = path.normpath(
            path.join(path.dirname(__file__), "../assets/audio/choose/qiang.wav")
        )
        sa.WaveObject.from_wave_file(audio).play()

    def choose(self):
        # 检查旧窗口是否已关闭
        for i in self.top.winfo_children():
            if i.winfo_class() == "Toplevel":
                i.destroy()
        # 选人
        if self.fileIn():
            self.show(choice(self.namelist))

    def on_closing(self):
        self.father.count -= 1
        self.top.destroy()
