import os
import sys
import threading
from pathlib import Path

#pylint: disable=no-name-in-module
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QWidget, QToolButton, QLineEdit, QPushButton, QFrame, QLabel, QApplication, QMessageBox)

import src.images
from utils.logger import logger
from utils.vaultplusDB import fetch_sequence
from utils.threading_ import threads_start, tflag, verify, stop_execution

class EnterCode(object):

    def closeEvent(self, event):

        msgBox = QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msgBox.setWindowIcon(QtGui.QIcon(icon))
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("Are you sure you want to close the window?")
        msgBox.setWindowTitle("2 Factor Authentication")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        reply = msgBox.exec()
        
        if reply == QMessageBox.Yes:
            event.accept()
            stop_execution()
            #self.Form.close()
        else:
            event.ignore()

    def setupUi(self, Form):

        self.Form = Form
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.setFixedSize(342, 403)
        Form.setMaximumSize(QtCore.QSize(374, 419))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(
            "*{\n"
            "font-family:Calibri;\n"
            "font-size:20px;\n"
            "}\n"
            "\n"
            "QFrame\n"
            "{\n"
            "background: rgba(0,0,0,0.8);\n"
            "border-radius:15px\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton\n"
            "{\n"
            "\n"
            "background:#2671a0;\n"
            "border-radius:60px;\n"
            "}\n"
            "\n"
            "QToolButton\n"
            "{\n"
            "\n"
            "background:#2671a0;\n"
            "border-radius:40px;\n"
            "}\n"
            "\n"
            "QLabel\n"
            "{\n"
            "color:white;\n"
            "background:transparent;\n"
            "font-weight:bold;\n"
            "}\n"
            "#label_2{\n"
            "font-weight:normal;\n"
            "}\n"
            "\n"
            "QPushButton\n"
            "{\n"
            "color:white;\n"
            "border-radius:15px;\n"
            "font-weight:bold;\n"
            "}\n"
            "QPushButton:hover\n"
            "{\n"
            "border-radius:15px;\n"
            "}\n"
            "\n"
            "#pushbutton2\n"
            "{\n"
            "background:rgba(0,0,0,0);\n"
            "font-weight:normal;\n"
            "}\n"
            "QLineEdit\n"
            "{\n"
            "background:transparent;\n"
            "border:none;\n"
            "color:white;\n"
            "border-bottom:1px solid #717072;\n"
            "}"
            )
        self.frame = QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 50, 321, 341))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 40, 101, 41))
        self.label.setStyleSheet("")
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 220, 301, 51))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 150, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("font-size:19px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushbutton2 = QPushButton(self.frame)
        self.pushbutton2.setGeometry(QtCore.QRect(50, 290, 241, 31))
        self.pushbutton2.setObjectName("pushbutton2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 141, 31))
        self.label_2.setObjectName("label_2")
        self.toolButton = QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(130, 10, 81, 81))
        self.toolButton.setStyleSheet("")
        self.toolButton.setText("")
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(45, 50))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.enter_code)
        self.pushbutton2.clicked.connect(self.backup_code)

        try:
            email = Path("modules", "user.txt").read_text()
            sequence = fetch_sequence(email)
            t1 = threading.Thread(target=threads_start, args=(sequence , email, 'Test',))
            t1.start()
        except: 
            logger.error("Error occurred during execution of threads!", exc_info=True)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Vault Plus"))
        self.label.setText(_translate("Form", "Vault Plus"))
        self.pushButton.setText(_translate("Form", "Log in"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "9 digit OTP"))
        self.pushbutton2.setText(_translate("Form", "Forgot/Lost Sequence?"))
        self.label_2.setText(_translate("Form", "Enter OTP:"))

    def backup_code(self):
        #stop_threads_execution()
        tflag = False
        self.Form.close()
        os.system('python Enter_BackupCode.py')
        
    def enter_code(self):
        msg = QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(QtGui.QIcon(icon))
        msg.setIcon(QMessageBox.Warning)
        user_code = self.lineEdit_2.text()
        user_code = user_code.upper().replace("-", "")
        if user_code == '':
            msg.setWindowTitle("Code")
            msg.setText("Please fill all fields.")
            msg.exec_()
        elif verify(user_code):
            tflag = False
            self.Form.close()
            os.system("python Main_Screen.py")
        else:
            msg.setWindowTitle("Code")
            msg.setText("Invalid code. Try again.")
            self.lineEdit_2.clear()
            msg.exec_()

def main():
#if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = EnterCode()
    ui.setupUi(Form)
    Form.show()
    #sys.exit(app.exec_())      
