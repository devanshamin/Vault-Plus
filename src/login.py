from pathlib import Path

from pyisemail import is_email
from PyQt5 import QtCore, QtGui, QtWidgets

import src.images
from utils.logger import logger
from utils.vaultplusDB import verify_email, validate_mp

class Login(object):
    """Display login GUI to the user."""

    def setupUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        """Creates the widget objects in the proper containers and assigns the proper object names to them.
        
        Args:
            MainWindow: Object of QMainWindow.
        """

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(374,444)
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 50, 331, 361))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 40, 101, 41))
        self.label.setStyleSheet("")
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 250, 311, 51))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 110, 271, 31))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("font-size:19px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 180, 271, 31))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("font-size:19px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushbutton2 = QtWidgets.QPushButton(self.frame)
        self.pushbutton2.setGeometry(QtCore.QRect(70, 320, 201, 16))
        self.pushbutton2.setObjectName("pushbutton2")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(150, 10, 81, 81))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Vault Plus"))
        self.label.setText(_translate("MainWindow", "  Vault Plus"))
        self.pushButton.setText(_translate("MainWindow", "Log in"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Email"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushbutton2.setText(_translate("MainWindow", "Create an account"))

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
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if not email or not password:
            msg.setWindowTitle("Login")
            msg.setText("Please fill all fields.")
            msg.exec_()
        else:
            if not is_email(email, check_dns=True):
                msg.setWindowTitle("Email")
                msg.setText("Invalid Email Address. Try again.")
                msg.exec_()
            else:
                if not verify_email(email):
                    msg.setWindowTitle(f"Email: {email}")
                    msg.setText("There is no account associated with this email address. Please create an account or try again.")
                    msg.exec_()
                else:
                    if not validate_mp(email, password):
                        msg.setWindowTitle("Master Password")
                        msg.setText("Incorrect password. Try again.")
                        msg.exec_()
                    else:
                        Path("modules", "user.txt").write_text(email)
                        return True