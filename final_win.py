from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
QApplication, QWidget,
QHBoxLayout, QVBoxLayout, QGridLayout,
QGroupBox, QRadioButton,
QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *

class FinalWin(QWidget):
	def __init__(self, exp, age):
		super().__init__()
		self.exp = exp
		print(exp)
		self.age = age
		self.initUI()
		self.set_appear()
		self.show()

	def results(self):
		if self.age < 7:
			return "нет данных для такого возраста"

		if self.age == 7 or self.age == 8:
			if self.exp >= 21:
				return txt_res1
			elif self.exp < 21 and self.exp >= 17:
				return txt_res2
			elif self.exp < 17 and self.exp >= 12:
				return txt_res3
			elif self.exp < 12 and self.exp >= 6.5:
				return txt_res4
			else:
				return txt_res5

		if self.age == 9 or self.age == 10:
			if self.exp >= 19.5:
				return txt_res1
			elif self.exp < 19.5 and self.exp >= 15.5:
				return txt_res2
			elif self.exp < 15.5 and self.exp >= 10.5:
				return txt_res3
			elif self.exp < 10.5 and self.exp >= 5:
				return txt_res4
			else:
				return txt_res5

		if self.age == 11 or self.age == 12:
			if self.exp >= 18:
				return txt_res1
			elif self.exp < 18 and self.exp >= 14:
				return txt_res2
			elif self.exp < 14 and self.exp >= 9:
				return txt_res3
			elif self.exp < 9 and self.exp >= 3.5:
				return txt_res4
			else:
				return txt_res5

		if self.age == 13 or self.age == 14:
			if self.exp>= 16.5:
				return txt_res1
			elif self.exp< 16.5 and self.exp>= 12.5:
				return txt_res2
			elif self.exp< 12.5 and self.exp>= 7.5:
				return txt_res3
			elif self.exp< 7.5 and self.exp>= 2:
				return txt_res4
			else:
				return txt_res5

		if self.age >= 15:
			if self.exp>= 15:
				return txt_res1
			elif self.exp< 15 and self.exp>= 11:
				return txt_res2
			elif self.exp< 11 and self.exp>= 6:
				return txt_res3
			elif self.exp< 6 and self.exp>= 0.5:
				return txt_res4
			else:
				return txt_res5

	def initUI(self):
		self.index_text = QLabel(txt_index + str(self.exp))
		self.work_text = QLabel(txt_workheart + self.results())
		
		self.layout_line = QVBoxLayout()
		self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
		self.layout_line.addWidget(self.work_text, alignment = Qt.AlignCenter)
		self.setLayout(self.layout_line)

	def set_appear(self):
		self.setWindowTitle(txt_finalwin)
		self.resize(win_width, win_height)
		self.move(win_x, win_y)