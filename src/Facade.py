import numpy as np
import sys
from Swarm import *
from Adapter import Adapter
from PyQt5 import QtWidgets
from UI import *


class Facade:
    def __init__(self):
        self.adapter = Adapter()
        self.swarm = None
        self.app = QtWidgets.QApplication(sys.argv)
        self.GUI = UI(self)
        self.GUI.show()
        sys.exit(self.app.exec_())

    def __swarm_isnt_create(self):
        raise (AttributeError(
            "Swarm isn't create. Please press \"random\", \"input\" or \"file\"."))
    
    def setSwarmSettings(self, valList):
        self.adapter.swarmSettings(valList)
    
    def openFile(self, fileName):
        file = open(fileName)
        valList = file.readlines()
        try:
            if fileName[-4:] == ".sds" and len(valList) == 12:
                self.adapter.swarmSettings(valList[:11])
                self.adapter.inputDots(valList[11])
                self.swarm = self.adapter.makeSwarm()
            elif fileName[-4:] == ".sdi" and len(valList) == 24:
                self.swarm = self.adapter.openIteratinsFile(valList)
                self.plotGraph()
            else:
                raise(ValueError(''))
        except ValueError:
            raise(ValueError("Файл не соответсвует формату."))
        file.close()
        self.GUI.fileState(self.adapter.getValList())
    
    def saveFile(self, fileName):
        if fileName[-4:] == ".sds":
            self.adapter.setSwarmSettings(self.swarm)
            self.adapter.saveSettingsFile(fileName)
        elif fileName[-4:] == ".sdi":
            print("Si")
            self.adapter.saveIterationsFile(self.swarm, fileName)
            
    def makeCanonIterations(self, iterationsNumber):
        self.swarm.canonIterations(iterationsNumber)
        self.plotGraph()
    
    def makeClassicIterations(self, iterationsNumber):
        self.swarm.classicIterations(iterationsNumber)
        self.plotGraph()
    
    def plotGraph(self):
        values = self.swarm.getBestVal()
        dots = self.swarm.getDots()
        meanDeviationChange = self.swarm.getMeanDeviationChange()
        self.GUI.plotFunc(values, dots)
        if meanDeviationChange:
            self.GUI.plotMeanDeviationChange(meanDeviationChange)
    
    def setRandomDots(self, valList):
        self.adapter.randomDots(valList)
        self.swarm = self.adapter.makeSwarm()
        self.GUI.fileState(self.adapter.getValList())
        
    def setInputDots(self, text):
        self.adapter.inputDots(text)
        self.swarm = self.adapter.makeSwarm()
    
    
    
if __name__ == "__main__":
    Facade()
