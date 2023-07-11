from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStatusBar
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(636, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(11, 20, 610, 531))
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.aMin = QtWidgets.QLineEdit(self.widget)
        self.aMin.setMinimumSize(QtCore.QSize(133, 20))
        self.aMin.setMaximumSize(QtCore.QSize(133, 20))
        self.verticalLayout.addWidget(self.aMin)
        self.aMin_label = QtWidgets.QLabel(self.widget)
        self.aMin_label.setEnabled(True)
        self.aMin_label.setMinimumSize(QtCore.QSize(0, 14))
        self.aMin_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.verticalLayout.addWidget(self.aMin_label)
        self.bMin = QtWidgets.QLineEdit(self.widget)
        self.bMin.setMinimumSize(QtCore.QSize(133, 20))
        self.bMin.setMaximumSize(QtCore.QSize(133, 20))
        self.verticalLayout.addWidget(self.bMin)
        self.bMin_label = QtWidgets.QLabel(self.widget)
        self.bMin_label.setMinimumSize(QtCore.QSize(0, 14))
        self.bMin_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.verticalLayout.addWidget(self.bMin_label)
        self.cMin = QtWidgets.QLineEdit(self.widget)
        self.cMin.setMinimumSize(QtCore.QSize(133, 20))
        self.cMin.setMaximumSize(QtCore.QSize(133, 20))
        self.verticalLayout.addWidget(self.cMin)
        self.cMin_label = QtWidgets.QLabel(self.widget)
        self.cMin_label.setMinimumSize(QtCore.QSize(0, 14))
        self.cMin_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.verticalLayout.addWidget(self.cMin_label)
        self.dMin = QtWidgets.QLineEdit(self.widget)
        self.dMin.setMinimumSize(QtCore.QSize(133, 20))
        self.dMin.setMaximumSize(QtCore.QSize(133, 20))
        self.verticalLayout.addWidget(self.dMin)
        self.dMin_label = QtWidgets.QLabel(self.widget)
        self.dMin_label.setMinimumSize(QtCore.QSize(0, 14))
        self.dMin_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.verticalLayout.addWidget(self.dMin_label)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.aMax = QtWidgets.QLineEdit(self.widget)
        self.aMax.setMinimumSize(QtCore.QSize(133, 20))
        self.aMax.setMaximumSize(QtCore.QSize(133, 20))
        self.verticalLayout_2.addWidget(self.aMax)
        self.aMax_label = QtWidgets.QLabel(self.widget)
        self.aMax_label.setMinimumSize(QtCore.QSize(0, 14))
        self.aMax_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.verticalLayout_2.addWidget(self.aMax_label)
        self.bMax = QtWidgets.QLineEdit(self.widget)
        self.bMax.setMinimumSize(QtCore.QSize(133, 20))
        self.bMax.setMaximumSize(QtCore.QSize(133, 20))
        self.verticalLayout_2.addWidget(self.bMax)
        self.bMax_label = QtWidgets.QLabel(self.widget)
        self.bMax_label.setMinimumSize(QtCore.QSize(0, 14))
        self.bMax_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.verticalLayout_2.addWidget(self.bMax_label)
        self.cMax = QtWidgets.QLineEdit(self.widget)
        self.cMax.setMinimumSize(QtCore.QSize(133, 20))
        self.cMax.setMaximumSize(QtCore.QSize(133, 20))
        self.verticalLayout_2.addWidget(self.cMax)
        self.cMax_label = QtWidgets.QLabel(self.widget)
        self.cMax_label.setMinimumSize(QtCore.QSize(0, 14))
        self.cMax_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.verticalLayout_2.addWidget(self.cMax_label)
        self.dMax = QtWidgets.QLineEdit(self.widget)
        self.dMax.setMinimumSize(QtCore.QSize(133, 20))
        self.dMax.setMaximumSize(QtCore.QSize(133, 20))
        self.verticalLayout_2.addWidget(self.dMax)
        self.dMax_label = QtWidgets.QLabel(self.widget)
        self.dMax_label.setMinimumSize(QtCore.QSize(0, 14))
        self.dMax_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.verticalLayout_2.addWidget(self.dMax_label)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.swarm = QtWidgets.QSpinBox(self.widget)
        self.swarm.setMinimumSize(QtCore.QSize(133, 20))
        self.swarm.setMaximumSize(QtCore.QSize(133, 20))
        self.swarm.setMinimum(2)
        self.swarm.setMaximum(10000)
        self.verticalLayout_3.addWidget(self.swarm)
        self.swarm_label = QtWidgets.QLabel(self.widget)
        self.swarm_label.setMinimumSize(QtCore.QSize(0, 14))
        self.swarm_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.verticalLayout_3.addWidget(self.swarm_label)
        self.GWC = QtWidgets.QDoubleSpinBox(self.widget)
        self.GWC.setMinimumSize(QtCore.QSize(133, 0))
        self.GWC.setMaximumSize(QtCore.QSize(133, 20))
        self.verticalLayout_3.addWidget(self.GWC)
        self.GWC_label = QtWidgets.QLabel(self.widget)
        self.GWC_label.setMinimumSize(QtCore.QSize(0, 14))
        self.GWC_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.verticalLayout_3.addWidget(self.GWC_label)
        self.LWC = QtWidgets.QDoubleSpinBox(self.widget)
        self.LWC.setMinimumSize(QtCore.QSize(133, 0))
        self.LWC.setMaximumSize(QtCore.QSize(133, 20))
        self.verticalLayout_3.addWidget(self.LWC)
        self.LWC_label = QtWidgets.QLabel(self.widget)
        self.LWC_label.setMinimumSize(QtCore.QSize(0, 14))
        self.LWC_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.verticalLayout_3.addWidget(self.LWC_label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.Iterations = QtWidgets.QSpinBox(self.widget)
        self.Iterations.setMinimumSize(QtCore.QSize(133, 20))
        self.Iterations.setMaximumSize(QtCore.QSize(133, 20))
        self.Iterations.setMinimum(1)
        self.Iterations.setMaximum(10000)
        self.verticalLayout_4.addWidget(self.Iterations)
        self.Iterations_label = QtWidgets.QLabel(self.widget)
        self.Iterations_label.setMinimumSize(QtCore.QSize(0, 14))
        self.Iterations_label.setMaximumSize(QtCore.QSize(16777215, 14))
        self.verticalLayout_4.addWidget(self.Iterations_label)
        # self.ratingCoef = QtWidgets.QDoubleSpinBox(self.widget)
        # self.ratingCoef.setMinimumSize(QtCore.QSize(133, 0))
        # self.ratingCoef.setMaximumSize(QtCore.QSize(133, 20))
        # self.verticalLayout_4.addWidget(self.ratingCoef)
        # self.ratingCoef_label = QtWidgets.QLabel(self.widget)
        # self.ratingCoef_label.setMinimumSize(QtCore.QSize(0, 14))
        # self.ratingCoef_label.setMaximumSize(QtCore.QSize(16777215, 14))
        # self.verticalLayout_4.addWidget(self.ratingCoef_label)
        self.iterationsButtonCanon = QtWidgets.QPushButton(self.widget)
        self.iterationsButtonCanon.setMinimumSize(QtCore.QSize(133, 0))
        self.iterationsButtonCanon.setMaximumSize(QtCore.QSize(133, 20))
        self.verticalLayout_4.addWidget(self.iterationsButtonCanon)
        self.iterationsButtonClassic = QtWidgets.QPushButton(self.widget)
        self.iterationsButtonClassic.setMinimumSize(QtCore.QSize(133, 0))
        self.iterationsButtonClassic.setMaximumSize(QtCore.QSize(133, 20))
        self.verticalLayout_4.addWidget(self.iterationsButtonClassic)
        self.saveButton = QtWidgets.QPushButton("save")
        self.saveButton.setMinimumSize(QtCore.QSize(133, 0))
        self.saveButton.setMaximumSize(QtCore.QSize(133, 20))
        self.verticalLayout_4.addWidget(self.saveButton)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.randomButton = QtWidgets.QPushButton(self.widget)
        self.horizontalLayout_3.addWidget(self.randomButton)
        self.inputButton = QtWidgets.QPushButton(self.widget)
        self.horizontalLayout_3.addWidget(self.inputButton)
        self.fileButton = QtWidgets.QPushButton(self.widget)
        self.horizontalLayout_3.addWidget(self.fileButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Swarm Alg"))
        self.aMin_label.setText(_translate("MainWindow", "A Min"))
        self.bMin_label.setText(_translate("MainWindow", "B Min"))
        self.cMin_label.setText(_translate("MainWindow", "C Min"))
        self.dMin_label.setText(_translate("MainWindow", "D Min"))
        self.aMax_label.setText(_translate("MainWindow", "A Max"))
        self.bMax_label.setText(_translate("MainWindow", "B Max"))
        self.cMax_label.setText(_translate("MainWindow", "C Max"))
        self.dMax_label.setText(_translate("MainWindow", "D Max"))
        self.swarm_label.setText(_translate("MainWindow", "Size of Swarm"))
        self.Iterations_label.setText(_translate(
            "MainWindow", "Number of Iterations"))
        # self.ratingCoef_label.setText(
            # _translate("MainWindow", "Rating Coefficient"))
        self.iterationsButtonCanon.setText(_translate("MainWindow", "canon iterations"))
        self.iterationsButtonClassic.setText(_translate("MainWindow", "classic iterations"))
        self.GWC_label.setText(_translate(
            "MainWindow", "Global Weight Coefficient"))
        self.LWC_label.setText(_translate(
            "MainWindow", "Local Weight Coefficient"))
        self.randomButton.setText(_translate("MainWindow", "random data"))
        self.inputButton.setText(_translate("MainWindow", "input data"))
        self.fileButton.setText(_translate("MainWindow", "file"))


class MplCanvas(FigureCanvas):
    def __init__(self, *args, **kwargs):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig, *args, **kwargs)

    def plotFunc(self, x, y):
        self.ax.plot(x, y, linewidth=1)

    def plotDots(self, x, y):
        self.ax.scatter(x, y, marker='o', s=1)

    def clear(self):
        self.fig.clear()
        self.ax = self.fig.add_subplot(111)


class UI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, facade):
        super(UI, self).__init__()
        self.setupUi(self)
        self.defaultState()
        self.statusBar().showMessage("Рой не загружен.")
        self.values = np.zeros(4)
        self.swarmCounter = 0
        self.iterationsCounter = 0
        self.facade = facade
        self.dialogRandom = DialogRandom(self)
        self.dialogInput = DialogInput(self)
        self.dialogSave = DialogSave(self)
        self.randomButton.clicked.connect(self.random)
        self.inputButton.clicked.connect(self.input)
        self.fileButton.clicked.connect(self.file)
        self.saveButton.clicked.connect(self.save)
        self.iterationsButtonCanon.clicked.connect(self.iterations)
        self.iterationsButtonClassic.clicked.connect(self.iterations)
        self.canavas_1 = MplCanvas()
        self.canavas_1.setMinimumSize(300, 300)
        self.canavas_2 = MplCanvas()
        self.canavas_2.setMinimumSize(300, 300)
        self.horizontalLayout_4.addWidget(self.canavas_1)
        self.horizontalLayout_4.addWidget(self.canavas_2)

    def defaultState(self):
        self.aMin.setText("-100")
        self.bMin.setText("-100")
        self.cMin.setText("-100")
        self.dMin.setText("-100")
        self.aMax.setText("100")
        self.bMax.setText("100")
        self.cMax.setText("100")
        self.dMax.setText("100")
        self.swarm.setValue(100)
        self.Iterations.setValue(10)
        # self.ratingCoef.setValue(0.1)
        self.GWC.setValue(0.5)
        self.LWC.setValue(0.5)
    
    def fileState(self, valList):
        assert len(valList) == 12
        self.aMin.setText(valList[0])
        self.bMin.setText(valList[1])
        self.cMin.setText(valList[2])
        self.dMin.setText(valList[3])
        self.aMax.setText(valList[4])
        self.bMax.setText(valList[5])
        self.cMax.setText(valList[6])
        self.dMax.setText(valList[7])
        self.swarm.setValue(int(valList[8]))
        self.GWC.setValue(float(valList[9]))
        self.LWC.setValue(float(valList[10]))
        self.dialogInput.dots.clear()
        self.dialogInput.dots.insertPlainText(valList[11])
        

    def plotFunc(self, args: np.ndarray, dots: np.ndarray):
        assert len(args) == 4
        self.canavas_1.clear()
        self.canavas_1.plotDots(dots[:, 0], dots[:, 1])
        def f(x): return args[0]*(x**3) + args[1]*(x**2) + args[2]*x + args[3]
        x = np.linspace(int(min(dots[:, 0])) - 1, int(max(dots[:, 0])) + 1, 100)
        # y = [f(i) for i in x]
        self.canavas_1.plotFunc(x, f(x))
        self.values = args
        self.canavas_1.draw()

    def plotMeanDeviationChange(self, meanDeviationChange):
        self.canavas_2.clear()
        self.canavas_2.plotFunc(list(range(len(meanDeviationChange))), meanDeviationChange)
        self.canavas_2.draw()
        self.statusBarResetIterationsCounter(len(meanDeviationChange), meanDeviationChange[-1])
    
    def errorMessage(self):
        QtWidgets.QMessageBox.question(self, 'ОШИБКА!', sys.exc_info()[1].args[0], QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
    
    def _swarmSetting(self):
        valList = [self.aMin.text(),
                   self.bMin.text(),
                   self.cMin.text(),
                   self.dMin.text(),
                   self.aMax.text(),
                   self.bMax.text(),
                   self.cMax.text(),
                   self.dMax.text(),
                   self.swarm.value(),
                   self.GWC.value(),
                   self.LWC.value()]
        self.facade.setSwarmSettings(valList)
    
    def random(self):
        try:
            self._swarmSetting()
        except ValueError:
            self.errorMessage()
            return
        self.dialogRandom.open()
    
    def input(self):
        try:
            self._swarmSetting()
        except ValueError:
            self.errorMessage()
            return
        self.dialogInput.open()
    
    def file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', './', 'Swarm text file (*.sds *.sdi)')
        if fileName:
            try:
                self.facade.openFile(fileName)
                self.statusBarNextSwarm()
            except ValueError:
                self.errorMessage()
    
    def iterations(self):
        if self.swarmCounter != 0:
            if self.sender() == self.iterationsButtonCanon:
                self.facade.makeCanonIterations(self.Iterations.value())
            else:
                self.facade.makeClassicIterations(self.Iterations.value())
                
    
    def save(self):
        if self.swarmCounter != 0:
            self.dialogSave.open()
    
    def statusBarResetIterationsCounter(self, n, meanDeviation):
        self.statusBar().showMessage("Номер роя: {}. Число итераций: {}. Среднее откланение: {}. Значения: {}.".format(self.swarmCounter, n, meanDeviation, self.values))
    
    def statusBarNextSwarm(self):
        self.swarmCounter += 1
        self.statusBar().showMessage("Номер роя: {}. Число итераций: 0.".format(self.swarmCounter))
        


class DialogRandom(QtWidgets.QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.root = root
        self.setWindowTitle("Random")
        self.xMin = QtWidgets.QLineEdit()
        self.yMin = QtWidgets.QLineEdit()
        self.xMax = QtWidgets.QLineEdit()
        self.yMax = QtWidgets.QLineEdit()
        self.size = QtWidgets.QSpinBox()
        self.size.setMaximum(1000)
        self.size.setMinimum(2)
        button = QtWidgets.QPushButton('next')
        button.clicked.connect(self.next)
        vLayout_1 = QtWidgets.QVBoxLayout()
        vLayout_1.addWidget(self.xMin)
        vLayout_1.addWidget(QtWidgets.QLabel('Min X'))
        vLayout_1.addWidget(self.yMin)
        vLayout_1.addWidget(QtWidgets.QLabel('Min Y'))
        vLayout_2 = QtWidgets.QVBoxLayout()
        vLayout_2.addWidget(self.xMax)
        vLayout_2.addWidget(QtWidgets.QLabel('Max X'))
        vLayout_2.addWidget(self.yMax)
        vLayout_2.addWidget(QtWidgets.QLabel('Max Y'))
        vLayout_3 = QtWidgets.QVBoxLayout()
        vLayout_3.addWidget(self.size)
        vLayout_3.addWidget(QtWidgets.QLabel('Number of Points'))
        vLayout_3.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addLayout(vLayout_1)
        hLayout.addLayout(vLayout_2)
        hLayout.addLayout(vLayout_3)
        vLayoutMain = QtWidgets.QVBoxLayout()
        vLayoutMain.addLayout(hLayout)
        vLayoutMain.addWidget(button)
        self.setLayout(vLayoutMain)
        self.defaultState()
        
    def defaultState(self):
        self.xMin.setText('-10000')
        self.yMin.setText('-10000')
        self.xMax.setText('10000')
        self.yMax.setText('10000')
        self.size.setValue(50)

    def next(self):
        valList = [self.xMin.text(),
                   self.yMin.text(),
                   self.xMax.text(),
                   self.yMax.text(),
                   self.size.value()]
        try:
            self.root.facade.setRandomDots(valList)
            self.close()
            self.root.statusBarNextSwarm()
        except ValueError:
            self.root.errorMessage()


class DialogInput(QtWidgets.QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.root = root
        self.setWindowTitle("Input")
        self.dots = QtWidgets.QTextEdit()
        self.nextButton = QtWidgets.QPushButton('next')
        self.nextButton.clicked.connect(self.next)
        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.nextButton)
        vLayoutMain = QtWidgets.QVBoxLayout()
        vLayoutMain.addWidget(self.dots)
        vLayoutMain.addWidget(QtWidgets.QLabel('Dots'))
        vLayoutMain.addLayout(hLayout)
        self.setLayout(vLayoutMain)

    def next(self):
        try:
            self.root.facade.setInputDots(self.dots.toPlainText())
            self.close()
            self.root.statusBarNextSwarm()
        except ValueError:
            self.root.errorMessage()

class DialogSave(QtWidgets.QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.root = root
        self.setWindowTitle("Save")
        self.saveSettingsButton = QtWidgets.QPushButton('save settings')
        self.saveIterationsButton = QtWidgets.QPushButton('save with iterations')
        self.saveSettingsButton.clicked.connect(self.save)
        self.saveIterationsButton.clicked.connect(self.save)
        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.saveSettingsButton)
        hLayout.addWidget(self.saveIterationsButton)
        vLayoutMain = QtWidgets.QVBoxLayout()
        vLayoutMain.addWidget(QtWidgets.QLabel('Как сохронить?'))
        vLayoutMain.addLayout(hLayout)
        self.setLayout(vLayoutMain)
    def save(self):
        try:
            fileName = None
            if self.sender() == self.saveSettingsButton:
                fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', './', 'Swarm text settings file (*.sds)')
            else:
                fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', './', 'Swarm text iterations file (*.sdi)')
            if fileName:
                self.root.facade.saveFile(fileName)
                self.close()
        except ValueError:
            self.root.errorMessage()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UI(None)
    ui.show()
    sys.exit(app.exec_())
