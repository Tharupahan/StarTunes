# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'starTunesGui.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from functions import Functions


class Ui_MainWindow(Functions,object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(403, 248)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../.designer/backup/disc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QLabel, QPushButton, QCheckBox, QToolButton, QSpinBox{\n"
"    color:  cyan;\n"
"}\n"
"\n"
"QProgressBar{\n"
"    border: cyan;\n"
"    border-radius: 6px;\n"
"    background-color: grey;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    background-color: cyan;\n"
"    margin: 1.5px;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(100, 180, 88, 34))
        self.pauseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pauseButton.setObjectName("pauseButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(210, 180, 88, 34))
        self.stopButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopButton.setObjectName("stopButton")
        self.resumeButton = QtWidgets.QPushButton(self.centralwidget)
        self.resumeButton.setGeometry(QtCore.QRect(100, 180, 88, 34))
        self.resumeButton.setObjectName("resumeButton")
        self.volumeBox = QtWidgets.QSpinBox(self.centralwidget)
        self.volumeBox.setGeometry(QtCore.QRect(70, 120, 52, 21))
        self.volumeBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.volumeBox.setAlignment(QtCore.Qt.AlignCenter)
        self.volumeBox.setMaximum(100)
        self.volumeBox.setObjectName("volumeBox")
        self.volumeLabel = QtWidgets.QLabel(self.centralwidget)
        self.volumeLabel.setGeometry(QtCore.QRect(20, 120, 58, 18))
        self.volumeLabel.setObjectName("volumeLabel")
        self.repeatBox = QtWidgets.QCheckBox(self.centralwidget)
        self.repeatBox.setGeometry(QtCore.QRect(230, 120, 21, 21))
        self.repeatBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.repeatBox.setText("")
        self.repeatBox.setIconSize(QtCore.QSize(16, 16))
        self.repeatBox.setTristate(False)
        self.repeatBox.setObjectName("repeatBox")
        self.repeatLabel = QtWidgets.QLabel(self.centralwidget)
        self.repeatLabel.setGeometry(QtCore.QRect(180, 120, 58, 18))
        self.repeatLabel.setObjectName("repeatLabel")
        self.fadeLabel = QtWidgets.QLabel(self.centralwidget)
        self.fadeLabel.setGeometry(QtCore.QRect(320, 120, 30, 18))
        self.fadeLabel.setObjectName("fadeLabel")
        self.fadeBox = QtWidgets.QCheckBox(self.centralwidget)
        self.fadeBox.setGeometry(QtCore.QRect(360, 120, 20, 21))
        self.fadeBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fadeBox.setText("")
        self.fadeBox.setObjectName("fadeBox")
        self.selectButton = QtWidgets.QToolButton(self.centralwidget)
        self.selectButton.setGeometry(QtCore.QRect(360, 70, 31, 21))
        self.selectButton.setObjectName("selectButton")
        self.trackName = QtWidgets.QLabel(self.centralwidget)
        self.trackName.setGeometry(QtCore.QRect(20, 20, 360, 18))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.trackName.setFont(font)
        self.trackName.setAutoFillBackground(False)
        self.trackName.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.trackName.setFrameShadow(QtWidgets.QFrame.Plain)
        self.trackName.setText("")
        self.trackName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.trackName.setWordWrap(False)
        self.trackName.setObjectName("trackName")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 70, 340, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.resumeButton.raise_()
        self.pauseButton.raise_()
        self.stopButton.raise_()
        self.volumeBox.raise_()
        self.volumeLabel.raise_()
        self.repeatBox.raise_()
        self.repeatLabel.raise_()
        self.fadeLabel.raise_()
        self.fadeBox.raise_()
        self.selectButton.raise_()
        self.trackName.raise_()
        self.progressBar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.selectButton.clicked.connect(self.select)
        self.pauseButton.clicked.connect(self.pause)
        self.resumeButton.clicked.connect(self.resume)
        self.stopButton.clicked.connect(self.stop)
        self.volumeBox.valueChanged.connect(self.change_volume)
        self.repeatBox.stateChanged.connect(self.repeat)
        self.fadeBox.stateChanged.connect(self.fade)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "StarTunes"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.resumeButton.setText(_translate("MainWindow", "Resume"))
        self.volumeLabel.setText(_translate("MainWindow", "Volume"))
        self.repeatLabel.setText(_translate("MainWindow", "Repeat"))
        self.fadeLabel.setText(_translate("MainWindow", "Fade"))
        self.selectButton.setText(_translate("MainWindow", "..."))

        #disable elements before debut play
        self.toggle_elements(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
