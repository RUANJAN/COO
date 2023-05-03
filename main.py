import tkinter as tk
from tkinter import ttk
from tkinter import Button, Frame
from datasoerce import CarbonFootPrint
from PIL import Image, ImageTk
import csv
# 導入資料庫模組
from datasoerce import *


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        # ----------------建立畫布--------------------
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('default')  # 畫布
        ttkStyle.configure('TLabelframe', borderwidth=0)

        # 建立圖片
        pic001Image1 = Image.open("./images/pic001.jpg")
        self.pic001 = ImageTk.PhotoImage(pic001Image1)
        self.canvas = tk.Canvas(self, width=500, height=250)  # 畫布
        self.canvas.pack()
        self.canvas.create_image(0, 5, image=self.pic001, anchor='nw')
        # 建立logo
        logoImage = Image.open('./Images/co2logo.png')
        resizeImage = logoImage.resize((89, 82), Image.LANCZOS)
        self.logoTkimage = ImageTk.PhotoImage(resizeImage)
        self.canvas.create_image(20, 30, image=self.logoTkimage, anchor='nw')
        # 建立Button
        btn = Button(self, text='石油', width=10,                    height=2, bd='10', command=draw_oil_co2)  # 石油
        btn.place(x=100, y=120)

        btn = Button(self, text='煤礦', width=10,
                    height=2, bd='10', command=draw_oil_co2)  # 煤礦圖
        btn.place(x=200, y=120)

        btn = Button(self, text='天然氣', width=10,
                    height=2, bd='10', command=draw_oil_co2)  # 天然氣圖表
        btn.place(x=300, y=120)

        btn = Button(self, text='甲烷', width=10,
                    height=2, bd='10', command=draw_oil_co2)  # 天然氣圖表
        btn.place(x=400, y=120)
        # 建立medianFrame
        medianFrame = ttk.Labelframe(self, text="各國家")
        # 建立combobox
        comboBoxFrame = ttk.LabelFrame(self, text="各國家")
        comboBoxFrame.pack(side=tk.LEFT, fill=tk.Y, padx=30)

        csv_filename = 'a.csv'
        with open(csv_filename) as f:
            reader = csv.reader(f)
            lst = list(tuple(line) for line in reader)
            lst.insert(0, '請選擇一個國家')
        comboBoxValues = (lst)

        comboBox = ttk.Combobox(comboBoxFrame, state="readonly")
        comboBox.pack()
        comboBox['values'] = comboBoxValues
        comboBox.current(0)
        comboBox.pack(side=tk.TOP)

        medianFrame.pack(side=tk.LEFT)
        # 建立bottomFrame
        bottomFrame = ttk.Labelframe(self)
        bottomFrame.pack(side=tk.LEFT)
        # 建立treeViewFrame
        treeViewFrame = ttk.Labelframe(self)
        treeViewFrame.pack(side=tk.RIGHT)
        # 建立treeview
        columns = ('#1', '#2', '#3')
        tree = ttk.Treeview(treeViewFrame, columns=columns, show='headings')
        tree.heading('#1', text='country')
        tree.column("#1", minwidth=0, width=75)
        tree.heading('#2', text='population')
        tree.column("#2", minwidth=0, width=100)
        tree.heading('#3', text='co2')
        tree.column("#3", minwidth=0, width=30)
        tree.pack(side=tk.LEFT)
        # ----------幫treeview加scrollbar----------------------------------
        scrollbar = ttk.Scrollbar(treeViewFrame, command=tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.config(yscrollcommand=scrollbar.set)
# 主程式


def main():

    try:
        api_list = CarbonFootPrint.download_aqi()
        #print(type(api_list))

    except Exception as err:
        #print(str(err))
        return

    window = Window()
    window.title("碳足跡CarbonFootPrint")
    window.mainloop()


# 啟動點
if __name__ == "__main__":
    main()