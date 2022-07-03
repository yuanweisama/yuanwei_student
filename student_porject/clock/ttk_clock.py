# coding=utf-8
from tkinter import *
import _tkinter
import math
import time
from threading import Thread


class Clock:
    def __init__(self, master, x, y, width, height, radius):
        """
    :param master: 父窗口
    :param x: 时钟中心点的x坐标
    :param y: 时钟中心点的y坐标
    :param width: 画布的宽度
    :param height: 画布的高度
    :param radius: 时钟钟盘的半径
        """
        self.centerX = x
        self.centerY = y
        self.radius = radius
        self.canvas = Canvas(master, width=width, height=height)  # 画布
        self.canvas.pack()
        self.canvas.create_oval(
            x - radius,
            y - radius,
            x + radius,
            y + radius)  # 画钟框
        self.id_lists = []
        self.hourHandRadius = self.radius * 1.0 / 4  # 指针长度
        self.minHandRadius = self.radius * 2.0 / 3  # 分针长度
        self.secHandRadius = self.radius * 4.0 / 5  # 秒针长度
        self.timeVar = StringVar()
        # self.timeVar.set('')
        self.timeLabel = Label(self.canvas.master, textvariable=self.timeVar)
        self.timeLabel.pack(side=BOTTOM)
        # self.canvas.master.protocol('WM_DELETE_WINDOW', self.canvas.master.destroy)

    def __del__(self):
        self._delete_items(self.id_lists)

    # 绘制时钟钟盘
    def draw_clock_dial(self):
        # 绘制钟盘上的数字1-12
        r = self.radius - 15
        for i in range(1, 13):
            rad = 2 * math.pi / 12 * i
            x = self.centerX + math.sin(rad) * r
            y = self.centerY - math.cos(rad) * r
            idd = self.canvas.create_text(x, y, text=str(i))
            self.id_lists.append(idd)
        # 绘制钟盘上的刻度
        r1 = self.radius - 5
        r2 = self.radius
        for i in range(1, 61):
            rad = 2 * math.pi / 60 * i
            x1, y1 = self._get_pos_by_rad_and_radius(rad, r1)
            x2, y2 = self._get_pos_by_rad_and_radius(rad, r2)
            ii_id = self.canvas.create_line(x1, y1, x2, y2)
            self.id_lists.append(ii_id)

    # 显示时间
    def showtime(self, tm):
        hour = tm.tm_hour % 12
        tm_min = tm.tm_min
        sec = tm.tm_sec
        sec_rad = 2 * math.pi / 60 * sec
        min_rad = 2 * math.pi / 60 * (tm_min + sec / 60.0)
        hour_rad = 2 * math.pi / 12 * (hour + tm_min / 60.0)
        time_str = '当前时间: %d-%02d-%02d %02d:%02d:%02d' % (tm.tm_year, tm.tm_mon, tm.tm_mday, hour, tm_min, sec)
        self.timeVar.set(time_str)
        hour_id = self._drawline(hour_rad, self.hourHandRadius, 6)
        min_id = self._drawline(min_rad, self.minHandRadius, 4)
        sec_id = self._drawline(sec_rad, self.secHandRadius, 3)
        return hour_id, min_id, sec_id

    def run(self):
        def _run():
            while True:
                tm = time.localtime()
                id_lists = self.showtime(tm)
                self.canvas.master.update()
                time.sleep(1)
                self._delete_items(id_lists)

        third = Thread(target=_run)  # 创建新的线程
        third.run()  # 启动线程

    def _drawline(self, rad, radius, width):
        x, y = self._get_pos_by_rad_and_radius(rad, radius)
        ii_dd = self.canvas.create_line(
            self.centerX, self.centerY, x, y, width=width)
        return ii_dd

    def _get_pos_by_rad_and_radius(self, rad, radius):
        x = self.centerX + radius * math.sin(rad)
        y = self.centerY - radius * math.cos(rad)
        return x, y

    def _delete_items(self, id_lists):
        for iid in id_lists:
            try:
                self.canvas.delete(iid)
            except BaseException:
                pass


if __name__ == '__main__':
    root = Tk()
    root.title('时钟')
    clock = Clock(root, 200, 200, 400, 400, 150)
    clock.draw_clock_dial()
    clock.run()
    root.mainloop()
