from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(11, 20, 610, 531))
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.A_Min = QtWidgets.QLineEdit(self.widget)
        self.A_Min.setMinimumSize(QtCore.QSize(133, 20))
        self.A_Min.setMaximumSize(QtCore.QSize(133, 20))
        self.A_Min.setObjectName("A_Min")
        self.verticalLayout.addWidget(self.A_Min)
        self.A_Min_label = QtWidgets.QLabel(self.widget)
        self.A_Min_label.setEnabled(True)
        self.A_Min_label.setMinimumSize(QtCore.QSize(0, 14))
        self.A_Min_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.A_Min_label.setObjectName("A_Min_label")
        self.verticalLayout.addWidget(self.A_Min_label)
        self.B_Min = QtWidgets.QLineEdit(self.widget)
        self.B_Min.setMinimumSize(QtCore.QSize(133, 20))
        self.B_Min.setMaximumSize(QtCore.QSize(133, 20))
        self.B_Min.setObjectName("B_Min")
        self.verticalLayout.addWidget(self.B_Min)
        self.B_Min_label = QtWidgets.QLabel(self.widget)
        self.B_Min_label.setMinimumSize(QtCore.QSize(0, 14))
        self.B_Min_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.B_Min_label.setObjectName("B_Min_label")
        self.verticalLayout.addWidget(self.B_Min_label)
        self.C_Min = QtWidgets.QLineEdit(self.widget)
        self.C_Min.setMinimumSize(QtCore.QSize(133, 20))
        self.C_Min.setMaximumSize(QtCore.QSize(133, 20))
        self.C_Min.setObjectName("C_Min")
        self.verticalLayout.addWidget(self.C_Min)
        self.C_Min_label = QtWidgets.QLabel(self.widget)
        self.C_Min_label.setMinimumSize(QtCore.QSize(0, 14))
        self.C_Min_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.C_Min_label.setObjectName("C_Min_label")
        self.verticalLayout.addWidget(self.C_Min_label)
        self.D_Min = QtWidgets.QLineEdit(self.widget)
        self.D_Min.setMinimumSize(QtCore.QSize(133, 20))
        self.D_Min.setMaximumSize(QtCore.QSize(133, 20))
        self.D_Min.setObjectName("D_Min")
        self.verticalLayout.addWidget(self.D_Min)
        self.D_Min_label = QtWidgets.QLabel(self.widget)
        self.D_Min_label.setMinimumSize(QtCore.QSize(0, 14))
        self.D_Min_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.D_Min_label.setObjectName("D_Min_label")
        self.verticalLayout.addWidget(self.D_Min_label)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.A_Max = QtWidgets.QLineEdit(self.widget)
        self.A_Max.setMinimumSize(QtCore.QSize(133, 20))
        self.A_Max.setMaximumSize(QtCore.QSize(133, 20))
        self.A_Max.setObjectName("A_Max")
        self.verticalLayout_2.addWidget(self.A_Max)
        self.A_Max_label = QtWidgets.QLabel(self.widget)
        self.A_Max_label.setMinimumSize(QtCore.QSize(0, 14))
        self.A_Max_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.A_Max_label.setObjectName("A_Max_label")
        self.verticalLayout_2.addWidget(self.A_Max_label)
        self.B_Max = QtWidgets.QLineEdit(self.widget)
        self.B_Max.setMinimumSize(QtCore.QSize(133, 20))
        self.B_Max.setMaximumSize(QtCore.QSize(133, 20))
        self.B_Max.setObjectName("B_Max")
        self.verticalLayout_2.addWidget(self.B_Max)
        self.B_Max_label = QtWidgets.QLabel(self.widget)
        self.B_Max_label.setMinimumSize(QtCore.QSize(0, 14))
        self.B_Max_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.B_Max_label.setObjectName("B_Max_label")
        self.verticalLayout_2.addWidget(self.B_Max_label)
        self.C_Max = QtWidgets.QLineEdit(self.widget)
        self.C_Max.setMinimumSize(QtCore.QSize(133, 20))
        self.C_Max.setMaximumSize(QtCore.QSize(133, 20))
        self.C_Max.setObjectName("C_Max")
        self.verticalLayout_2.addWidget(self.C_Max)
        self.C_Max_label = QtWidgets.QLabel(self.widget)
        self.C_Max_label.setMinimumSize(QtCore.QSize(0, 14))
        self.C_Max_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.C_Max_label.setObjectName("C_Max_label")
        self.verticalLayout_2.addWidget(self.C_Max_label)
        self.D_Max = QtWidgets.QLineEdit(self.widget)
        self.D_Max.setMinimumSize(QtCore.QSize(133, 20))
        self.D_Max.setMaximumSize(QtCore.QSize(133, 20))
        self.D_Max.setObjectName("D_Max")
        self.verticalLayout_2.addWidget(self.D_Max)
        self.D_Max_label = QtWidgets.QLabel(self.widget)
        self.D_Max_label.setMinimumSize(QtCore.QSize(0, 14))
        self.D_Max_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.D_Max_label.setObjectName("D_Max_label")
        self.verticalLayout_2.addWidget(self.D_Max_label)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Swarm = QtWidgets.QSpinBox(self.widget)
        self.Swarm.setMinimumSize(QtCore.QSize(133, 20))
        self.Swarm.setMaximumSize(QtCore.QSize(133, 20))
        self.Swarm.setMinimum(2)
        self.Swarm.setMaximum(10000)
        self.Swarm.setObjectName("Swarm")
        self.verticalLayout_3.addWidget(self.Swarm)
        self.Swarm_label = QtWidgets.QLabel(self.widget)
        self.Swarm_label.setMinimumSize(QtCore.QSize(0, 14))
        self.Swarm_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.Swarm_label.setObjectName("Swarm_label")
        self.verticalLayout_3.addWidget(self.Swarm_label)
        self.Iterations = QtWidgets.QSpinBox(self.widget)
        self.Iterations.setMinimumSize(QtCore.QSize(133, 20))
        self.Iterations.setMaximumSize(QtCore.QSize(133, 20))
        self.Iterations.setMinimum(1)
        self.Iterations.setMaximum(10000)
        self.Iterations.setObjectName("Iterations")
        self.verticalLayout_3.addWidget(self.Iterations)
        self.Iterations_label = QtWidgets.QLabel(self.widget)
        self.Iterations_label.setMinimumSize(QtCore.QSize(0, 14))
        self.Iterations_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.Iterations_label.setObjectName("Iterations_label")
        self.verticalLayout_3.addWidget(self.Iterations_label)
        self.Rating_Coef = QtWidgets.QDoubleSpinBox(self.widget)
        self.Rating_Coef.setMinimumSize(QtCore.QSize(133, 0))
        self.Rating_Coef.setMaximumSize(QtCore.QSize(133, 20))
        self.Rating_Coef.setObjectName("Rating_Coef")
        self.verticalLayout_3.addWidget(self.Rating_Coef)
        self.Rating_Coef_label = QtWidgets.QLabel(self.widget)
        self.Rating_Coef_label.setMinimumSize(QtCore.QSize(0, 14))
        self.Rating_Coef_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.Rating_Coef_label.setObjectName("Rating_Coef_label")
        self.verticalLayout_3.addWidget(self.Rating_Coef_label)
        self.pbt_iter = QtWidgets.QPushButton(self.widget)
        self.pbt_iter.setMinimumSize(QtCore.QSize(133, 0))
        self.pbt_iter.setMaximumSize(QtCore.QSize(133, 20))
        self.pbt_iter.setObjectName("pbt_iter")
        self.verticalLayout_3.addWidget(self.pbt_iter)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.GWC = QtWidgets.QDoubleSpinBox(self.widget)
        self.GWC.setMinimumSize(QtCore.QSize(133, 0))
        self.GWC.setMaximumSize(QtCore.QSize(133, 20))
        self.GWC.setObjectName("GWC")
        self.verticalLayout_4.addWidget(self.GWC)
        self.GWC_label = QtWidgets.QLabel(self.widget)
        self.GWC_label.setMinimumSize(QtCore.QSize(0, 14))
        self.GWC_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.GWC_label.setObjectName("GWC_label")
        self.verticalLayout_4.addWidget(self.GWC_label)
        self.LWC = QtWidgets.QDoubleSpinBox(self.widget)
        self.LWC.setMinimumSize(QtCore.QSize(133, 0))
        self.LWC.setMaximumSize(QtCore.QSize(133, 20))
        self.LWC.setObjectName("LWC")
        self.verticalLayout_4.addWidget(self.LWC)
        self.LWC_label = QtWidgets.QLabel(self.widget)
        self.LWC_label.setMinimumSize(QtCore.QSize(0, 14))
        self.LWC_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.LWC_label.setObjectName("LWC_label")
        self.verticalLayout_4.addWidget(self.LWC_label)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pbt_rand = QtWidgets.QPushButton(self.widget)
        self.pbt_rand.setObjectName("pbt_rand")
        self.horizontalLayout_3.addWidget(self.pbt_rand)
        self.pbt_input = QtWidgets.QPushButton(self.widget)
        self.pbt_input.setObjectName("pbt_input")
        self.horizontalLayout_3.addWidget(self.pbt_input)
        self.pbt_file = QtWidgets.QPushButton(self.widget)
        self.pbt_file.setObjectName("pbt_file")
        self.horizontalLayout_3.addWidget(self.pbt_file)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        '''self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView.setMinimumSize(QtCore.QSize(300, 300))
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_4.addWidget(self.graphicsView)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView_2.setMinimumSize(QtCore.QSize(300, 300))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_4.addWidget(self.graphicsView_2)'''
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.A_Min, self.B_Min)
        MainWindow.setTabOrder(self.B_Min, self.C_Min)
        MainWindow.setTabOrder(self.C_Min, self.D_Min)
        MainWindow.setTabOrder(self.D_Min, self.A_Max)
        MainWindow.setTabOrder(self.A_Max, self.B_Max)
        MainWindow.setTabOrder(self.B_Max, self.C_Max)
        MainWindow.setTabOrder(self.C_Max, self.D_Max)
        MainWindow.setTabOrder(self.D_Max, self.pbt_rand)
        MainWindow.setTabOrder(self.pbt_rand, self.pbt_file)
        MainWindow.setTabOrder(self.pbt_file, self.pbt_input)
        # MainWindow.setTabOrder(self.pbt_input, self.graphicsView)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Swarm Alg"))
        self.A_Min_label.setText(_translate("MainWindow", "A Min"))
        self.B_Min_label.setText(_translate("MainWindow", "B Min"))
        self.C_Min_label.setText(_translate("MainWindow", "C Min"))
        self.D_Min_label.setText(_translate("MainWindow", "D Min"))
        self.A_Max_label.setText(_translate("MainWindow", "A Max"))
        self.B_Max_label.setText(_translate("MainWindow", "B Max"))
        self.C_Max_label.setText(_translate("MainWindow", "C Max"))
        self.D_Max_label.setText(_translate("MainWindow", "D Max"))
        self.Swarm_label.setText(_translate("MainWindow", "Size of Swarm"))
        self.Iterations_label.setText(_translate(
            "MainWindow", "Number of Iterations"))
        self.Rating_Coef_label.setText(
            _translate("MainWindow", "Rating Coefficient"))
        self.pbt_iter.setText(_translate("MainWindow", "make iterations"))
        self.GWC_label.setText(_translate(
            "MainWindow", "Global Weight Coefficient"))
        self.LWC_label.setText(_translate(
            "MainWindow", "Local Weight Coefficient"))
        self.pbt_rand.setText(_translate("MainWindow", "random data"))
        self.pbt_input.setText(_translate("MainWindow", "input data"))
        self.pbt_file.setText(_translate("MainWindow", "file"))


class MplCanvas(FigureCanvas):
    def __init__(self, *args, **kwargs):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig, *args, **kwargs)

    def plot_func(self, x, y):
        self.ax.plot(x, y, linewidth=1)

    def plot_dots(self, x, y):
        self.ax.scatter(x, y, marker='o', s=1)

    def clear(self):
        self.fig.clear()
        self.ax = self.fig.add_subplot(111)


class UI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, facade):
        super(UI, self).__init__()
        self.setupUi(self)
        self.defaultState()
        self.facade = facade
        self.dialogRand = DialogRandom(self)
        self.dialogInput = DialogInput(self)
        self.pbt_rand.clicked.connect(self.dialogRand.open)
        self.pbt_file.clicked.connect(self.open_file)
        self.pbt_input.clicked.connect(self.dialogInput.open)
        self.canavas_1 = MplCanvas()
        self.canavas_1.setMinimumSize(300, 300)
        self.canavas_2 = MplCanvas()
        self.canavas_2.setMinimumSize(300, 300)
        self.horizontalLayout_4.addWidget(self.canavas_1)
        self.horizontalLayout_4.addWidget(self.canavas_2)

    def defaultState(self):
        self.A_Min.setText("-100")
        self.B_Min.setText("-100")
        self.C_Min.setText("-100")
        self.D_Min.setText("-100")
        self.A_Max.setText("100")
        self.B_Max.setText("100")
        self.C_Max.setText("100")
        self.D_Max.setText("100")
        self.Swarm.setValue(100)
        self.Iterations.setValue(10)
        self.Rating_Coef.setValue(0.1)
        self.GWC.setValue(0.5)
        self.LWC.setValue(0.5)

    def plot_func(self, args: np.ndarray, x, y):
        assert len(x) == len(y)
        assert len(args) == 4
        self.canavas_1.clear()
        self.canavas_1.plot_dots(x, y)
        def f(x): return args[0]*(x**3) + args[1]*(x**2) + args[2]*x + args[3]
        x = list(range(int(min(x)) - 1, int(max(x)) + 1))
        y = [f(i) for i in x]
        self.canavas_1.plot_func(x, y)
        self.canavas_1.draw()

    def plot_mean_deviation_change(self, x, y):
        assert len(x) == len(y)
        self.canavas_2.clear()
        self.canavas_2.plot_func(x, y)
        self.canavas_2.show()

    def message(self, text=''):
        QtWidgets.QMessageBox.question(
            self, 'ОШИБКА!', text, QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def open_file(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open File', './', 'Text file (*.txt)')
        if file:
            try:
                self.facade.file_swarm(file)
            except ValueError:
                e = sys.exc_info()[1]
                self.message(e.args[0])


class DialogRandom(QtWidgets.QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.root = root
        self.setWindowTitle("Random")
        label = QtWidgets.QLabel('Number of Points')
        self.Size = QtWidgets.QSpinBox()
        self.Size.setMaximum(10000)
        self.Size.setMinimum(1)
        button = QtWidgets.QPushButton('next')
        button.clicked.connect(self.next)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.Size)
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)

    def next(self):
        list_val = [self.root.A_Min.text(),
                    self.root.B_Min.text(),
                    self.root.C_Min.text(),
                    self.root.D_Min.text(),
                    self.root.A_Max.text(),
                    self.root.B_Max.text(),
                    self.root.C_Max.text(),
                    self.root.D_Max.text(),
                    self.root.GWC.value(),
                    self.root.LWC.value(),
                    self.root.Swarm.value(),
                    self.root.Iterations.value(),
                    self.root.Rating_Coef.value(),
                    self.Size.value()]
        self.close()
        try:
            self.root.facade.random_swarm(list_val)
        except ValueError:
            e = sys.exc_info()[1]
            self.root.message(e.args[0])


class DialogInput(QtWidgets.QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.root = root
        # self.setWindowTitle("Input")
        self.setStatusTip("Input")
        label = QtWidgets.QLabel('Dots')
        self.Dots = QtWidgets.QTextEdit()
        self.pbtnext = QtWidgets.QPushButton('next')
        self.pbtsave = QtWidgets.QPushButton('save')
        self.pbtnext.clicked.connect(self.next)
        self.pbtsave.clicked.connect(self.next)
        button_panel = QtWidgets.QHBoxLayout()
        button_panel.addWidget(self.pbtnext)
        button_panel.addWidget(self.pbtsave)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.Dots)
        layout.addWidget(label)
        layout.addLayout(button_panel)
        self.setLayout(layout)

    def next(self):
        list_val = [self.root.A_Min.text(),
                    self.root.B_Min.text(),
                    self.root.C_Min.text(),
                    self.root.D_Min.text(),
                    self.root.A_Max.text(),
                    self.root.B_Max.text(),
                    self.root.C_Max.text(),
                    self.root.D_Max.text(),
                    self.root.GWC.value(),
                    self.root.LWC.value(),
                    self.root.Swarm.value(),
                    self.root.Iterations.value(),
                    self.root.Rating_Coef.value(),
                    self.Dots.toPlainText()]
        try:
            if self.sender() == self.pbtnext:
                self.close()
                self.root.facade.input_swarm(list_val)
            else:
                file, _ = QtWidgets.QFileDialog.getSaveFileName(
                    self, 'Save File', './', 'Text file (*.txt)')
                if file:
                    self.root.facade.save_file(list_val, file)
        except ValueError:
            e = sys.exc_info()[1]
            self.root.message(e.args[0])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UI(None)
    ui.show()
    sys.exit(app.exec_())
