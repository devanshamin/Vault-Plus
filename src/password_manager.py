from pathlib import Path
from ast import literal_eval

from PyQt5 import QtCore, QtGui, QtWidgets

import src.images
from utils.user_id import id_
from utils.sequence import download_sequence
from utils.vaultplusDB import (fetch_backupcodes, fetch_password, check_service, 
                                store_password, update_password, delete_password,
                                validate_mp, fetch_sequence, fetch_backupcodes)

class VaultPlus(object):
    """Display password manager GUI to the user."""

    def setupUi(self, Form: QtWidgets.QWidget) -> None:
        """Creates the widget objects in the proper containers and assigns the proper object names to them.

        Args:
            Form: Object of QWidget.
        """

        self.email = Path("modules", "user.txt").read_text()
        Path("modules", "user.txt").unlink()
        self.uid = id_(self.email)

        self.Form = Form
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(522, 553)
        Form.setMaximumSize(QtCore.QSize(724, 702))
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
            "QPushButton\n"
            "{\n"
            "\n"
            "background:#2671a0;\n"
            "border-radius:60px;\n"
            "font-weight:bold;\n"
            "}\n"
            "\n"
            "QToolButton\n"
            "{\n"
            "\n"
            "background:#2671a0;\n"
            "border-radius:50px;\n"
            "}\n"
            "\n"
            "QLabel\n"
            "{\n"
            "color:white;\n"
            "background:transparent;\n"
            "}\n"
            "\n"
            "QPushButton\n"
            "{\n"
            "color:white;\n"
            "border-radius:15px;\n"
            "}\n"
            "\n"
            "QLineEdit\n"
            "{\n"
            "background:transparent;\n"
            "border:none;\n"
            "color:white;\n"
            "border-bottom:1px solid #717072;\n"
            "}"
            )
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 60, 501, 481))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(80, 410, 331, 51))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.log_out)

        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(0, 80, 501, 291))
        self.tabWidget.setStyleSheet(
            "QTabWidget::pane{border-bottom: 0px;\n"
            "background: rgba(0,0,0,0.8);\n"
            "}"
            )
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")

        # View password
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 30, 461, 151))
        self.listWidget_2.setStyleSheet("background-color:white;")
        self.listWidget_2.setObjectName("listWidget_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_7.setGeometry(QtCore.QRect(30, 210, 261, 31))
        self.lineEdit_7.setStyleSheet(
            "color:white;\n"
            ""
            )
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 210, 151, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")

        self.pushButton_2.clicked.connect(self.view_password)

        # Store Password
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(598, 16, 208, 33))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 40, 241, 33))
        self.lineEdit_2.setStyleSheet("color:white;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(90, 40, 91, 42))
        self.label.setStyleSheet("font-size:26px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 111, 42))
        self.label_2.setStyleSheet("font-size:26px;")
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 110, 241, 33))
        self.lineEdit_3.setStyleSheet("color:white;")
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(200, 190, 111, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.tab_2, "")

        self.pushButton_8.clicked.connect(self.store_password)

        # Update password
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 40, 241, 33))
        self.lineEdit_4.setStyleSheet("color:white;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 110, 241, 33))
        self.lineEdit_5.setStyleSheet("color:white;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(90, 40, 91, 42))
        self.label_3.setStyleSheet("font-size:26px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(60, 110, 111, 42))
        self.label_4.setStyleSheet("font-size:26px;")
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 190, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.pushButton_3.clicked.connect(self.update_password)

        # Delete password
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 80, 231, 33))
        self.lineEdit_6.setStyleSheet("color:white;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(90, 80, 81, 42))
        self.label_5.setStyleSheet("font-size:26px;")
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 190, 131, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.pushButton_4.clicked.connect(self.delete_password)

        # Download sequence
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 180, 241, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_8.setGeometry(QtCore.QRect(100, 100, 311, 33))
        self.lineEdit_8.setStyleSheet("color:white;")
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_6 = QtWidgets.QLabel(self.tab_5)
        self.label_6.setGeometry(QtCore.QRect(130, 30, 251, 42))
        self.label_6.setStyleSheet("font-size:26px;")
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab_5, "")

        self.pushButton_5.clicked.connect(self.download_sequence)

        # Backup codes
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_6.setGeometry(QtCore.QRect(280, 80, 191, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.listWidget = QtWidgets.QListWidget(self.tab_6)
        self.listWidget.setGeometry(QtCore.QRect(40, 60, 191, 151))
        self.listWidget.setStyleSheet("background-color:white;")
        self.listWidget.setObjectName("listWidget")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_7.setGeometry(QtCore.QRect(280, 160, 191, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.tabWidget.addTab(self.tab_6, "")

        self.pushButton_6.clicked.connect(self.view_backup_codes)
        self.pushButton_7.clicked.connect(self.download_backup_codes)

        self.toolButton_2 = QtWidgets.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(210, 10, 101, 101))
        self.toolButton_2.setStyleSheet("")
        self.toolButton_2.setText("")
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(45, 50))
        self.toolButton_2.setObjectName("toolButton_2")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form: QtWidgets.QWidget) -> None:
        """Sets the text and titles of the widgets.

        Args:
            Form: Object of QWidget.
        """

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Vault Plus"))
        self.pushButton.setText(_translate("Form", "   Log out"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", "Service"))
        self.pushButton_2.setText(_translate("Form", "Get Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "View Password"))
        self.label.setText(_translate("Form", "Service:"))
        self.label_2.setText(_translate("Form", "Password:"))
        self.pushButton_8.setText(_translate("Form", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Store password"))
        self.label_3.setText(_translate("Form", "Service:"))
        self.label_4.setText(_translate("Form", "Password:"))
        self.pushButton_3.setText(_translate("Form", "Update"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Update password"))
        self.label_5.setText(_translate("Form", "Service:"))
        self.pushButton_4.setText(_translate("Form", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Delete password"))
        self.pushButton_5.setText(_translate("Form", "Download PDF file "))
        self.label_6.setText(_translate("Form", "Enter Master Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Download sequence"))
        self.pushButton_6.setText(_translate("Form", "View"))
        self.pushButton_7.setText(_translate("Form", "Download"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "Backup codes"))

    def view_password(self) -> None:
        """Fetch and display the password for a given service."""

        self.listWidget_2.clear()
        msg = QtWidgets.QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(QtGui.QIcon(icon))
        service = self.lineEdit_7.text()
        self.lineEdit_7.clear()
        if not service:
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("View Password")
            msg.setText("Please fill all fields.")
            msg.exec_()
        else:
            msg.setIcon(QtWidgets.QMessageBox.Information)
            service = service.capitalize()
            passwords = fetch_password(self.uid)
            if not passwords:
                msg.setWindowTitle("View Password")
                msg.setText("Your safe is empty.")
                msg.exec_()
            elif service == "All":
                for k, v in passwords.items():
                    self.listWidget_2.addItem(f"{k}: {v}")
            elif service in passwords:
                self.listWidget_2.addItem(f"{service}: {passwords[service]}")
            else:
                msg.setWindowTitle("View Password")
                msg.setText("Service not found.")
                msg.exec_()

    def store_password(self) -> None:
        """Store a user's password for a service."""

        msg = QtWidgets.QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(QtGui.QIcon(icon))
        service = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        if not service or not password:
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowTitle("Store Password")
            msg.setText("Please fill all fields.")
            msg.exec_()
        else:
            service = service.capitalize()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            if check_service(self.uid, service):
                msg.setWindowTitle("Store Password")
                msg.setText("Service already exists.")
                msg.exec_()
            else:
                store_password(self.uid, service, password)
                msg.setWindowTitle("Store Password")
                msg.setText("Password has been stored successfully.")
                msg.exec_()

    def update_password(self) -> None:
        """Update a user's password for a service."""

        msg = QtWidgets.QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(QtGui.QIcon(icon))
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        service = self.lineEdit_4.text()
        password = self.lineEdit_5.text()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        if not service or not password:
            msg.setWindowTitle("Update Password")
            msg.setText("Please fill all fields.")
            msg.exec_()
        else:
            service = service.capitalize()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            if not fetch_password(self.uid):
                msg.setWindowTitle("Update Password")
                msg.setText("Your safe is empty.")
                msg.exec_()
            elif check_service(self.uid, service):
                update_password(self.uid, service, password)
                msg.setWindowTitle("Update Password")
                msg.setText("Password has been updated successfully.")
                msg.exec_()
            else:
                msg.setWindowTitle("Update Password")
                msg.setText("Service doesn't exist. Go to 'View Passwords' to view your existing services and try again.")
                msg.exec_()

    def delete_password(self) -> None:
        """Delete a user's password for a service."""

        msg = QtWidgets.QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(QtGui.QIcon(icon))
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        service = self.lineEdit_6.text()
        self.lineEdit_6.clear()
        if service == '':
            msg.setWindowTitle("Store Password")
            msg.setText('Please fill all fields.')
            msg.exec_()
        else:
            service = service.capitalize()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            if not fetch_password(self.uid):
                msg.setWindowTitle("Delete Password")
                msg.setText("Your safe is empty.")
                msg.exec_()
            elif check_service(self.uid, service):
                delete_password(self.uid, service)
                msg.setWindowTitle("Delete Password")
                msg.setText("Password has been removed successfully.")
                msg.exec_()
            else:
                msg.setWindowTitle("Delete Password")
                msg.setText("Service doesn't exist. Go to 'View Passwords' to view your existing services and try again.")
                msg.exec_()

    def download_sequence(self) -> None:
        """Download a PDF file containing user's sequence."""

        msg = QtWidgets.QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(QtGui.QIcon(icon))
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        password = self.lineEdit_8.text()
        self.lineEdit_8.clear()
        if not password:
            msg.setWindowTitle("Download Sequence")
            msg.setText("Please fill all fields.")
            msg.exec_()
        else:
            msg.setIcon(QtWidgets.QMessageBox.Information)
            if validate_mp(self.email, password):
                sequence = literal_eval(fetch_sequence(self.email))
                dir_path = Path("users", self.uid[1:])
                if not dir_path.exists():
                    dir_path.mkdir(parents=True)
                elif not Path(dir_path, "Sequence.pdf").exists():
                    download_sequence(self.email, password, sequence, dir_path)	
                msg.setWindowTitle("Master Password")
                msg.setText("Download complete. PDF file can be found in the 'users' directory.")
                msg.exec_()
            else:
                msg.setWindowTitle("Master Password")
                msg.setText("Incorrect master password. Please try again.")
                msg.exec_()

    def view_backup_codes(self) -> None:
        """Fetch and display user's backup codes."""

        self.listWidget.clear()
        codes = fetch_backupcodes(self.email)
        for code in codes.split('-'):
            self.listWidget.addItem(f"{code[:4]} {code[4:]}")
    
    def download_backup_codes(self) -> None:
        """Fetch and save the backup codes text file in the users directory."""

        dir_path = Path("users", self.uid[1:])
        if not dir_path.exists():
            dir_path.mkdir(parents=True)
        codes = fetch_backupcodes(self.email)
        text = "Keep these backup codes somewhere safe but accessible.\n\n{}\n\nEach backup code can be used once.\nAfter use of each backup code, a new backup code is automatically generated and is available inside the password manager.".format(codes.replace("-", "\n")) 
        Path(dir_path, "BackupCodes.txt").write_text(text)
        msg = QtWidgets.QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(QtGui.QIcon(icon))
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Backup codes")
        msg.setText("Download complete. Text file can be found in the 'users' directory.")
        msg.exec_()

    def log_out(self) -> None:
        """Close the widget."""
        
        self.Form.close()