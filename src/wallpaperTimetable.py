import ctypes
import csv
import plotly.graph_objects as go
from PIL import Image
import ctypes
from os import path
from tkinter import messagebox as mes

from src.getResource import getResourcePath

async def run() -> None:
    #读取csv
    csv_path = getResourcePath("timetable.csv")
    data = []
    if not path.exists(csv_path):
        mes.showerror("错误", "未找到课表文件")
        return
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)

    # 生成表格
    tablePath = getResourcePath("timetable.png")
    go.Figure(data=[go.Table(
        header=dict(values=data[0]), 
        cells=dict(values=list(zip(*data[1:])))
    )]).write_image(tablePath)

    # 生成新背景
    wallpaperPath = getResourcePath("wallpaper.jpg")
    if not path.exists(wallpaperPath):
        mes.showerror("错误", "未找到壁纸文件")
        return
    wallpaper = Image.open(wallpaperPath)
    tableImg = Image.open(tablePath)
    position = (wallpaper.width - tableImg.width - 150, 150)
    tableImg = tableImg.resize((tableImg.width + 150, tableImg.height + 150))
    wallpaper.paste(tableImg, position)
    outputPath = getResourcePath("outputWallpaper.jpg")
    wallpaper.save(outputPath)
    # 设置背景
    ctypes.windll.user32.SystemParametersInfoW(20, 0, outputPath, 0)
