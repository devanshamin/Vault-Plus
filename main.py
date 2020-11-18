import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from src.create_account import CreateAnAccount

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)    
    Form = QtWidgets.QWidget()
    ui = CreateAnAccount()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())