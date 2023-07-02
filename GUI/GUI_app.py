from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.verticalLayout.addWidget(self.lineEdit_1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.pbtrand = QtWidgets.QPushButton(self.widget)
        self.pbtrand.setObjectName("pbtrand")
        self.verticalLayout.addWidget(self.pbtrand)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_2.addWidget(self.lineEdit_7)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.pbtfile = QtWidgets.QPushButton(self.widget)
        self.pbtfile.setObjectName("pbtfile")
        self.verticalLayout_2.addWidget(self.pbtfile)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_3.addWidget(self.lineEdit_11)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_3.addWidget(self.lineEdit_9)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_3.addWidget(self.lineEdit_10)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.pbtinput = QtWidgets.QPushButton(self.widget)
        self.pbtinput.setObjectName("pbtinput")
        self.verticalLayout_3.addWidget(self.pbtinput)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_4.addWidget(self.textEdit)
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SP"))
        self.label.setText(_translate("MainWindow", "A Min"))
        self.label_2.setText(_translate("MainWindow", "B Min"))
        self.label_3.setText(_translate("MainWindow", "C Min"))
        self.label_4.setText(_translate("MainWindow", "D Min"))
        self.pbtrand.setText(_translate("MainWindow", "random"))
        self.label_5.setText(_translate("MainWindow", "A Max"))
        self.label_6.setText(_translate("MainWindow", "B Max"))
        self.label_7.setText(_translate("MainWindow", "C Max"))
        self.label_8.setText(_translate("MainWindow", "D Max"))
        self.pbtfile.setText(_translate("MainWindow", "file"))
        self.label_9.setText(_translate("MainWindow", "Count of Points"))
        self.label_12.setText(_translate("MainWindow", "Size of Swarm"))
        self.label_10.setText(_translate("MainWindow", "Number of Iterations"))
        self.label_11.setText(_translate("MainWindow", "Rating Coefficient"))
        self.pbtinput.setText(_translate("MainWindow", "input"))


class MplCanvas(FigureCanvas):
    def __init__(self, *args, **kwargs):
        self.fig = Figure()
        super(MplCanvas, self).__init__(self.fig, *args, **kwargs)

    def plot(self, x, y):
        self.fig.clear()
        self.ax = self.fig.add_subplot(111)
        self.ax.plot(x, y, linewidth=1)
        print(y)
        self.ax.legend()
        self.draw()


class UI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.setupUi(self)
        self.defaultState()
        self.pbtrand.clicked.connect(self.plot_graph)
        self.pbtfile.clicked.connect(self.plot_graph)
        self.pbtinput.clicked.connect(self.plot_graph)
        self.canavas = MplCanvas()
        self.canavas.setMinimumSize(300, 300)
        self.verticalLayout_4.addWidget(self.canavas)

    def defaultState(self):
        self.lineEdit.setText("35")
        self.lineEdit_1.setText("-100")
        self.lineEdit_2.setText("-100")
        self.lineEdit_3.setText("-100")
        self.lineEdit_4.setText("-100")
        self.lineEdit_5.setText("100")
        self.lineEdit_6.setText("100")
        self.lineEdit_7.setText("100")
        self.lineEdit_8.setText("100")

    def plot_graph(self):
        sender = self.sender()
        if sender == self.pbtfile:
            return
        elif sender == self.pbtrand:
            max_val = np.zeros(4)
            min_val = np.zeros(4)
            size = 0
            try:
                min_val[0] = float(self.lineEdit_1.text())
            except:
                self.Message(2, 'A Min')
                return
            try:
                max_val[0] = float(self.lineEdit_5.text())
            except:
                self.Message(2, 'A Max')
                return
            if min_val[0] >= max_val[0]:
                self.Message(3, 'A')
                return

            try:
                min_val[1] = float(self.lineEdit_2.text())
            except:
                self.Message(2, 'B Min')
                return
            try:
                max_val[1] = float(self.lineEdit_6.text())
            except:
                self.Message(2, 'B Max')
                return
            if min_val[1] >= max_val[1]:
                self.Message(3, 'B')
                return

            try:
                min_val[2] = float(self.lineEdit_3.text())
            except:
                self.Message(2, 'C Min')
                return
            try:
                max_val[2] = float(self.lineEdit_7.text())
            except:
                self.Message(2, 'C Max')
                return
            if min_val[2] >= max_val[2]:
                self.Message(3, 'C')
                return

            try:
                min_val[3] = float(self.lineEdit_4.text())
            except:
                self.Message(2, 'D Min')
                return
            try:
                max_val[3] = float(self.lineEdit_8.text())
            except:
                self.Message(2, 'D Max')
                return
            if min_val[3] >= max_val[3]:
                self.Message(3, 'D')
                return

            if self.lineEdit.text().isdigit():
                size = int(self.lineEdit.text())
            else:
                self.Message(1)
                return
        else:
            self.Message(0)
            return

        def f(x): return min_val[0]*(x**3) + \
            min_val[1]*(x**2) + min_val[2]*x + min_val[3]
        x = list(range(0, 100))
        y = [f(i) for i in x]
        self.canavas.plot(x, y)

    def Message(self, ind, text=''):
        if ind == 0:
            text = "В большом поле записываются значения координат точек функции, к которой стримится функция, в формате \{X1 Y1, X2 Y2, ..., Xn Yn\}. Целую от нецелой части числа разделяет точка."
        elif ind == 1:
            text = "В поле 'size' записывется количество точек для оценки. Число должно быть целым и не менее 2."
        elif ind == 2:
            text = "В ячейке '{}' должно хронится действительное число. Целую от нецелой части числа должно отделять точка.".format(
                text)
        else:
            text = "Значение '{} Min' должно быть меньше значения в '{} Max'".format(
                text)

        QtWidgets.QMessageBox.question(
            self, 'ОШИБКА!', text, QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UI()
    ui.show()
    sys.exit(app.exec_())
