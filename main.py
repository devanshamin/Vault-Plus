import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from src import (login, create_account, enter_code, 
                password_requirements)

class Login_(QtWidgets.QMainWindow, login.Login):

    # Switch window when "Login" button is clicked.
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
            self.switch_window.emit()

    def pushbutton2_handler(self):
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
            self.switch_window.emit()

    def pushbutton2_handler(self):
        self.switch_window2.emit()

    def pushbutton3_handler(self):
        self.switch_window3.emit()

class EnterCode_(QtWidgets.QWidget, enter_code.EnterCode):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

class PasswordRequirements_(QtWidgets.QWidget, password_requirements.PasswordRequirements):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

class Controller(object):

    def show_login(self) -> None:
        global flag
        self.login = Login_()
        self.login.switch_window.connect(self.show_enter_code)
        self.login.switch_window2.connect(self.show_create_an_account)
        if flag:
            self.caccount.close()
        self.login.show()

    def show_create_an_account(self) -> None:
        global flag
        flag = True
        self.caccount = CreateAnAccount_()
        #self.caccount.switch_window.connect(self.)
        self.caccount.switch_window2.connect(self.show_login)
        self.caccount.switch_window3.connect(self.show_password_requirements)
        self.login.close()
        self.caccount.show()
    
    def show_enter_code(self) -> None:
        self.ecode = EnterCode_()
        self.login.close()
        self.ecode.show()
    
    def show_password_requirements(self) -> None:
        self.prequirements = PasswordRequirements_()
        self.prequirements.show()

if __name__ == "__main__":

    # Flag is used to go back and forth between "Login" window and "Create An Account" window.
    flag = False

    # Starts off the QApplication object’s event loop.
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())