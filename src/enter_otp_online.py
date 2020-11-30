import time
import threading
from pathlib import Path
from ast import literal_eval

#pylint: disable=no-name-in-module
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QWidget, QToolButton, QLineEdit, QPushButton, 
                            QFrame, QLabel, QApplication, QMessageBox)

import src.images
from utils.logger import logger
from utils.email import email_code
from utils.vaultplusDB import fetch_sequence
from utils.sequence import generate_code, derive_otp

flag, code, email, length = None, None, None, None

class EnterOtpON(object):
    """Display enter OTP (online implementation) GUI to the user."""

    def setupUi(self, Form: QWidget) -> None:
        """Creates the widget objects in the proper containers and assigns the proper object names to them.
        
        Args:
            Form: Object of QWidget.
        """

        global length, email, flag
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

        email = Path("modules", "user.txt").read_text()
        self.sequence = literal_eval(fetch_sequence(email))
        length = [len(s.split(' | ')) for s in self.sequence]

        flag = True

        # Configuring separate thread
        self.counterThread = QtCore.QThread()
        self.counter = Counter()
        self.counter.moveToThread(self.counterThread)

    def retranslateUi(self, Form: QWidget) -> None:
        """Sets the text and titles of the widgets.
        
        Args:
            Form: Object of QWidget.
        """

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Vault Plus"))
        self.label.setText(_translate("Form", "Vault Plus"))
        self.pushButton.setText(_translate("Form", "Log in"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "9 digit OTP"))
        self.pushbutton2.setText(_translate("Form", "Forgot/Lost Sequence?"))
        self.label_2.setText(_translate("Form", "Enter OTP:"))

    def start_timer(self) -> None:
        """Start the execution of the thread."""

        self.counterThread.started.connect(self.counter.start)
        self.counterThread.start()

    def validate(self) -> bool:
        """Validate the input provided by the user.
        
        Returns:
            True if the input is valid else False.
        """

        global flag
        msg = QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(QtGui.QIcon(icon))
        msg.setIcon(QMessageBox.Warning)
        user_otp = self.lineEdit_2.text()
        user_otp = user_otp.upper().replace("-", "").replace(" ", "")
        otp = derive_otp(code, self.sequence)
        if not user_otp:
            msg.setWindowTitle("Enter OTP")
            msg.setText("Please fill all fields.")
            msg.exec_()
        elif user_otp != otp:
            msg.setWindowTitle("Enter OTP")
            msg.setText("Invalid OTP. Try again.")
            self.lineEdit_2.clear()
            msg.exec_()
        else:
            flag = False
            self.counterThread.exit()
            self.counterThread.quit()
            self.counterThread.wait()
            return True

    def closeEvent(self, event) -> None:
        """The event handler that receives close events.
        
        Args:
            event: Contains a flag that indicates whether the user wants the widget to be closed or not.
        """
        
        global flag
        flag = False
        self.counterThread.exit()
        self.counterThread.quit()
        self.counterThread.wait()

class Counter(QtCore.QObject):
    """Class intended to be used in a separate thread to generate numbers and send them to another thread."""

    def __init__(self):
        super(Counter, self).__init__()

    def start(self) -> None:
        """Start the 60 seconds timer and email a random code every 60 seconds."""

        global code
        while flag:
            code = generate_code(length)
            email_code(code, email)
            start = time.time()
            elapsed = 0
            seconds = 60
            while elapsed < seconds and flag:
                elapsed = time.time() - start
                time.sleep(1)