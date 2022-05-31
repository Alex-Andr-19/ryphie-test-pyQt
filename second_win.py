from time import time

from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
QApplication, QWidget,
QHBoxLayout, QVBoxLayout, QGridLayout,
QGroupBox, QRadioButton,
QPushButton, QLabel, QListWidget, QLineEdit)

from final_win import *
from instr import *


class SecondWin(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
		self.set_appear()
		self.connects()
		self.show()

		self.res = 0
		self.timer = [15, 45, 60]

		self.q_timer = QTimer(self)
		self.q_timer.timeout.connect(self.showTime)
		self.q_timer.start(1000)

		self.test_num = -1

	def create_main_layout(self):
		layout = QHBoxLayout()
		first_layout = QVBoxLayout()
		second_layout = QVBoxLayout()

		first_layout.addWidget(self.l[0])
		first_layout.addWidget(self.le[0])
		first_layout.addWidget(self.l[1])
		first_layout.addWidget(self.le[1])
		first_layout.addWidget(self.l[2])
		first_layout.addWidget(self.b[0])
		first_layout.addWidget(self.le[2])
		first_layout.addWidget(self.l[3])
		first_layout.addWidget(self.b[1])
		first_layout.addWidget(self.l[4])
		first_layout.addWidget(self.b[2])
		first_layout.addWidget(self.le[3])
		first_layout.addWidget(self.le[4])
		first_layout.addWidget(self.b[3])

		second_layout.addWidget(self.l[5])

		layout.addLayout(first_layout)
		layout.addLayout(second_layout)

		return layout

	def set_appear(self): 
		self.setWindowTitle(txt_title)
		self.resize(win_width, win_height)
		self.move(win_x, win_y)

	def initUI(self): 
		self.l = [
			QLabel(txt_name, alignment = Qt.AlignLeft), 
			QLabel(txt_hintage, alignment = Qt.AlignLeft), 
			QLabel(txt_test1, alignment = Qt.AlignLeft), 
			QLabel(txt_test2, alignment = Qt.AlignLeft), 
			QLabel(txt_test3, alignment = Qt.AlignLeft),
			QLabel("00:00:15")
		]

		self.b = [
			QPushButton(txt_starttest1), 
			QPushButton(txt_starttest2), 
			QPushButton(txt_starttest3), 
			QPushButton(txt_sendresults)
		]

		self.le = [
			QLineEdit(txt_hintname), 
			QLineEdit(txt_age), 
			QLineEdit(txt_age), 
			QLineEdit(txt_age), 
			QLineEdit(txt_age)
		]

		self.main_layout = QVBoxLayout()
		self.main_layout.addLayout(self.create_main_layout())

		self.setLayout(self.main_layout)

	def connects(self):
		self.b[0].clicked.connect(self.start_first_test)
		self.b[1].clicked.connect(self.start_phisical_ex)
		self.b[2].clicked.connect(self.start_final_test)
		self.b[3].clicked.connect(self.next_click)

	def add_zero(self, num):
		res = str(num)
		if num < 10:
			res = "0" + res
		return res

	def set_true_time(self, test_num):
		if self.timer[test_num] >= 0:
			self.l[5].setText(f"00:{self.add_zero(self.timer[test_num]//60)}:{self.add_zero(self.timer[test_num]%60)}")
			self.timer[test_num] -= 1

	def showTime(self):
		if self.test_num >= 0:
			self.set_true_time(self.test_num)

	def start_first_test(self):
		self.test_num = 0

	def start_phisical_ex(self):
		self.test_num = 1

	def start_final_test(self):
		self.test_num = 2

	def calculate(self):
		summ = float(self.le[2].text()) + float(self.le[3].text()) + float(self.le[4].text())
		self.res = (4*summ - 200)/10

	def next_click(self):
		age = int(self.le[1].text())
		self.calculate()
		print(self.res)
		self.hide()
		self.tw = FinalWin(self.res, age)