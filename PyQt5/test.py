# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SimpleCalc.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainCalculatorWindow(object):
    def setupUi(self, MainCalculatorWindow):
        MainCalculatorWindow.setObjectName("MainCalculatorWindow")
        MainCalculatorWindow.resize(370, 532)
        self.mainwidget = QtWidgets.QWidget(MainCalculatorWindow)
        self.mainwidget.setObjectName("mainwidget")
        self.outputLabel = QtWidgets.QLabel(self.mainwidget)
        self.outputLabel.setGeometry(QtCore.QRect(0, 10, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setMidLineWidth(2)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.percentButton = QtWidgets.QPushButton(self.mainwidget, clicked=lambda: self.press_it("%"))
        self.percentButton.setGeometry(QtCore.QRect(10, 90, 78, 78))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        # -
        self.CButton = QtWidgets.QPushButton(self.mainwidget, clicked=lambda: self.press_it("%"))
        self.CButton.setGeometry(QtCore.QRect(100, 90, 78, 78))
        self.CButton.setFont(font)
        self.CButton.setObjectName("CButton")
        # -
        self.changeButton = QtWidgets.QPushButton(self.mainwidget)
        self.changeButton.setGeometry(QtCore.QRect(190, 90, 78, 78))
        self.changeButton.setFont(font)
        self.changeButton.setObjectName("changeButton")
        # -
        self.perButton = QtWidgets.QPushButton(self.mainwidget)
        self.perButton.setGeometry(QtCore.QRect(280, 90, 78, 78))
        self.perButton.setFont(font)
        self.perButton.setObjectName("perButton")
        # -
        self.pushButton_multi = QtWidgets.QPushButton(self.mainwidget)
        self.pushButton_multi.setGeometry(QtCore.QRect(280, 170, 78, 78))
        self.pushButton_multi.setFont(font)
        self.pushButton_multi.setObjectName("pushButton_multi")
        # -
        self.pushButton_21 = QtWidgets.QPushButton(self.mainwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(100, 170, 78, 78))
        self.pushButton_21.setFont(font)
        self.pushButton_21.setObjectName("pushButton_21")
        # -
        self.pushButton_7 = QtWidgets.QPushButton(self.mainwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 170, 78, 78))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        # -
        self.pushButton_22 = QtWidgets.QPushButton(self.mainwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(190, 170, 78, 78))
        self.pushButton_22.setFont(font)
        self.pushButton_22.setObjectName("pushButton_22")
        # -
        self.pushButton_minus = QtWidgets.QPushButton(self.mainwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(280, 250, 78, 78))
        #-
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_6 = QtWidgets.QPushButton(self.mainwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(100, 250, 78, 78))
        #-
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.mainwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 250, 78, 78))
        #-
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.mainwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(190, 250, 78, 78))
        #-
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_plus = QtWidgets.QPushButton(self.mainwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(280, 330, 78, 78))
        #-
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_2 = QtWidgets.QPushButton(self.mainwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 330, 78, 78))
        #-
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.mainwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 330, 78, 78))
        #-
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_3 = QtWidgets.QPushButton(self.mainwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 330, 78, 78))
        #-
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_equel = QtWidgets.QPushButton(self.mainwidget)
        self.pushButton_equel.setGeometry(QtCore.QRect(280, 410, 78, 78))
        #-
        self.pushButton_equel.setFont(font)
        self.pushButton_equel.setObjectName("pushButton_equel")
        self.pushButton_0 = QtWidgets.QPushButton(self.mainwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(100, 410, 78, 78))
        #-
        self.pushButton_0.setFont(font)
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_minesplus = QtWidgets.QPushButton(self.mainwidget)
        self.pushButton_minesplus.setGeometry(QtCore.QRect(10, 410, 78, 78))
        #-
        self.pushButton_minesplus.setFont(font)
        self.pushButton_minesplus.setObjectName("pushButton_minesplus")
        self.pushButton_dart = QtWidgets.QPushButton(self.mainwidget)
        self.pushButton_dart.setGeometry(QtCore.QRect(190, 410, 78, 78))
        #-
        self.pushButton_dart.setFont(font)
        self.pushButton_dart.setObjectName("pushButton_dart")
        MainCalculatorWindow.setCentralWidget(self.mainwidget)
        self.menubar = QtWidgets.QMenuBar(MainCalculatorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 21))
        self.menubar.setObjectName("menubar")
        MainCalculatorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainCalculatorWindow)
        self.statusbar.setObjectName("statusbar")
        MainCalculatorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainCalculatorWindow)
        QtCore.QMetaObject.connectSlotsByName(MainCalculatorWindow)

    def press_it(self, pressed):
        self.outputLabel.setText(pressed)

    def retranslateUi(self, MainCalculatorWindow):
        _translate = QtCore.QCoreApplication.translate
        MainCalculatorWindow.setWindowTitle(_translate("MainCalculatorWindow", "Simple Calculator"))
        self.outputLabel.setText(_translate("MainCalculatorWindow", "0"))
        self.percentButton.setText(_translate("MainCalculatorWindow", "%"))
        self.CButton.setText(_translate("MainCalculatorWindow", "C"))
        self.changeButton.setText(_translate("MainCalculatorWindow", "<<"))
        self.perButton.setText(_translate("MainCalculatorWindow", "/"))
        self.pushButton_multi.setText(_translate("MainCalculatorWindow", "X"))
        self.pushButton_21.setText(_translate("MainCalculatorWindow", "8"))
        self.pushButton_7.setText(_translate("MainCalculatorWindow", "7"))
        self.pushButton_22.setText(_translate("MainCalculatorWindow", "9"))
        self.pushButton_minus.setText(_translate("MainCalculatorWindow", "-"))
        self.pushButton_6.setText(_translate("MainCalculatorWindow", "5"))
        self.pushButton_4.setText(_translate("MainCalculatorWindow", "4"))
        self.pushButton_8.setText(_translate("MainCalculatorWindow", "6"))
        self.pushButton_plus.setText(_translate("MainCalculatorWindow", "+"))
        self.pushButton_2.setText(_translate("MainCalculatorWindow", "2"))
        self.pushButton_1.setText(_translate("MainCalculatorWindow", "1"))
        self.pushButton_3.setText(_translate("MainCalculatorWindow", "3"))
        self.pushButton_equel.setText(_translate("MainCalculatorWindow", "="))
        self.pushButton_0.setText(_translate("MainCalculatorWindow", "0"))
        self.pushButton_minesplus.setText(_translate("MainCalculatorWindow", "+/-"))
        self.pushButton_dart.setText(_translate("MainCalculatorWindow", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainCalculatorWindow = QtWidgets.QMainWindow()
    ui = Ui_MainCalculatorWindow()
    ui.setupUi(MainCalculatorWindow)
    MainCalculatorWindow.show()
    sys.exit(app.exec_())
