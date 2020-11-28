import sys

from PyQt5 import QtCore, QtWidgets

from src import (login, create_account, enter_code_online,
                enter_code_offline, password_requirements, 
                enter_backup_code, password_manager, 
                sequence_info, demo)
from utils.threading_ import stop_execution

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

    def pushButton_handler(self):
        # First validate the user inputs and then display the next window.
        if self.validate():
            self.close()
            self.switch_window.emit()

    def pushbutton2_handler(self):
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

    def pushButton_handler(self):
        # First validate the user inputs and then display the next window.
        if self.validate():
            self.close()
            self.switch_window.emit()

    def pushbutton2_handler(self):
        self.close()
        self.switch_window2.emit()

    def pushbutton3_handler(self):
        self.switch_window3.emit()

class EnterCodeON_(QtWidgets.QWidget, enter_code_online.EnterCodeON):

    # Switch window when "Log in" button is clicked.
    switch_window = QtCore.pyqtSignal()
    # Switch window when "Forgot/Lost Sequence?" button is clicked.
    switch_window2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.pushbutton2.clicked.connect(self.pushbutton2_handler)

    def pushButton_handler(self):
        # First validate the user inputs and then display the next window.
        if self.validate():
            self.close()
            self.switch_window.emit()

    def pushbutton2_handler(self):
        self.close()
        self.switch_window2.emit()

class EnterCodeOF_(QtWidgets.QWidget, enter_code_offline.EnterCodeOF):

    # Switch window when "Log in" button is clicked.
    switch_window = QtCore.pyqtSignal()
    # Switch window when "Forgot/Lost Sequence?" button is clicked.
    switch_window2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.pushbutton2.clicked.connect(self.pushbutton2_handler)

    def pushButton_handler(self):
        # First validate the user inputs and then display the next window.
        if self.validate():
            self.close()
            self.switch_window.emit()

    def pushbutton2_handler(self):
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

    def pushButton_handler(self):
        # First validate the user inputs and then display the next window.
        if self.validate():
            #self.close()
            self.switch_window.emit()

    def pushbutton2_handler(self):
        self.close()
        self.switch_window2.emit()
    
    def closeEvent(self, event):
        stop_execution()

class PasswordManager_(QtWidgets.QWidget, password_manager.VaultPlus):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

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
    
    def pushButton_handler(self):
        self.close()
        self.switch_window.emit()

    def pushbutton2_handler(self):
        self.close()
        self.switch_window2.emit()

class Demo_(QtWidgets.QWidget, demo.Demo):

    # Switch window when the current window is closed.
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def closeEvent(self, event):
        self.window_handler()

    def window_handler(self):
        self.close()
        self.switch_window.emit()

class Controller(object):

    def show_login(self) -> None:
        self.login = Login_()
        self.login.switch_window.connect(self.show_enter_code_offline)
        self.login.switch_window2.connect(self.show_create_an_account)
        self.login.show()

    def show_create_an_account(self) -> None:
        self.caccount = CreateAnAccount_()
        self.caccount.switch_window.connect(self.show_sequence_info)
        self.caccount.switch_window2.connect(self.show_login)
        self.caccount.switch_window3.connect(self.show_password_requirements)
        self.caccount.show()
    
    def show_enter_code_online(self) -> None:
        self.ecode = EnterCodeON_()
        self.ecode.switch_window.connect(self.show_password_manager)
        self.ecode.switch_window2.connect(self.show_enter_backup_code)
        self.ecode.show()
    
    def show_enter_code_offline(self) -> None:
        self.ecode = EnterCodeOF_()
        self.ecode.start_timer()
        self.ecode.switch_window.connect(self.show_password_manager)
        self.ecode.switch_window2.connect(self.show_enter_backup_code)
        self.ecode.show()
    
    def show_password_requirements(self) -> None:
        self.prequirements = PasswordRequirements_()
        self.prequirements.show()

    def show_password_manager(self) -> None:
        self.pm = PasswordManager_()
        self.pm.show()

    def show_enter_backup_code(self) -> None:
        self.ebcode = EnterBackupCode_()
        self.ebcode.switch_window.connect(self.show_password_manager)
        self.ebcode.switch_window2.connect(self.show_enter_code_offline)
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

    # Display the startup window (Login).
    controller.show_login()
    
    # app.exec() starts off the QApplication object’s event loop.
    # sys.exit() method ensures a clean exit.
    sys.exit(app.exec_())