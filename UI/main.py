# -*- coding: utf-8 -*-
# @Time     :2022/1/3 21:59
# @Author   :Z
# @File     :main.py

import tkinter as tk
from tkinter.simpledialog import askinteger
from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self, name = "demo"):
        super().__init__()
        self.title(name)
        self.geometry("1024x768")


        self.worker = None
        self.label = None

        self.count = None
        self.img = None
        self.photo = None

        self.init()

    def init(self):
        '''
            初始化原界面
        :return: 
        '''
        self.create_worker()

        # 设置每个格子的大小
        for col in range(9):
            self.button_frame.grid_columnconfigure(col, minsize = 30)
        self.button_frame.grid_rowconfigure(0, minsize=40)

        self.button1 = tk.Button(self.button_frame, font = ('黑体', 15), height=2, text = "倒计时", command = self.cdStart)
        self.button1.grid(row=1, column=1)

        self.button2 = tk.Button(self.button_frame, font=('黑体', 15), height=2, text="倒计时")
        self.button2.grid(row=1, column=3)

        self.button3 = tk.Button(self.button_frame, font=('黑体', 15), height=2, text="倒计时")
        self.button3.grid(row=1, column=5)

        self.button4 = tk.Button(self.button_frame, font=('黑体', 15), height=2, text="倒计时")
        self.button4.grid(row=1, column=7)

    def create_worker(self):
        if self.worker is not None:
            self.worker.destroy()
        if self.label is not None:
            self.label.destroy()

        self.update()

        self.worker = tk.Frame(self, height=self.winfo_height() * 0.8, width=self.winfo_width(), bg='blue')
        self.worker.grid(row=0, column=0)

        self.button_frame = tk.Frame(self, height=self.winfo_height() * 0.2, width=self.winfo_width())
        self.button_frame.grid(row=1, column=0)


    def cdStart(self):
        self.init()

        self.label = tk.Label(self.worker, text="倒计时开始！", font=("黑体", 40))
        self.label.place(relx=0.5, rely=0.5, anchor='center')

        self.count = askinteger("倒计时", "倒计时")
        self.countdown(self.count)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="计时结束")
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)


    def randomStart(self):
        for windget in self.worker.winfo_children():
            windget.destroy()
        self.text = tk.Text(self.worker, height = 600, width = 1024)
        self.text.pack()
        self.randomAdd(30)

    def randomAdd(self, count = 100):
        self.text.insert("insert", "人生重启！\n")
        self.after(500, self.randomAdd)

    def showPhoto(self):

        self.img = Image.open('t.png')  # 打开图片
        self.photo = ImageTk.PhotoImage(self.img)  # 用PIL模块的PhotoImage打开
        imglabel = tk.Label(self.worker, image=self.photo)
        imglabel.pack()

    def reset(self):
        for windget in self.winfo_children():
            windget.destroy()
        self.__init__()

if __name__ == "__main__":
    root = App("一点小程序")
    root.mainloop()