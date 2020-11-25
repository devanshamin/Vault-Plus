from PyQt5 import QtCore, QtGui, QtWidgets

import src.images

class SequenceInfo(object):
    """Display sequence information GUI to the user."""

    def setupUi(self, Form: QtWidgets.QWidget) -> None:
        """Creates the widget objects in the proper containers and assigns the proper object names to them.
        
        Args:
            Form: Object of QWidget.
        """

        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.setFixedSize(391, 490)
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
            "QToolButton\n"
            "{\n"
            "background:#2671a0;\n"
            "border-radius:43px;\n"
            "}\n"
            "\n"
            "QLabel\n"
            "{\n"
            "color:white;\n"
            "background:transparent;\n"
            "font-weight:bold;\n"
            "}\n"
            "\n"
            "#label_2\n"
            "{\n"
            "font-weight:normal;\n"
            "}\n"
            "#label_3\n"
            "{\n"
            "font-weight:normal;\n"
            "}\n"
            "#label_4\n"
            "{\n"
            "font-weight:normal;\n"
            "}\n"
            "#label_5\n"
            "{\n"
            "font-weight:normal;\n"
            "}#label_6\n"
            "{\n"
            "font-weight:normal;\n"
            "}\n"
            "#label_7\n"
            "{\n"
            "font-weight:normal;\n"
            "}#label_8\n"
            "{\n"
            "font-weight:normal;\n"
            "}\n"
            "#label_9\n"
            "{\n"
            "font-weight:normal;\n"
            "}\n"
            "\n"
            "QPushButton\n"
            "{\n"
            "background:#2671a0;\n"
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
            "}"
            )
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 50, 371, 431))
        self.frame.setMaximumSize(QtCore.QSize(641, 621))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 50, 201, 41))
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(10, 320, 351, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushbutton2 = QtWidgets.QPushButton(self.frame)
        self.pushbutton2.setGeometry(QtCore.QRect(140, 380, 101, 41))
        self.pushbutton2.setObjectName("pushbutton2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 331, 41))
        self.label_2.setStyleSheet("font-size:18px;")
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 381, 51))
        self.label_3.setStyleSheet("font-size:18px;")
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 431, 51))
        self.label_4.setStyleSheet("font-size:18px;")
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(20, 230, 321, 41))
        self.label_7.setStyleSheet("font-size:18px;")
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 260, 301, 41))
        self.label_8.setStyleSheet("font-size:18px;")
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setObjectName("label_8")
        self.toolButton_2 = QtWidgets.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(150, 10, 91, 91))
        self.toolButton_2.setStyleSheet("")
        self.toolButton_2.setText("")
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(45, 50))
        self.toolButton_2.setObjectName("toolButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form: QtWidgets.QWidget) -> None:
        """Sets the text and titles of the widgets.
        
        Args:
            Form: Object of QWidget.
        """

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Vault Plus - 2FA"))
        self.label.setText(_translate("Form", "2 Factor Authentication"))
        self.pushButton.setText(_translate("Form", " See demo"))
        self.pushbutton2.setText(_translate("Form", "Skip demo"))
        self.label_2.setText(_translate("Form", "• Our system uses Sequence based 2FA. "))
        self.label_3.setText(_translate("Form", "• A PDF file named Sequence_youremail.pdf "))
        self.label_4.setText(_translate("Form", "   is created in the users directory."))
        self.label_7.setText(_translate("Form", "•  A text file named BackupCodes.txt is"))
        self.label_8.setText(_translate("Form", "is also created in the users directory."))