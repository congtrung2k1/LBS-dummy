# This Python file uses the following encoding: utf-8
import sys

from PySide2.QtCore import QObject, Signal, Slot, QThread
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel

from socket import *
from core.Process.caseProcess import pipeIn


class MainWindow(QObject):
    getUpdateResult = Signal(str)

    def __init__(self):
        QObject.__init__(self)
        self.ggmap = None

    def serverOn(self):
        self.working = TCPThread()
        self.working.start()
        self.working.updateLocation.connect(self.getUpdate)
        self.working.updateMap.connect(self.getMap)

    def getUpdate(self, res):
        self.getUpdateResult.emit(res)

    def getMap(self, map):
        self.ggmap = map

    @Slot()
    def showMemorized(self):
        if self.ggmap == None:
            self.deny = denyWindow()
            self.deny.show()
            return

        self.showing = showWindow(self.ggmap)
        self.showing.show()

class TCPThread(QThread):
    updateLocation = Signal(str)
    updateMap = Signal(object)

    def __init__(self):
        QThread.__init__(self)
        self.ggmap = None

    def run(self):
        s = socket(AF_INET,SOCK_STREAM)
        s.bind(('', 3117))
        s.listen(1)

        #print("[+] Server is on...")

        while True:
            ssub, addr = s.accept()
            loc = ssub.recv(1024).decode()

            print(f'\nReceiving {loc} from {addr[0]}:{addr[1]}')

            state = int(loc.split('-')[0])
            x = int(loc.split('-')[1])
            y = int(loc.split('-')[2])
            level = int(loc.split('-')[3])
            ret = pipeIn(self.ggmap, state, x, y, level)

            if state == 0:
                self.ggmap = ret[0]
                dum = ret[1]
            else:
                dum = ret

            loc = f'{dum[0]}-{dum[1]}'
            ssub.send(loc.encode())
            ssub.close()

            if ret == [-1, -1]:
                continue

            self.updateLocation.emit(f'{x}-{y}-{dum[0]}-{dum[1]}')
            self.updateMap.emit(self.ggmap)

        s.close()

class showWindow(QWidget):
    def __init__(self, ggmap: object):
        QWidget.__init__(self)
        self.setWindowTitle("Saved state")
        self.resize(450, 300)

        table = QTableWidget()
        table.setColumnCount(4)
        table.setRowCount(len(ggmap.memorized))
        table.setHorizontalHeaderLabels(["User Location", "Level", "User Shape", "Dummy Location"])

        for i, tmp in enumerate(ggmap.memorized):
            user = QTableWidgetItem(f'{tmp[0][0]}, {tmp[0][1]}')
            dumm = QTableWidgetItem(f'{tmp[1][0]}, {tmp[1][1]}')
            level = QTableWidgetItem(f'{tmp[2]}')
            uShape = QTableWidgetItem(f'{tmp[3][0]}, {tmp[3][1]}')

            table.setItem(i, 0, user)
            table.setItem(i, 1, level)
            table.setItem(i, 2, uShape)
            table.setItem(i, 3, dumm)

        layout = QVBoxLayout()
        layout.addWidget(table)
        self.setLayout(layout)

class denyWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QVBoxLayout()
        label = QLabel("Sorry, there are nothing yet.")
        layout.addWidget(label)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = MainWindow()

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("core", main)
    engine.load("qml/main.qml")

    main.serverOn()

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
