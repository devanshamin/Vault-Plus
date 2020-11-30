import sys
from pathlib import Path

from PyQt5 import QtCore, QtWidgets

from utils.vaultplusDB import fetch_2FA_type
from src import (login, create_account, enter_otp_online,
                enter_otp_offline, password_requirements, 
                enter_backup_code, password_manager, 
                sequence_info, demo)

class Login_(QtWidgets.QMainWindow, login.Login):

    # Switch window when "Log in" button is clicked.
    switch_window = QtCore.pyqtSignal()
    # Switch window when "Create an account" button is clicked.
    switch_window2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.pushbutton2.clicked.connect(self.pushbutton2_handler)

    def pushButton_handler(self) -> None:
        # First validate the user inputs and then display the next window.
        if self.validate():
            self.close()
            email = Path("modules", "user.txt").read_text()
            if fetch_2FA_type(email) == "Online":
                self.switch_window.connect(controller.show_enter_otp_online)
            else:
                self.switch_window.connect(controller.show_enter_otp_offline)
            self.switch_window.emit()

    def pushbutton2_handler(self) -> None:
        self.close()
        self.switch_window2.emit()

class CreateAnAccount_(QtWidgets.QMainWindow, create_account.CreateAnAccount):

    # Switch window when "Next" button is clicked.
    switch_window = QtCore.pyqtSignal()
    # Switch window when "I already have an account" button is clicked.
    switch_window2 = QtCore.pyqtSignal()
    # Switch window when "i" button is clicked.
    switch_window3 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.pushbutton2.clicked.connect(self.pushbutton2_handler)
        self.pushbutton3.clicked.connect(self.pushbutton3_handler)

    def pushButton_handler(self) -> None:
        # First validate the user inputs and then display the next window.
        if self.validate():
            self.close()
            self.switch_window.emit()

    def pushbutton2_handler(self) -> None:
        self.close()
        self.switch_window2.emit()

    def pushbutton3_handler(self) -> None:
        self.switch_window3.emit()

class EnterOtpON_(QtWidgets.QWidget, enter_otp_online.EnterOtpON):

    # Switch window when "Log in" button is clicked.
    switch_window = QtCore.pyqtSignal()
    # Switch window when "Forgot/Lost Sequence?" button is clicked.
    switch_window2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.pushbutton2.clicked.connect(self.pushbutton2_handler)

    def pushButton_handler(self) -> None:
        # First validate the user inputs and then display the next window.
        if self.validate():
            self.close()
            self.counterThread.quit()
            self.switch_window.emit()

    def pushbutton2_handler(self) -> None:
        self.close()
        self.switch_window2.emit()

class EnterOtpOF_(QtWidgets.QWidget, enter_otp_offline.EnterOtpOF):

    # Switch window when "Log in" button is clicked.
    switch_window = QtCore.pyqtSignal()
    # Switch window when "Forgot/Lost Sequence?" button is clicked.
    switch_window2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.pushbutton2.clicked.connect(self.pushbutton2_handler)

    def pushButton_handler(self) -> None:
        # First validate the user inputs and then display the next window.
        if self.validate():
            self.close()
            self.switch_window.emit()

    def pushbutton2_handler(self) -> None:
        self.close()
        self.switch_window2.emit()

class PasswordRequirements_(QtWidgets.QWidget, password_requirements.PasswordRequirements):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

class EnterBackupCode_(QtWidgets.QWidget, enter_backup_code.EnterBackupCode):

    # Switch window when "Log in" button is clicked.
    switch_window = QtCore.pyqtSignal()
    # Switch window when "Go back" button is clicked.
    switch_window2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.pushbutton2.clicked.connect(self.pushbutton2_handler)

    def pushButton_handler(self) -> None:
        # First validate the user inputs and then display the next window.
        if self.validate():
            #self.close()
            self.switch_window.emit()

    def pushbutton2_handler(self) -> None:
        self.close()
        self.switch_window2.emit()
        
class PasswordManager_(QtWidgets.QWidget, password_manager.VaultPlus):

    # Switch window when "Delete" button is pressed inside "Delete account" tab.
    switch_window = QtCore.pyqtSignal()
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton_9.clicked.connect(self.pushButton_9_handler)
    
    def pushButton_9_handler(self) -> None:
        if self.delete_account():
            self.close()
            self.switch_window.emit()

class SequenceInfo_(QtWidgets.QWidget, sequence_info.SequenceInfo):

    # Switch window when "See demo" button is clicked.
    switch_window = QtCore.pyqtSignal()
    # Switch window when "Skip demo" button is clicked.
    switch_window2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.pushbutton2.clicked.connect(self.pushbutton2_handler)
    
    def pushButton_handler(self) -> None:
        self.close()
        self.switch_window.emit()

    def pushbutton2_handler(self) -> None:
        self.close()
        self.switch_window2.emit()

class Demo_(QtWidgets.QWidget, demo.Demo):

    # Switch window when the current window is closed.
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def closeEvent(self, event) -> None:
        self.window_handler()

    def window_handler(self) -> None:
        self.close()
        self.switch_window.emit()

class Controller(object):
    """Control the display of the widgets."""

    def show_login(self) -> None:
        self.login = Login_()
        self.login.switch_window2.connect(self.show_create_an_account)
        self.login.show()
    
    def show_create_an_account(self) -> None:
        self.caccount = CreateAnAccount_()
        self.caccount.switch_window.connect(self.show_sequence_info)
        self.caccount.switch_window2.connect(self.show_login)
        self.caccount.switch_window3.connect(self.show_password_requirements)
        self.caccount.show()
    
    def show_enter_otp_online(self) -> None:
        self.ecodeon = EnterOtpON_()
        self.ecodeon.start_timer()
        self.ecodeon.switch_window.connect(self.show_password_manager)
        self.ecodeon.switch_window2.connect(self.show_enter_backup_code)
        self.ecodeon.show()
    
    def show_enter_otp_offline(self) -> None:
        self.ecodeof = EnterOtpOF_()
        self.ecodeof.start_timer()
        self.ecodeof.switch_window.connect(self.show_password_manager)
        self.ecodeof.switch_window2.connect(self.show_enter_backup_code)
        self.ecodeof.show()
    
    def show_password_requirements(self) -> None:
        self.prequirements = PasswordRequirements_()
        self.prequirements.show()

    def show_password_manager(self) -> None:
        self.pm = PasswordManager_()
        self.pm.switch_window.connect(self.show_login)
        self.pm.show()

    def show_enter_backup_code(self) -> None:
        self.ebcode = EnterBackupCode_()
        self.ebcode.switch_window.connect(self.show_password_manager)
        email = Path("modules", "user.txt").read_text()
        if fetch_2FA_type(email) == "Online":
            self.ebcode.switch_window2.connect(self.show_enter_otp_online)
        else:
            self.ebcode.switch_window2.connect(self.show_enter_otp_offline)
        self.ebcode.show()
    
    def show_sequence_info(self) -> None:
        self.seqin = SequenceInfo_()
        self.seqin.switch_window.connect(self.show_demo)
        self.seqin.switch_window2.connect(self.show_password_manager)
        self.seqin.show()

    def show_demo(self) -> None:
        self.demo = Demo_()
        self.demo.switch_window.connect(self.show_password_manager)
        self.demo.show()

if __name__ == "__main__":

    # QApplication class manages the GUI application’s control flow and main settings.
    app = QtWidgets.QApplication(sys.argv)

    # Controls the display of the widgets.
    controller = Controller()

    # Display the startup window (Log in).
    controller.show_login()
    
    # app.exec() starts off the QApplication object’s event loop.
    # sys.exit() method ensures a clean exit.
    sys.exit(app.exec_())