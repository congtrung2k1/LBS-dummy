# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide2.QtCore import QObject, Signal, Slot
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

from backend.location_generate import rand_location
from backend.moving import moving
from backend.connect import tcpclient


class MainWindow(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.key = 0
        self.decrypt = False
        self.saveText = ""
        self.level = 3
        self.userLocaion = []
        self.dummyLocation = []

    getFactorsResult = Signal(str)
    getConvertResult = Signal(str)
    getKey = Signal(str)
    getRandLocation = Signal(str)
    getDummyLocation = Signal(str)
    getMovingLocation = Signal(str)
    readText = Signal(str)
    getG = Signal(str)
    getP = Signal(str)
    getPubKey = Signal(str)
    getSharedKey = Signal(str)

    @Slot()
    def callRandLocation(self) -> None:
        self.userLocation = rand_location.random_location()
        self.getRandLocation.emit(f"User Location \n(X,Y) = {self.userLocation}")
        return None

    @Slot(int)
    def callDummyLocation(self, state: int) -> None:
        self.dummyLocation = tcpclient.sendLocation(state, self.userLocation[0], self.userLocation[1], self.level)
        self.getDummyLocation.emit(f"Dummy Location\n(X, Y) = {self.dummyLocation}")
        return None

    @Slot()
    def callMovingLocation(self) -> None:
        self.userLocation = moving.movingLocation(self.userLocation)
        self.getMovingLocation.emit(f"User Location \n(X, Y) = {self.userLocation}")
        return None

    @Slot(int)
    def callChangePriv(self, level: int) -> None:
        self.level = level
        return None


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    app = QApplication(sys.argv)
    app.setOrganizationName(" ")
    app.setOrganizationDomain(" ")

    main = MainWindow()

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("backend", main)
    engine.load("qml/pages/homePage.qml")

    if not engine.rootObjects():
        exit(-1)
    exit(app.exec_())
