"""
作者:ls
程序名:课堂小助手
版本:Alpha-0.1
文件编码:utf-8
"""

VIERSION = "Alpha-0.1"

import tkinter as tk
from random import choice
from random import seed
from tkinter import messagebox as mes
from time import time
import os.path as path
from sys import exit


class Classhelper:
    def __init__(self):
        seed(time())  # 随机种子
        self.namelist = []
        # 初始化窗口
        self.top = tk.Tk()
        self.top.title(f"课堂小助手 {VIERSION}")
        self.top.wm_attributes("-topmost", True)
        width = self.top.winfo_screenwidth()
        height = self.top.winfo_screenheight()
        self.top.geometry(
            "%dx%d+%d+%d"
            % (
                width // 8,
                height // 8,
                width - width // 8 - 40,
                height - height // 8 - 80,
            )
        )
        self.bun = tk.Button(self.top, command=self.choose, text="选人")
        self.bun.pack()
        tk.mainloop()  # 启动

    def get_file(self):
        # 读取名单
        try:
            filepath = path.join(path.dirname(path.abspath(__file__)), "namelist.txt")
            with open(filepath, "r", encoding="utf-8") as f:
                self.namelist = f.read().split("\n")
        except OSError:
            mes.showerror("错误", "数据获取失败")
            exit(1)

    def choose(self):
        # 选人
        self.get_file()
        mes.showinfo("结果", f"恭喜{choice(self.namelist)}同学，请你回答该问题！")


a = Classhelper()
