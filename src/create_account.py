import os
import sys
from pathlib import Path

from pyisemail import is_email
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

import src.images
from utils.vaultplusDB import verify_email
from utils.validate_password import pvalidate
from src.password_requirements import PasswordRequirements
from modules.registration import Registration

class CreateAnAccount(object):
    """Display GUI to the user creating a new account."""

    def login(self) -> None:
        """Open GUI for Login."""
        Form.close()
        os.system("python login.py")
        
    def setupUi(self, Form: QtWidgets.QWidget) -> None:
        """Setup user interface for Qt Widget.
        
        Args:
            Form: Object of Qt Widget.
        """
        self.Form = Form
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.setFixedSize(401,428)
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
            "#pushbutton2\n"
            "{\n"
            "background:rgba(0,0,0,0);\n"
            "font-weight:normal;\n"
            "}\n"
            "#pushbutton3:hover{\n"
            "color:black;\n"
            "background:red;\n"
            "}\n"
            "QLineEdit\n"
            "{\n"
            "background:transparent;\n"
            "border:none;\n"
            "color:white;\n"
            "border-bottom:1px solid #717072;\n"
            "}"
        )
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 50, 361, 361))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 40, 211, 41))
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 260, 341, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushbutton2 = QtWidgets.QPushButton(self.frame)
        self.pushbutton2.setGeometry(QtCore.QRect(50, 330, 271, 21))
        self.pushbutton2.setObjectName("pushbutton2")
        self.pushbutton3 = QtWidgets.QPushButton(self.frame)
        self.pushbutton3.setGeometry(QtCore.QRect(320, 190, 31, 31))
        self.pushbutton3.setStyleSheet("font:bold;")
        self.pushbutton3.setObjectName("pushbutton3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 120, 291, 31))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("font-size:19px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 190, 291, 31))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("font-size:19px;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.toolButton_2 = QtWidgets.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(160, 10, 81, 81))
        self.toolButton_2.setStyleSheet("")
        self.toolButton_2.setText("")
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(45, 50))
        self.toolButton_2.setObjectName("toolButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.validate)
        self.pushbutton2.clicked.connect(self.login)
        self.pushbutton3.clicked.connect(self.pwd_req)

    def retranslateUi(self, Form: QtWidgets.QWidget) -> None:
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Welcome to Vault Plus"))
        self.label.setText(_translate("Form", "Create your free account"))
        self.pushButton.setText(_translate("Form", "Next"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Enter your email"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Create a strong password"))
        self.pushbutton2.setText(_translate("Form", "I already have an account"))
        self.pushbutton3.setText(_translate("Form", "i"))

    def pwd_req(self) -> None:
        """Open GUI for Password Requirements."""
        self.window = QtWidgets.QWidget()
        self.ui = PasswordRequirements()
        self.ui.setupUi(self.window)
        self.window.show()

    def validate(self) -> None:
        """Validate the input provided by the user."""
        msg = QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(QtGui.QIcon(icon))
        msg.setIcon(QMessageBox.Warning)
        
        email = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        if email == '' or password == '':
            msg.setWindowTitle("Create account")
            msg.setText("Please fill all fields.")
            msg.exec_()
        else:
            if not is_email(email, check_dns=True):
                msg.setWindowTitle("Email")
                msg.setText("Invalid Email Address. Try again.")
                msg.exec_()
            else:
                if verify_email(email):
                    msg.setWindowTitle(f"Email: {email}")
                    msg.setText("An account with this email already exists.")
                    msg.exec_()
                else:
                    problem = pvalidate(password)
                    if problem:
                        msg.setWindowTitle("Invalid Password")
                        msg.setText(problem)
                        msg.exec_()
                    else:
                        Registration(email, password)
                        Path("modules", "user.txt").write_text(email)
                        self.Form.close()
                        os.system("python Sequence_Info.py")

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)    
    Form = QtWidgets.QWidget()
    ui = CreateAnAccount()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
