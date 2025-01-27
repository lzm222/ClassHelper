import pyttsx3
import time
from os import path
from sys import exit
import tkinter as tk
from tkinter import messagebox as mes
from threading import Thread
from threading import Event

flag = Event()


class Read:
    def __init__(self):
        self.engine = pyttsx3.init()  # 初始化tts引擎
        # 初始化窗口
        self.top = tk.Tk()
        self.top.title("默写")
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
        thread = Thread(target=self.run, daemon=True)
        self.bun1 = tk.Button(self.top, command=thread.start, text="开始")
        self.bun1.pack()
        self.bun2 = tk.Button(self.top, command=flag.clear, text="中断")
        self.bun2.pack()
        self.bun3 = tk.Button(self.top, command=flag.set, text="继续")
        self.bun3.pack()

    def fileIn(self):
        # 读取文件
        filePath = path.join(path.dirname(path.abspath(__file__)), "wordlist.txt")
        try:
            file = open(filePath, "r", encoding="utf-8")
        except FileNotFoundError:
            mes.showerror("错误", "数据获取失败")
            exit(1)
        self.lis = file.read().split("\n")
        file.close()

    def read(self, start):
        self.flag.set()  # 重置
        end = len(self.lis) - 1  # 设置结束位置
        num = end + 1
        state = "开始"
        if start != 0:
            state = "继续"
        # 开始提示
        self.engine.setProperty("rate", 200)
        self.engine.say(f"默写将在5秒后{state}，请做好准备")
        self.engine.runAndWait()
        time.sleep(5)
        self.engine.say(state)
        self.engine.runAndWait()
        time.sleep(0.2)
        # 开始
        self.engine.setProperty("rate", 120)
        for i in range(start, end + 1):
            if not flag.is_set():  # 中断
                self.engine.setProperty("rate", 200)
                self.engine.say("默写已中断")
                self.engine.runAndWait()
                flag.wait()
                self.engine.say("默写已继续")
                self.engine.runAndWait()
            word = self.lis[i]  # 当前词语
            # 报号
            self.engine.say(str(i + 1))
            self.engine.runAndWait()
            time.sleep(0.5)
            # 播报
            self.engine.say(word)
            self.engine.runAndWait()
            time.sleep(4)
            # 重复
            self.engine.say(word)
            self.engine.runAndWait()
            time.sleep(4.5)
        # 结束提示
        self.engine.setProperty("rate", 200)
        self.engine.say(f"默写完毕，总计{num}个词语")
        self.engine.runAndWait()

    def run(self, start=0):
        self.fileIn()
        self.read(start)
