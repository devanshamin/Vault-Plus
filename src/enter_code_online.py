import threading
from pathlib import Path

#pylint: disable=no-name-in-module
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QWidget, QToolButton, QLineEdit, QPushButton, 
                            QFrame, QLabel, QApplication, QMessageBox)

import src.images
from utils.logger import logger
from utils.vaultplusDB import fetch_sequence
from utils.threading_ import threads_start, verify, stop_execution

class EnterCodeON(object):
    """Display enter code (online implementation) GUI to the user."""

    def setupUi(self, Form: QWidget) -> None:
        """Creates the widget objects in the proper containers and assigns the proper object names to them.
        
        Args:
            Form: Object of QWidget.
        """

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

        try:
            email = Path("modules", "user.txt").read_text()
            sequence = fetch_sequence(email)
            t1 = threading.Thread(target=threads_start, args=(sequence , email, 'Test',))
            t1.start()
        except: 
            logger.error("Error occurred during execution of threads!", exc_info=True)

    def retranslateUi(self, Form: QWidget) -> None:
        """Sets the text and titles of the widgets.
        
        Args:
            Form: Object of QWidget.
        """

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Vault Plus"))
        self.label.setText(_translate("Form", "Vault Plus"))
        self.pushButton.setText(_translate("Form", "Log in"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "9 digit code"))
        self.pushbutton2.setText(_translate("Form", "Forgot/Lost Sequence?"))
        self.label_2.setText(_translate("Form", "Enter code:"))

    def validate(self) -> bool:
        """Validate the input provided by the user.
        
        Returns:
            True if the input is valid else False.
        """

        msg = QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(QtGui.QIcon(icon))
        msg.setIcon(QMessageBox.Warning)
        user_code = self.lineEdit_2.text()
        user_code = user_code.upper().replace("-", "").replace(" ", "")
        if not user_code:
            msg.setWindowTitle("Code")
            msg.setText("Please fill all fields.")
            msg.exec_()
        elif not verify(user_code):
            msg.setWindowTitle("Code")
            msg.setText("Invalid code. Try again.")
            self.lineEdit_2.clear()
            msg.exec_()
        else:
            stop_execution()
            return True