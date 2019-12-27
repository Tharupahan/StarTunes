# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'starTunesGui.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from functions import Functions

class Ui_MainWindow(Functions, object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 249)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("disc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(100, 180, 88, 34))
        self.pauseButton.setObjectName("pauseButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(210, 180, 88, 34))
        self.stopButton.setObjectName("stopButton")
        self.timeSlider = QtWidgets.QSlider(self.centralwidget)
        self.timeSlider.setGeometry(QtCore.QRect(10, 60, 350, 20))
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.resumeButton = QtWidgets.QPushButton(self.centralwidget)
        self.resumeButton.setGeometry(QtCore.QRect(100, 180, 88, 34))
        self.resumeButton.setObjectName("resumeButton")
        self.volume_box = QtWidgets.QSpinBox(self.centralwidget)
        self.volume_box.setGeometry(QtCore.QRect(80, 120, 52, 21))
        self.volume_box.setObjectName("volume_box")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 120, 58, 18))
        self.label.setObjectName("label")
        self.repeat_box = QtWidgets.QCheckBox(self.centralwidget)
        self.repeat_box.setGeometry(QtCore.QRect(230, 121, 20, 21))
        self.repeat_box.setText("")
        self.repeat_box.setObjectName("repeat_box")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 120, 58, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 120, 58, 18))
        self.label_3.setObjectName("label_3")
        self.fadeout_box = QtWidgets.QCheckBox(self.centralwidget)
        self.fadeout_box.setGeometry(QtCore.QRect(360, 120, 20, 21))
        self.fadeout_box.setText("")
        self.fadeout_box.setObjectName("fadeout_box")
        self.selectButton = QtWidgets.QToolButton(self.centralwidget)
        self.selectButton.setGeometry(QtCore.QRect(370, 60, 21, 21))
        self.selectButton.setObjectName("selectButton")
        self.resumeButton.raise_()
        self.pauseButton.raise_()
        self.stopButton.raise_()
        self.timeSlider.raise_()
        self.volume_box.raise_()
        self.label.raise_()
        self.repeat_box.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.fadeout_box.raise_()
        self.selectButton.raise_()
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


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "StarTunes"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.resumeButton.setText(_translate("MainWindow", "Resume"))
        self.label.setText(_translate("MainWindow", "Volume"))
        self.label_2.setText(_translate("MainWindow", "Repeat"))
        self.label_3.setText(_translate("MainWindow", "FadeOut"))
        self.selectButton.setText(_translate("MainWindow", "..."))

        self.toggle_elements(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
