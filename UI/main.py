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
        self.init()

        self.count = None
        self.img = None
        self.photo = None

    def init(self):
        '''
            初始化原界面
        :return: 
        '''

        self.worker = tk.Frame(self, height= 600, width = 1024,bg = 'blue')
        self.worker.pack()

        self.button1 = tk.Button(self, text ="倒计时", font = ('黑体', 15), bd = 3, width = 10, height=2, padx= 1, pady= 1, command=self.cdStart)
        self.button1.place(relx = 0.15, rely = 0.85)

        self.button2 = tk.Button(self, text="人生模拟器", font = ('黑体', 15), bd = 3, width = 10, height=2, padx= 1, pady= 1, command=self.randomStart)
        self.button2.place(relx= 0.35, rely = 0.85)

        self.button3 = tk.Button(self, text="相册", font = ('黑体', 15), bd=3, width=10, height=2, padx=1, pady=1, command=self.showPhoto)
        self.button3.place(relx= 0.55, rely = 0.85)

        self.button4 = tk.Button(self, text="重置", font = ('黑体', 15), bd=3, width=10, height=2, padx=1, pady=1, bg = 'purple', command=self.reset)
        self.button4.place(relx= 0.75, rely = 0.85)

    def cdStart(self):
        for windget in self.worker.winfo_children():
            windget.destroy()

        self.label = tk.Label(self.worker, text="倒计时开始！", font=("黑体", 40))
        self.label.place(relx=0.35, rely=0.45)

        self.count = askinteger("倒计时", "倒计时")
        self.countdown(self.count)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="计时结束")
        else:
            self.label.place(relx=0.45, rely=0.45)
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