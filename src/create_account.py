from pathlib import Path

from pyisemail import is_email
from PyQt5 import QtCore, QtGui, QtWidgets

import src.images
from utils.vaultplusDB import verify_email
from utils.validate_password import pvalidate
from modules.registration import Registration
from src.password_requirements import PasswordRequirements

class CreateAnAccount(object):
    """Display GUI to the user creating a new account."""

    def setupUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        """Creates the widget objects in the proper containers and assigns the proper object names to them.
        
        Args:
            MainWindow: Object of QMainWindow.
        """

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(401, 521)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            "*{\n"
            "font-family:Calibri;\n"
            "font-size:20px;\n"
            "}\n"
            "QFrame\n"
            "{\n"
            "background: rgba(0,0,0,0.8);\n"
            "border-radius:15px\n"
            "}\n"
            "QPushButton\n"
            "{\n"
            "\n"
            "background:#2671a0;\n"
            "border-radius:60px;\n"
            "}\n"
            "QToolButton\n"
            "{\n"
            "background:#2671a0;\n"
            "border-radius:40px;\n"
            "}\n"
            "QLabel\n"
            "{\n"
            "color:white;\n"
            "background:transparent;\n"
            "font-weight:bold;\n"
            "}\n"
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
            "QLineEdit\n"
            "{\n"
            "background:transparent;\n"
            "border:none;\n"
            "color:white;\n"
            "border-bottom:1px solid #717072;\n"
            "}\n"
            "QRadioButton\n"
            "{\n"
            "color:white;\n"
            "font-size:19px\n"
            "}\n"
            "#label_2\n"
            "{\n"
            "font-weight:normal;\n"
            "font-size:19px;\n"
            "}\n"
            "QToolTip\n"
            "{\n"
            "font-weight:normal;\n"
            "background-color:black;\n" 
            "color:white;\n"
            "border:black solid 1px;\n"
            "}"
            )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 50, 361, 441))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 40, 211, 41))
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 330, 341, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushbutton2 = QtWidgets.QPushButton(self.frame)
        self.pushbutton2.setGeometry(QtCore.QRect(50, 400, 271, 21))
        self.pushbutton2.setObjectName("pushbutton2")
        self.pushbutton3 = QtWidgets.QPushButton(self.frame)
        self.pushbutton3.setGeometry(QtCore.QRect(320, 190, 31, 31))
        self.pushbutton3.setStyleSheet("font:bold;")
        self.pushbutton3.setObjectName("pushbutton3")
        self.pushbutton3.setToolTip("Password requirements")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 120, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("font-size:19px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 190, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("font-size:19px;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 260, 131, 41))
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(170, 260, 81, 41))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setToolTip("OTP is sent via email")
        self.radioButton.setChecked(True)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(260, 260, 81, 41))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setToolTip("OTP is shown within the GUI")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(160, 10, 81, 81))
        self.toolButton_2.setStyleSheet("")
        self.toolButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(45, 50))
        self.toolButton_2.setObjectName("toolButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        """Sets the text and titles of the widgets.
        
        Args:
            MainWindow: Object of QMainWindow.
        """

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome to Vault Plus"))
        self.label.setText(_translate("MainWindow", "Create your free account"))
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.pushbutton2.setText(_translate("MainWindow", "I already have an account"))
        self.pushbutton3.setText(_translate("MainWindow", "i"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Enter your email"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Create a strong password"))
        self.label_2.setText(_translate("MainWindow", "Select 2FA type:"))
        self.radioButton.setText(_translate("MainWindow", "Online"))
        self.radioButton_2.setText(_translate("MainWindow", "Offline"))

    def validate(self) -> bool:
        """Validate the input provided by the user.
        
        Returns:
            True if the input is valid else False.
        """
        msg = QtWidgets.QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(QtGui.QIcon(icon))
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        
        email = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        if not email or not password:
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
                        type_ = "Online" if self.radioButton.isChecked() else "Offline"
                        Registration(email, password, type_)
                        Path("modules", "user.txt").write_text(email)
                        return True