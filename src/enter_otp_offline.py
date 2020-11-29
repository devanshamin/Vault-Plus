import time
from pathlib import Path
from ast import literal_eval

from PyQt5 import QtCore, QtGui, QtWidgets

import src.images
from utils.vaultplusDB import fetch_sequence
from utils.sequence import generate_otp, derive_code

length = None

class EnterOtpOF(object):
    """Display enter OTP (offline implementation) GUI to the user."""

    def setupUi(self, Form: QtWidgets.QWidget) -> None:
        """Creates the widget objects in the proper containers and assigns the proper object names to them.
        
        Args:
            Form: Object of QWidget.
        """

        global length
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.setFixedSize(342, 471)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setItalic(False)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWhatsThis("")
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(False)
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
            "#lcdNumber{\n"
            "background:#2671a0;\n"
            "}\n"
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
            "#label_3\n"
            "{\n"
            "font-weight:normal;\n"
            "}\n"
            "#label_4\n"
            "{\n"
            "font-weight:normal;\n"
            "font-size:25px;\n"
            "}\n"
            "\n"
            "#textBrowser\n"
            "{\n"
            "background:transparent;\n"
            "}\n"
            "QLineEdit\n"
            "{\n"
            "background:transparent;\n"
            "border:none;\n"
            "color:white;\n"
            "border-bottom:1px solid #717072;\n"
            "}"
            )
        Form.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 50, 321, 411))
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
        self.pushButton.setGeometry(QtCore.QRect(10, 290, 301, 51))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 220, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("font-size:19px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushbutton2 = QtWidgets.QPushButton(self.frame)
        self.pushbutton2.setGeometry(QtCore.QRect(50, 360, 241, 31))
        self.pushbutton2.setObjectName("pushbutton2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 220, 101, 31))
        self.label_2.setObjectName("label_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 110, 91, 61))
        self.lcdNumber.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumber.setLineWidth(1)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(4)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 60.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(180, 110, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(150, 140, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.toolButton = QtWidgets.QToolButton(Form)
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

        self.otp = generate_otp(length)
        self.label_4.setText(self.otp.replace("-", " - "))

        # Configuring separate thread
        self.counterThread = QtCore.QThread()
        self.counter = Counter()
        self.counter.moveToThread(self.counterThread)

    def retranslateUi(self, Form: QtWidgets.QWidget) -> None:
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
        self.label_3.setText(_translate("Form", "Your code is"))
        self.label_4.setText(_translate("Form", "123 - 456 - 987"))

    def start_timer(self) -> None:
        """Start the execution of the thread."""

        self.counter.count.connect(self.lcdNumber.display)
        self.counter.new_otp.connect(self.label_4.setText)
        self.counter.stopped.connect(self.counterThread.wait)
        self.counterThread.started.connect(self.counter.start)
        self.counterThread.start()
    
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
        user_code = self.lineEdit_2.text()
        user_code = user_code.upper().replace("-", "").replace(" ", "")
        code = derive_code(self.otp, self.sequence)
        if not user_code:
            msg.setWindowTitle("Code")
            msg.setText("Please fill all fields.")
            msg.exec_()
        elif user_code != code:
            msg.setWindowTitle("Code")
            msg.setText("Invalid code. Try again.")
            self.lineEdit_2.clear()
            msg.exec_()
        else:
            self.counterThread.quit()
            return True

class Counter(QtCore.QObject):
    """Class intended to be used in a separate thread to generate numbers and send them to another thread."""

    new_otp = QtCore.pyqtSignal(str)
    count = QtCore.pyqtSignal(int)
    stopped = QtCore.pyqtSignal()

    def __init__(self):
        super(Counter, self).__init__()

    def start(self) -> None:
        """Start the count down from 60 to 1 and emit each value to the GUI thread to display."""

        x = 61
        while True and not QtCore.QThread().isInterruptionRequested():
            x -= 1
            if x == 0:
                otp = generate_otp(length)
                self.new_otp.emit(otp.replace("-", " - "))
                x = 60
            self.count.emit(x)
            time.sleep(1)
        QtCore.QThread().requestInterruption()
        self.stopped.emit()