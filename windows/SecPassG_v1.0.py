# -*- coding: utf-8 -*-

###################################################################
# Writer    #  Tolga AKKAPULU                                     #
# Web       #  https://www.tolgaakkapulu.com                      #
#           #  https://www.parolaanalizi.com                      #
# LinkedIN  #  https://tr.linkedin.com/in/tolgaakkapulu           #
# GitHub    #  https://github.com/tolgaakkapulu                   #
###################################################################

import random
import string
import time
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(305, 377)
        MainWindow.setMinimumSize(QtCore.QSize(305, 377))
        MainWindow.setMaximumSize(QtCore.QSize(305, 377))
        
        app_icon = QtGui.QIcon()
        app_icon.addFile('secpass.ico', QtCore.QSize(32,32))
        app.setWindowIcon(app_icon)
        
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 13, 0, 1, 2)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout_10, 0, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setMinimumSize(QtCore.QSize(0, 0))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_8.addWidget(self.line_8)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setTristate(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_8.addWidget(self.checkBox_2)
        self.gridLayout.addLayout(self.horizontalLayout_8, 4, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_9.addWidget(self.line_9)
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_9.addWidget(self.checkBox_4)
        self.gridLayout.addLayout(self.horizontalLayout_9, 5, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_7.addWidget(self.line_7)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setMinimum(8)
        self.spinBox.setMaximum(255)
        self.spinBox.setProperty("value", 16)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_7.addWidget(self.spinBox)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_7.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(153, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(153, 0, 0);\n"
"border-color: rgb(153, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_11.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout_11, 11, 0, 1, 2)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_13.addWidget(self.line_5)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(0, 128, 0);")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_13.addWidget(self.lineEdit, 0, QtCore.Qt.AlignVCenter)
        self.gridLayout.addLayout(self.verticalLayout_13, 8, 0, 1, 2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 2)
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout.addWidget(self.line_10, 12, 0, 1, 2)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 9, 0, 1, 2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setChecked(True)
        self.checkBox_1.setObjectName("checkBox_1")
        self.verticalLayout_4.addWidget(self.checkBox_1)
        self.gridLayout.addLayout(self.verticalLayout_4, 4, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_4.addWidget(self.checkBox_3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_19.addWidget(self.label_4)
        self.gridLayout.addLayout(self.verticalLayout_19, 7, 0, 1, 2)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 6, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 305, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(self.Save_pass)
        self.pushButton.clicked.connect(self.SecPass)
        self.label_3.linkActivated.connect(self.openURL)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SecPassG - Secure Password Generator"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SecPassG v1.0<br/>Tolga Akkapulu - 2017 <br/></span><a href=\"https://www.tolgaakkapulu.com\"><span style=\" font-weight:600; text-decoration: underline; color:#990000;\">https://www.tolgaakkapulu.com</span></a></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#990000;\">Secure Password Generator</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Password Length"))
        self.checkBox_2.setText(_translate("MainWindow", "Symbol [!@#$% etc.]"))
        self.checkBox_4.setText(_translate("MainWindow", "Number [0-9]"))
        self.pushButton_2.setText(_translate("MainWindow", "Save"))
        self.pushButton.setText(_translate("MainWindow", "Generate"))
        self.checkBox_1.setText(_translate("MainWindow", "Upper Case [A-Z]"))
        self.checkBox_3.setText(_translate("MainWindow", "Lower Case [a-z]"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Press <span style=\" font-weight:600;\"></span><span style=\" font-weight:600; color:#990000;\">Generate</span><span style=\" font-weight:600;\"></span> button to create secure password</p></body></html>"))

    def openURL(self):
        webbrowser.open("https://www.tolgaakkapulu.com")

    password = ''
    def SecPass(self, MainWindow):
        Ui_MainWindow.password = ''
        Ui_MainWindow._translate = QtCore.QCoreApplication.translate
        self.label_4.setText(Ui_MainWindow._translate("MainWindow", "<html><head/><body><p align=\"center\">Press <span style=\" font-weight:600;\"></span><span style=\" font-weight:600; color:#990000;\">Generate</span><span style=\" font-weight:600;\"></span> button to create secure password</p></body></html>"))
        if self.checkBox_1.isChecked() and self.checkBox_2.isChecked() and self.checkBox_3.isChecked() and self.checkBox_4.isChecked() == True:
            chars = string.ascii_uppercase + string.punctuation + string.ascii_lowercase + string.digits
            Ui_MainWindow.password = ''.join(random.choice(chars) for x in range(int(self.spinBox.value())))
            self.lineEdit.setText(Ui_MainWindow.password)
        elif self.checkBox_1.isChecked() and self.checkBox_2.isChecked() and self.checkBox_3.isChecked() == True:
            chars = string.ascii_uppercase + string.punctuation + string.ascii_lowercase
            Ui_MainWindow.password = ''.join(random.choice(chars) for x in range(int(self.spinBox.value())))
            self.lineEdit.setText(Ui_MainWindow.password)
        elif self.checkBox_1.isChecked() and self.checkBox_2.isChecked() and self.checkBox_4.isChecked() == True:
            chars = string.ascii_uppercase + string.punctuation + string.digits
            Ui_MainWindow.password = ''.join(random.choice(chars) for x in range(int(self.spinBox.value())))
            self.lineEdit.setText(Ui_MainWindow.password)
        elif self.checkBox_1.isChecked() and self.checkBox_3.isChecked() and self.checkBox_4.isChecked() == True:
            chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
            Ui_MainWindow.password = ''.join(random.choice(chars) for x in range(int(self.spinBox.value())))
            self.lineEdit.setText(Ui_MainWindow.password)
        elif self.checkBox_2.isChecked() and self.checkBox_3.isChecked() and self.checkBox_4.isChecked() == True:
            chars = string.punctuation + string.ascii_lowercase + string.digits
            Ui_MainWindow.password = ''.join(random.choice(chars) for x in range(int(self.spinBox.value())))
            self.lineEdit.setText(Ui_MainWindow.password)
        elif self.checkBox_1.isChecked() and self.checkBox_2.isChecked() == True:
            chars = string.ascii_uppercase + string.punctuation
            Ui_MainWindow.password = ''.join(random.choice(chars) for x in range(int(self.spinBox.value())))
            self.lineEdit.setText(Ui_MainWindow.password)
        elif self.checkBox_1.isChecked() and self.checkBox_3.isChecked() == True:
            chars = string.ascii_uppercase + string.ascii_lowercase
            Ui_MainWindow.password = ''.join(random.choice(chars) for x in range(int(self.spinBox.value())))
            self.lineEdit.setText(Ui_MainWindow.password)
        elif self.checkBox_1.isChecked() and self.checkBox_4.isChecked() == True:
            chars = string.ascii_uppercase + string.digits
            Ui_MainWindow.password = ''.join(random.choice(chars) for x in range(int(self.spinBox.value())))
            self.lineEdit.setText(Ui_MainWindow.password)
        elif self.checkBox_2.isChecked() and self.checkBox_3.isChecked() == True:
            chars = string.punctuation + string.ascii_lowercase
            Ui_MainWindow.password = ''.join(random.choice(chars) for x in range(int(self.spinBox.value())))
            self.lineEdit.setText(Ui_MainWindow.password)
        elif self.checkBox_2.isChecked() and self.checkBox_4.isChecked() == True:
            chars = string.punctuation + string.digits
            Ui_MainWindow.password = ''.join(random.choice(chars) for x in range(int(self.spinBox.value())))
            self.lineEdit.setText(Ui_MainWindow.password)
        elif self.checkBox_3.isChecked() and self.checkBox_4.isChecked() == True:
            chars = string.ascii_lowercase + string.digits
            Ui_MainWindow.password = ''.join(random.choice(chars) for x in range(int(self.spinBox.value())))
            self.lineEdit.setText(Ui_MainWindow.password)
        elif self.checkBox_1.isChecked() == True:
            chars = string.ascii_uppercase
            Ui_MainWindow.password = ''.join(random.choice(chars) for x in range(int(self.spinBox.value())))
            self.lineEdit.setText(Ui_MainWindow.password)
        elif self.checkBox_2.isChecked() == True:
            chars = string.punctuation
            Ui_MainWindow.password = ''.join(random.choice(chars) for x in range(int(self.spinBox.value())))
            self.lineEdit.setText(Ui_MainWindow.password)
        elif self.checkBox_3.isChecked() == True:
            chars = string.ascii_lowercase
            Ui_MainWindow.password = ''.join(random.choice(chars) for x in range(int(self.spinBox.value())))
            self.lineEdit.setText(Ui_MainWindow.password)
        elif self.checkBox_4.isChecked() == True:
            chars = string.digits
            Ui_MainWindow.password = ''.join(random.choice(chars) for x in range(int(self.spinBox.value())))
            self.lineEdit.setText(Ui_MainWindow.password)
        else:
            Ui_MainWindow.password = ''
            self.lineEdit.setText("Select at least 1 option")

    def Save_pass(self, MainWindow):
        Ui_MainWindow._translate = QtCore.QCoreApplication.translate
        if not Ui_MainWindow.password == '' or Ui_MainWindow.password == ' ':
            file = open("SecPassG.txt", 'a')
            file.write("----------Secure Password Generator----------\n")
            file.write("Date & Time\t :  %s" % str(time.strftime("%c")))
            file.write("\nPassword Length\t :  %s characters" % str(self.spinBox.value()))
            file.write("\nYour Password\t :  %s\n" %str(Ui_MainWindow.password))
            file.close()
            self.label_4.setText(Ui_MainWindow._translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\"></span><span style=\" font-weight:600; color:#990000;\">Password </span>is saved.<br>File name : <span style=\" font-weight:600; color:#990000;\">SecPassG.txt</span></p></body></html>"))
        else:
            self.lineEdit.setText("Firstly, press Generate")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
