import math
import os
import sys

import numpy
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
from PIL import Image, ImageQt
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QBuffer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QVBoxLayout, QMainWindow, QLineEdit, QScrollArea


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.main_window = QMainWindow()
        self.label = QLabel()
        self.title = 'PyQt5 image'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.Rrgb = 10
        self.Grgb = 0
        self.Brgb = 0
        self.Hhsv = 0
        self.Shsv = 0
        self.Vhsv = 0
        self.Ccmyk = 0
        self.Mcmyk = 0
        self.Ycmyk = 0
        self.Kcmyk = 0
        self.Llab = 0
        self.Alab = 0
        self.Blab = 0
        self.Hhsl = 0
        self.Shsl = 0
        self.Lhsl = 0
        self.Y = 0
        self.CR = 0
        self.CB = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)
        label5 = QLabel(self)
        rgbLabel = QLabel(self)
        hsvLabel = QLabel(self)
        cmykLabel = QLabel(self)
        hslLabel = QLabel(self)
        ycrcbLabel = QLabel(self)
        labLabel = QLabel(self)
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', 'C:/', 'Image File (*.jpg *.jpeg)')
        pixmap = QPixmap(filename)
        self.label.setPixmap(pixmap.scaledToHeight(300))
        img = pixmap.toImage()
        size = img.size()
        extension = os.path.splitext(filename)[-1]

        txt1 = "Разрешение: " + size.width().__str__() + "x" + size.height().__str__()
        txt2 = "Вес: " + img.sizeInBytes().__str__() + " байт"
        txt3 = "Глубина: " + img.depth().__str__()
        txt4 = "Формат: " + extension
        if img.hasAlphaChannel():
            txt5 = "Цветовая модель: ARGB"
        else:
            txt5 = "Цветовая модель: RGB"

        label1.setText(txt1)
        label2.setText(txt2)
        label3.setText(txt3)
        label4.setText(txt4)
        label5.setText(txt5)
        rgbLabel.setText('RGB')
        hsvLabel.setText('HSV')
        cmykLabel.setText('CMYK')
        hslLabel.setText('HSL')
        ycrcbLabel.setText('YCrCb(YCC)')
        labLabel.setText('LAB')

        print("Разрешение: ", size.width(), "x", size.height())
        print("Вес: ", img.sizeInBytes(), "байт")
        print("Глубина: ", img.depth())  # Глубина
        print("Формат: ", extension)  # Формат
        print("Цветовая модель: ", img.format())

        self.setFixedSize(500, 500)
        # button = QtWidgets.QPushButton()
        # button.setText("Rbg_to_cmyk")
        # button.clicked.connect(lambda: self.rgb_to_cmykSetImage(size.width(), size.height(),newImage))

        self.r = QLineEdit(self)
        self.r.setObjectName("R")
        self.r.setPlaceholderText("R")
        self.r.setText(self.Rrgb.__str__())
        self.r.editingFinished.connect(self.rgb_to_hsv_changed)

        self.g = QLineEdit(self)
        self.g.setObjectName("G")  # Устанавливаем имя для удобства доступа
        self.g.setPlaceholderText("G")
        self.g.setText(self.Grgb.__str__())
        self.g.editingFinished.connect(self.rgb_to_hsv_changed)

        self.b = QLineEdit(self)
        self.b.setObjectName("B")  # Устанавливаем имя для удобства доступа
        self.b.setPlaceholderText("B")
        self.b.setText(self.Brgb.__str__())
        self.b.editingFinished.connect(self.rgb_to_hsv_changed)

        self.HhsvLine = QLineEdit(self)
        self.HhsvLine.setObjectName("HhsvLine")
        self.HhsvLine.setPlaceholderText("H")
        self.HhsvLine.setText(self.Hhsv.__str__())
        self.HhsvLine.editingFinished.connect(self.hsv_to_rgb_changed)

        self.ShsvLine = QLineEdit(self)
        self.ShsvLine.setObjectName("Shsv")
        self.ShsvLine.setPlaceholderText("S")
        self.ShsvLine.setText(self.Shsv.__str__())
        self.ShsvLine.editingFinished.connect(self.hsv_to_rgb_changed)

        self.VhsvLine = QLineEdit(self)
        self.VhsvLine.setObjectName("Vhsv")
        self.VhsvLine.setPlaceholderText("V")
        self.VhsvLine.setText(self.Vhsv.__str__())
        self.VhsvLine.editingFinished.connect(self.hsv_to_rgb_changed)

        self.c = QLineEdit(self)
        self.c.setObjectName("C")  # Устанавливаем имя для удобства доступа
        self.c.setPlaceholderText("C")
        self.c.setText(self.Ccmyk.__str__())
        self.c.editingFinished.connect(self.cmyk_to_rgb_changed)

        self.m = QLineEdit(self)
        self.m.setObjectName("M")
        self.m.setPlaceholderText("M")
        self.m.setText(self.Mcmyk.__str__())
        self.m.editingFinished.connect(self.cmyk_to_rgb_changed)

        self.y = QLineEdit(self)
        self.y.setPlaceholderText("Y")
        self.y.setText(self.Ycmyk.__str__())
        self.y.editingFinished.connect(self.cmyk_to_rgb_changed)

        self.k = QLineEdit(self)
        self.k.setPlaceholderText("K")
        self.k.setText(self.Kcmyk.__str__())
        self.k.editingFinished.connect(self.cmyk_to_rgb_changed)

        self.HhslLine = QLineEdit(self)
        self.HhslLine.setObjectName("HhslLine")
        self.HhslLine.setPlaceholderText("H")
        self.HhslLine.setText(self.Hhsl.__str__())
        self.HhslLine.editingFinished.connect(self.hsl_to_rgb_changed)

        self.ShslLine = QLineEdit(self)
        self.ShslLine.setPlaceholderText("S")
        self.ShslLine.setText(self.Shsl.__str__())
        self.ShslLine.editingFinished.connect(self.hsl_to_rgb_changed)

        self.LhslLine = QLineEdit(self)
        self.LhslLine.setPlaceholderText("L")
        self.LhslLine.setText(self.Lhsl.__str__())
        self.LhslLine.editingFinished.connect(self.hsl_to_rgb_changed)

        self.Ycr = QLineEdit(self)
        self.Ycr.setObjectName("Ycr")
        self.Ycr.setPlaceholderText("Y")
        self.Ycr.setText(self.Y.__str__())
        self.Ycr.editingFinished.connect(self.ycrcb_to_rgb_changed)

        self.Cr = QLineEdit(self)
        self.Cr.setPlaceholderText("Cr")
        self.Cr.setText(self.CR.__str__())
        self.Cr.editingFinished.connect(self.ycrcb_to_rgb_changed)

        self.Cb = QLineEdit(self)
        self.Cb.setPlaceholderText("Cb")
        self.Cb.setText(self.CB.__str__())
        self.Cb.editingFinished.connect(self.ycrcb_to_rgb_changed)

        self.L = QLineEdit(self)
        self.L.setObjectName("L")
        self.L.setPlaceholderText("L")
        self.L.setText(self.Llab.__str__())
        self.L.editingFinished.connect(self.lab_to_rgb_changed)

        self.A = QLineEdit(self)
        self.A.setPlaceholderText("A")
        self.A.setText(self.Alab.__str__())
        self.A.editingFinished.connect(self.lab_to_rgb_changed)

        self.B = QLineEdit(self)
        self.B.setPlaceholderText("B")
        self.B.setText(self.Blab.__str__())
        self.B.editingFinished.connect(self.lab_to_rgb_changed)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(label1)
        vertical_layout.addWidget(label2)
        vertical_layout.addWidget(label3)
        vertical_layout.addWidget(label4)
        vertical_layout.addWidget(label5)

        vertical_layout.addWidget(rgbLabel)
        vertical_layout.addWidget(self.r)
        vertical_layout.addWidget(self.g)
        vertical_layout.addWidget(self.b)

        vertical_layout.addWidget(hsvLabel)
        vertical_layout.addWidget(self.HhsvLine)
        vertical_layout.addWidget(self.ShsvLine)
        vertical_layout.addWidget(self.VhsvLine)

        vertical_layout.addWidget(cmykLabel)
        vertical_layout.addWidget(self.c)
        vertical_layout.addWidget(self.m)
        vertical_layout.addWidget(self.y)
        vertical_layout.addWidget(self.k)

        vertical_layout.addWidget(hslLabel)
        vertical_layout.addWidget(self.HhslLine)
        vertical_layout.addWidget(self.ShslLine)
        vertical_layout.addWidget(self.LhslLine)

        vertical_layout.addWidget(ycrcbLabel)
        vertical_layout.addWidget(self.Ycr)
        vertical_layout.addWidget(self.Cr)
        vertical_layout.addWidget(self.Cb)

        vertical_layout.addWidget(labLabel)
        vertical_layout.addWidget(self.L)
        vertical_layout.addWidget(self.A)
        vertical_layout.addWidget(self.B)

        central_widget = QWidget()
        scroll_area = QScrollArea()
        central_widget.setLayout(vertical_layout)
        scroll_area.setWidget(central_widget)
        self.main_window.setCentralWidget(scroll_area)

        self.main_window.show()

    def rgb_to_hsv_changed(self):
        r = float(self.r.text())
        g = float(self.g.text())
        b = float(self.b.text())
        hsv = self.rgb_to_hsv(r, g, b)
        cmyk = self.rgb_to_cmyk(r, g, b)
        hsl = self.rgb_to_hsl(r, g, b)
        ycrcb = self.rgb_to_ycrcb(r, g, b)
        lab = self.rgb_to_lab(r, g, b)
        self.HhsvLine.setText(hsv[0].__str__())
        self.ShsvLine.setText(hsv[1].__str__())
        self.VhsvLine.setText(hsv[2].__str__())

        self.c.setText(cmyk[0].__str__())
        self.m.setText(cmyk[1].__str__())
        self.y.setText(cmyk[2].__str__())
        self.k.setText(cmyk[3].__str__())

        self.HhslLine.setText(hsl[0].__str__())
        self.ShslLine.setText(hsl[1].__str__())
        self.LhslLine.setText(hsl[2].__str__())

        self.Ycr.setText(ycrcb[0].__str__())
        self.Cr.setText(ycrcb[1].__str__())
        self.Cb.setText(ycrcb[2].__str__())

        self.L.setText(lab[0].__str__())
        self.A.setText(lab[1].__str__())
        self.B.setText(lab[2].__str__())

    def hsv_to_rgb_changed(self):
        h = float(self.HhsvLine.text())
        s = float(self.ShsvLine.text())
        v = float(self.VhsvLine.text())
        rgb = self.hsv_to_rgb(h, s, v)
        cmyk = self.rgb_to_cmyk(rgb[0], rgb[1], rgb[2])
        hsl = self.rgb_to_hsl(rgb[0], rgb[1], rgb[2])
        ycrcb = self.rgb_to_ycrcb(rgb[0], rgb[1], rgb[2])
        lab = self.rgb_to_lab(rgb[0], rgb[1], rgb[2])
        self.r.setText(rgb[0].__str__())
        self.g.setText(rgb[1].__str__())
        self.b.setText(rgb[2].__str__())

        self.c.setText(cmyk[0].__str__())
        self.m.setText(cmyk[1].__str__())
        self.y.setText(cmyk[2].__str__())
        self.k.setText(cmyk[3].__str__())

        self.HhslLine.setText(hsl[0].__str__())
        self.ShslLine.setText(hsl[1].__str__())
        self.LhslLine.setText(hsl[2].__str__())

        self.Ycr.setText(ycrcb[0].__str__())
        self.Cr.setText(ycrcb[1].__str__())
        self.Cb.setText(ycrcb[2].__str__())

        self.L.setText(lab[0].__str__())
        self.A.setText(lab[1].__str__())
        self.B.setText(lab[2].__str__())

    def cmyk_to_rgb_changed(self):
        c = float(self.c.text())
        m = float(self.m.text())
        y = float(self.y.text())
        k = float(self.k.text())
        rgb = self.cmyk_to_rgb(c, m, y, k)
        self.r.setText(rgb[0].__str__())
        self.g.setText(rgb[1].__str__())
        self.b.setText(rgb[2].__str__())

        hsv = self.rgb_to_hsv(rgb[0], rgb[1], rgb[2])
        hsl = self.rgb_to_hsl(rgb[0], rgb[1], rgb[2])
        ycrcb = self.rgb_to_ycrcb(rgb[0], rgb[1], rgb[2])
        lab = self.rgb_to_lab(rgb[0], rgb[1], rgb[2])

        self.r.setText(rgb[0].__str__())
        self.g.setText(rgb[1].__str__())
        self.b.setText(rgb[2].__str__())

        self.HhsvLine.setText(hsv[0].__str__())
        self.ShsvLine.setText(hsv[1].__str__())
        self.VhsvLine.setText(hsv[2].__str__())

        self.HhslLine.setText(hsl[0].__str__())
        self.ShslLine.setText(hsl[1].__str__())
        self.LhslLine.setText(hsl[2].__str__())

        self.Ycr.setText(ycrcb[0].__str__())
        self.Cr.setText(ycrcb[1].__str__())
        self.Cb.setText(ycrcb[2].__str__())

        self.L.setText(lab[0].__str__())
        self.A.setText(lab[1].__str__())
        self.B.setText(lab[2].__str__())

    def hsl_to_rgb_changed(self):
        h = float(self.HhslLine.text())
        s = float(self.ShslLine.text())
        l = float(self.LhslLine.text())
        rgb = self.hsl_to_rgb(h, s, l)
        cmyk = self.rgb_to_cmyk(rgb[0], rgb[1], rgb[2])
        hsv = self.rgb_to_hsv(rgb[0], rgb[1], rgb[2])
        ycrcb = self.rgb_to_ycrcb(rgb[0], rgb[1], rgb[2])
        lab = self.rgb_to_lab(rgb[0], rgb[1], rgb[2])
        self.r.setText(rgb[0].__str__())
        self.g.setText(rgb[1].__str__())
        self.b.setText(rgb[2].__str__())

        self.c.setText(cmyk[0].__str__())
        self.m.setText(cmyk[1].__str__())
        self.y.setText(cmyk[2].__str__())
        self.k.setText(cmyk[3].__str__())

        self.HhsvLine.setText(hsv[0].__str__())
        self.ShsvLine.setText(hsv[1].__str__())
        self.VhsvLine.setText(hsv[2].__str__())

        self.Ycr.setText(ycrcb[0].__str__())
        self.Cr.setText(ycrcb[1].__str__())
        self.Cb.setText(ycrcb[2].__str__())

        self.L.setText(lab[0].__str__())
        self.A.setText(lab[1].__str__())
        self.B.setText(lab[2].__str__())

    def lab_to_rgb_changed(self):
        l = float(self.L.text())
        a = float(self.A.text())
        b = float(self.B.text())
        rgb = self.lab_to_rgb(l, a, b)
        cmyk = self.rgb_to_cmyk(rgb[0], rgb[1], rgb[2])
        hsv = self.rgb_to_hsv(rgb[0], rgb[1], rgb[2])
        ycrcb = self.rgb_to_ycrcb(rgb[0], rgb[1], rgb[2])
        hsl = self.rgb_to_hsl(rgb[0], rgb[1], rgb[2])
        self.r.setText(rgb[0].__str__())
        self.g.setText(rgb[1].__str__())
        self.b.setText(rgb[2].__str__())

        self.c.setText(cmyk[0].__str__())
        self.m.setText(cmyk[1].__str__())
        self.y.setText(cmyk[2].__str__())
        self.k.setText(cmyk[3].__str__())

        self.HhsvLine.setText(hsv[0].__str__())
        self.ShsvLine.setText(hsv[1].__str__())
        self.VhsvLine.setText(hsv[2].__str__())

        self.Ycr.setText(ycrcb[0].__str__())
        self.Cr.setText(ycrcb[1].__str__())
        self.Cb.setText(ycrcb[2].__str__())

        self.HhslLine.setText(hsl[0].__str__())
        self.ShslLine.setText(hsl[1].__str__())
        self.LhslLine.setText(hsl[2].__str__())

    def ycrcb_to_rgb_changed(self):
        y = int(self.Ycr.text())
        cr = int(self.Cr.text())
        cb = int(self.Cb.text())
        rgb = self.ycbcr_to_rgb(y, cr, cb)
        cmyk = self.rgb_to_cmyk(rgb[0], rgb[1], rgb[2])
        hsv = self.rgb_to_hsv(rgb[0], rgb[1], rgb[2])
        lab = self.rgb_to_lab(rgb[0], rgb[1], rgb[2])
        hsl = self.rgb_to_hsl(rgb[0], rgb[1], rgb[2])
        self.r.setText(rgb[0].__str__())
        self.g.setText(rgb[1].__str__())
        self.b.setText(rgb[2].__str__())

        self.c.setText(cmyk[0].__str__())
        self.m.setText(cmyk[1].__str__())
        self.y.setText(cmyk[2].__str__())
        self.k.setText(cmyk[3].__str__())

        self.HhsvLine.setText(hsv[0].__str__())
        self.ShsvLine.setText(hsv[1].__str__())
        self.VhsvLine.setText(hsv[2].__str__())

        self.L.setText(lab[0].__str__())
        self.A.setText(lab[1].__str__())
        self.B.setText(lab[2].__str__())

        self.HhslLine.setText(hsl[0].__str__())
        self.ShslLine.setText(hsl[1].__str__())
        self.LhslLine.setText(hsl[2].__str__())

    def rgb_to_cmyk(self, red, green, blue):
        red = red / 255.0
        green = green / 255.0
        blue = blue / 255.0

        key = 1 - max(red, green, blue)
        cyan = (1 - red - key) / (1 - key)
        magenta = (1 - green - key) / (1 - key)
        yellow = (1 - blue - key) / (1 - key)

        return int(cyan * 100), int(magenta * 100), int(yellow * 100), int(key * 100)

    def cmyk_to_rgb(self, c, m, y, k):
        """Преобразование цвета из CMYK в RGB."""
        c = c / 100
        m = m / 100
        y = y / 100
        k = k / 100
        # Преобразование CMY для каждого компонента
        r = 1 - c * (1 - k)
        g = 1 - m * (1 - k)
        b = 1 - y * (1 - k)

        return math.ceil(r * 255), math.ceil(g * 255), math.ceil(b * 255)

    def rgb_to_hsv(self, r, g, b):
        # Нормализация значений RGB
        r, g, b = [x / 255. for x in [r, g, b]]

        # Нахождение минимального и максимального значений
        min_val = min(r, g, b)
        max_val = max(r, g, b)

        delta = max_val - min_val
        # Вычисление насыщенности и яркости
        s = delta / max_val if max_val > 0 else 0

        # Вычисление тона
        if max_val == min_val:
            h = 0.0
        elif max_val == r:
            h = (((g - b) / delta) % 6)
        elif max_val == g:
            h = ((b - r) / delta + 2)
        elif max_val == b:
            h = (r - g) / delta + 4
        h *= 60

        return math.ceil(h), math.ceil(s * 100), math.ceil(max_val * 100)

    def hsv_to_rgb(self, h, s, v):
        h = float(h)
        s = float(s) / 100
        v = float(v) / 100

        r, g, b = [0, 0, 0]

        if s == 0:
            r, g, b = v, v, v
        else:
            h = (h / 60) % 6
            i = int(h)
            f = h - i
            p = v * (1 - s)
            q = v * (1 - s * f)
            t = v * (1 - s * (1 - f))

            if i == 0:
                r, g, b = v, t, p
            elif i == 1:
                r, g, b = q, v, p
            elif i == 2:
                r, g, b = p, v, t
            elif i == 3:
                r, g, b = p, q, v
            elif i == 4:
                r, g, b = t, p, v
            elif i == 5:
                r, g, b = v, p, q

        return tuple(math.ceil(x * 255) for x in [r, g, b])

    def rgb_to_ycrcb(self, r, g, b):
        # Нормализуем значения RGB до диапазона [0, 1]
        r = r / 255.0
        g = g / 255.0
        b = b / 255.0

        # Применяем преобразования для получения Y, Cr и Cb
        y = 0.299 * r + 0.587 * g + 0.114 * b
        cr = 0.5 * r - 0.418688 * g - 0.081312 * b + 0.5
        cb = -0.168736 * r - 0.331264 * g + 0.5 * b + 0.5

        # Преобразуем значения обратно в диапазон [0, 255]
        y = round(y * 255)
        cr = round(cr * 255)
        cb = round(cb * 255)

        return y, cr, cb

    def ycbcr_to_rgb(self, y, cr, cb):
     r = y + 1.40200 * (cr - 128)
     g = y - 0.34414 * (cb - 128) - 0.71414 * (cr - 128)
     b = y + 1.77200 * (cb - 128)
     return math.ceil(r), math.ceil(g), math.ceil(b)

    def rgb_to_hsl(self, r, g, b):
        # Преобразование RGB в HSL
        r, g, b = r / 255.0, g / 255.0, b / 255.0
        min_value = min(r, g, b)
        max_value = max(r, g, b)
        delta = max_value - min_value
        l = (min_value + max_value) / 2
        if delta == 0:
            h = 0
            s = 0
        else:
            s = delta / (1 - abs(2 * l - 1))
            if l < 0.5:
                s = delta / (max_value + min_value)
            if r == g and g == b:
                h = 0
            elif r == max_value:
                h = (g - b) / delta
            elif g == max_value:
                h = 2 + (b - r) / delta
            else:
                h = 4 + (r - g) / delta
            h *= 60
            if h < 0:
                h += 360

        return math.ceil(h), math.ceil(s * 100), math.ceil(l * 100)

    def rgb_to_lab(self, r, g, b):
        r, g, b = [x / 255. for x in [r, g, b]]

        var_r, var_g, var_b = 100 * self.norm(r), 100* self.norm(g), 100 * self.norm(b),

        # Преобразование из RGB в XYZ
        x = (var_r * 0.412453 + var_g * 0.357580 + var_b * 0.180423)
        y = (var_r * 0.212671 + var_g * 0.715160 + var_b * 0.072169)
        z = (var_r * 0.019334 + var_g * 0.119193 + var_b * 0.950227)

        ref_x = 95.047
        ref_y = 100.000
        ref_z = 108.883

        # x = 4.950280289802328
        # y = 4.415476751814342
        # z = 27.025186241611866

        x /= ref_x
        y /= ref_y
        z /= ref_z



        # Преобразование из XYZ в LAB
        l = 116 * self.f_xyz(y) - 16
        a = 500 * (self.f_xyz(x) - self.f_xyz(y))
        b = 200 * (self.f_xyz(y) - self.f_xyz(z))

        # return x, y, z
        return round(l), round(a), round(b)

    def f_xyz(self, t):
        return t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16.0 / 116.0

    def norm(self, t):
        return ((t + 0.055) / 1.055) ** 2.4 if t > 0.045045 else t / 12.92

    def var_rgb(self, t):
        return 1.055 * (t ** (1 / 2.4)) - 0.055 if t > 0.0031308 else t * 12.92

    def var(self, t):
        return t ** 3 if t ** 3 > 0.008856 else (t - 16 / 116) / 7.787

    def lab_to_rgb(self, l, a, b):
        # lab to xyz
        var_Y = (l + 16) / 116
        var_X = a / 500 + var_Y
        var_Z = var_Y - b / 200

        var_X = self.var(var_X)
        var_Y = self.var(var_Y)
        var_Z = self.var(var_Z)

        ref_x = 95.047
        ref_y = 100.000
        ref_z = 108.883

        x = var_X * ref_x
        y = var_Y * ref_y
        z = var_Z * ref_z

        # xyz to rgb
        var_x = x / 100
        var_y = y / 100
        var_z = z / 100

        var_r = self.var_rgb(var_x * 3.2406 + var_y * -1.5372 + var_z * -0.4986)
        var_g = self.var_rgb(var_x * -0.9689 + var_y * 1.8758 + var_z * 0.0415)
        var_b = self.var_rgb(var_x * 0.0557 + var_y * -0.2040 + var_z * 1.0570)

        return round(var_r * 255), round(var_g * 255), round(var_b * 255)

    def hsl_to_rgb(self, h, s, l):
        # Нормализация значений H, S и L
        h = float(h) / 360.0
        s = max(0, min(s/100, 1))
        l = max(0, min(l/100, 1))

        # Расчет компонентов RGB
        if s == 0:
            r, g, b = l, l, l
        else:
            q = l * (1 + s) if l < 0.5 else l + s - l * s
            p = 2 * l - q

            r = int(self.hue_to_rgb(p, q, h + 1.0 / 3) * 255)
            g = int(self.hue_to_rgb(p, q, h) * 255)
            b = int(self.hue_to_rgb(p, q, h - 1.0 / 3) * 255)

        return r, g, b

    def hue_to_rgb(self, p, q, t):
     if t < 0:
      t += 1
     if t > 1:
      t -= 1
     if t < 1 / 6:
      return p + (q - p) * 6 * t
     if t < 1 / 2:
      return q
     if t < 2 / 3:
      return p + (q - p) * (2 / 3 - t) * 6
     return p




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
