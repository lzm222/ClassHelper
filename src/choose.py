import tkinter as tk
from random import choice
from random import seed
from tkinter import messagebox as mes
from time import time
import os.path as path
import simpleaudio as sa
from src.getResource import getResourcePath


class ChooseStudent:
    def __init__(self, parent):
        seed(time())  # 随机种子
        self.nameList = []
        parent.count += 1
        # 初始化窗口
        self.parent = parent
        self.window = tk.Toplevel(parent.window)
        self.window.title("随机选人")
        self.window.wm_attributes("-topmost", True)
        self.width = parent.width
        self.height = parent.height
        self.window.geometry(
            "%dx%d+%d+%d"
            % (
                self.width // 8,
                self.height // 8,
                self.width - self.width // 8 - 40,
                self.height - self.height // 8 - 80,
            )
        )
        self.chooseButton = tk.Button(
            self.window, command=self.selectStudent, text="选人"
        )
        self.chooseButton.pack()
        self.window.protocol("WM_DELETE_WINDOW", self.onClosing)

    def loadNameList(self):
        # 读取名单
        try:
            file_path = getResourcePath("namelist.txt")
            with open(file_path, "r", encoding="utf-8") as f:
                self.nameList = f.read().split("\n")
            if not self.nameList or self.nameList[0] == "":
                raise FileNotFoundError
        except FileNotFoundError:
            mes.showerror("错误", "数据获取失败", parent=self.window)
            return False
        return True

    def displayResult(self, name):
        # 设置消息框
        resultWindow = tk.Toplevel(self.window)
        resultWindow.title("结果")
        resultWindow.geometry(
            "%dx%d+%d+%d"
            % (
                self.width // 2,
                self.height // 2,
                self.width // 4,
                self.height // 4,
            )
        )
        # 自定义字体
        resultFont = ("黑体", 150)
        # 显示结果
        resultLabel = tk.Label(resultWindow, text=name, font=resultFont)
        resultLabel.pack(expand=True, anchor="center")
        audioPath = path.normpath(
            path.join(path.dirname(__file__), "../assets/audio/choose/qiang.wav")
        )
        sa.WaveObject.from_wave_file(audioPath).play()

    def selectStudent(self):
        # 检查旧窗口是否已关闭
        for widget in self.window.winfo_children():
            if widget.winfo_class() == "Toplevel":
                widget.destroy()
        # 选人
        if self.loadNameList():
            self.displayResult(choice(self.nameList))

    def onClosing(self):
        self.parent.count -= 1
        self.window.destroy()
