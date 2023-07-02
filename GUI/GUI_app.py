# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_b_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.figure import Figure


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(447, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(11, 11, 423, 611))
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.verticalLayout_5.addWidget(self.lineEdit_1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_5.addWidget(self.lineEdit_3)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_5.addWidget(self.lineEdit_4)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_6.addWidget(self.lineEdit_5)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_6.addWidget(self.lineEdit_6)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_6.addWidget(self.lineEdit_7)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_6.addWidget(self.lineEdit_8)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 70))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pbtrand = QtWidgets.QPushButton(self.widget)
        self.pbtrand.setObjectName("pbtrand")
        self.verticalLayout_2.addWidget(self.pbtrand)
        self.pbtfile = QtWidgets.QPushButton(self.widget)
        self.pbtfile.setObjectName("pbtfile")
        self.verticalLayout_2.addWidget(self.pbtfile)
        self.pbtinput = QtWidgets.QPushButton(self.widget)
        self.pbtinput.setObjectName("pbtinput")
        self.verticalLayout_2.addWidget(self.pbtinput)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_4.addWidget(self.textEdit)
        self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_4.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_1, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        MainWindow.setTabOrder(self.lineEdit_6, self.lineEdit_7)
        MainWindow.setTabOrder(self.lineEdit_7, self.lineEdit_8)
        MainWindow.setTabOrder(self.lineEdit_8, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.textEdit)
        MainWindow.setTabOrder(self.textEdit, self.pbtrand)
        MainWindow.setTabOrder(self.pbtrand, self.pbtfile)
        MainWindow.setTabOrder(self.pbtfile, self.pbtinput)
        MainWindow.setTabOrder(self.pbtinput, self.graphicsView)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "A Min"))
        self.label_2.setText(_translate("MainWindow", "B Min"))
        self.label_3.setText(_translate("MainWindow", "C Min"))
        self.label_4.setText(_translate("MainWindow", "D Min"))
        self.label_5.setText(_translate("MainWindow", "A Max"))
        self.label_6.setText(_translate("MainWindow", "B Max"))
        self.label_7.setText(_translate("MainWindow", "C Max"))
        self.label_8.setText(_translate("MainWindow", "D Max"))
        self.label_9.setText(_translate("MainWindow", "Size"))
        self.pbtrand.setText(_translate("MainWindow", "random"))
        self.pbtfile.setText(_translate("MainWindow", "file"))
        self.pbtinput.setText(_translate("MainWindow", "input"))


class MplCanvas(FigureCanvas):      # класс для построения графика в окне интерфейса
    def __init__(self, *args, **kwargs):
        self.fig = Figure()
        super(MplCanvas, self).__init__(self.fig, *args, **kwargs)

    def plot(self, x, y):       # функция для отрисовки графика
        self.fig.clear()        # очистка поля для построения
        self.ax = self.fig.add_subplot(111)
        self.ax.plot(x, y, color="darkmagenta", label="y(x)", linewidth=2)      # оформление графика
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("f(x)")
        self.ax.legend()
        self.ax.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
        self.draw()

class TEST(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(TEST, self).__init__()
        self.setupUi(self)
        self.pbtrand.clicked.connect(self.plot_graph)      # обработка нажатия на кнопку построения графика
        self.canavas = MplCanvas()
        self.canavas.setMinimumSize(300, 300)
        # self.toolbar = NavigationToolbar(self.canavas, self)
        self.verticalLayout.addWidget(self.canavas)
        # self.verticalLayout.addWidget(self.toolbar)
        # self.toolbar.hide()
        # self.setStyleSheet('.QWidget {background-image: url(v1.jpg);}')

    def plot_graph(self):
        # print("YESSSSSSS")
        # self.lineEdit._rise()
        # self.lineEdit_2._rise()
        # self.lineEdit_3._rise()
        # self.lineEdit_4._rise()
        # reply = QtWidgets.QMessageBox.question(self, 'Message',
        # "Are you sure to quit?" + self.lineEdit.text(), QtWidgets.QMessageBox.Yes |
        # QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        # a = float(self.lineEdit.text())   
        # b = float(self.lineEdit_2.text())
        # c = float(self.lineEdit_3.text())
        # d = float(self.lineEdit_4.text())
        a, b, c, d =1, 1, 1, 1
        f = lambda x: a*(x**3) + b*(x**2) + c*x + d
        x = list(range(0, 100))
        y = [f(i) for i in x]
        self.canavas.plot(x, y)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = TEST()
    ui.show()
    sys.exit(app.exec_())
