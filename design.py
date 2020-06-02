# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1095, 698)
        MainWindow.setMaximumSize(QtCore.QSize(1822, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setMaximumSize(QtCore.QSize(256, 256))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/icon.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.btnBrowse = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBrowse.sizePolicy().hasHeightForWidth())
        self.btnBrowse.setSizePolicy(sizePolicy)
        self.btnBrowse.setMaximumSize(QtCore.QSize(160, 25))
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout.addWidget(self.splitter)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setMaximumSize(QtCore.QSize(256, 256))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/icon.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.temButton = QtWidgets.QPushButton(self.splitter_2)
        self.temButton.setEnabled(True)
        self.temButton.setMaximumSize(QtCore.QSize(160, 25))
        self.temButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.temButton.setObjectName("temButton")
        self.horizontalLayout.addWidget(self.splitter_2)
        self.splitter_4 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.label_3 = QtWidgets.QLabel(self.splitter_4)
        self.label_3.setMaximumSize(QtCore.QSize(256, 256))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/icon.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.resultButton = QtWidgets.QPushButton(self.splitter_3)
        self.resultButton.setEnabled(True)
        self.resultButton.setMaximumSize(QtCore.QSize(100, 25))
        self.resultButton.setObjectName("resultButton")
        self.saveButton = QtWidgets.QPushButton(self.splitter_3)
        self.saveButton.setMaximumSize(QtCore.QSize(100, 25))
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.splitter_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnBrowse.setText(_translate("MainWindow", "Выберите фото"))
        self.temButton.setText(_translate("MainWindow", "Выберите тему"))
        self.resultButton.setText(_translate("MainWindow", "Результат"))
        self.saveButton.setText(_translate("MainWindow", "Сохранить фото"))

