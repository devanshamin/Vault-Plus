from PyQt5 import QtCore, QtGui, QtWidgets

class PasswordRequirements(object):
    """Display GUI for the password requirements."""

    def setupUi(self, Form: QtWidgets.QWidget) -> None:
        """Creates the widget objects in the proper containers and assigns the proper object names to them.
        
        Args:
            Form: Object of Qt Widget.
        """

        Form.setObjectName("Form")
        Form.setFixedSize(301, 230)
        #Form.move(281, 211)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(
            "*{\n"
            "font-family:Calibri;\n"
            "}\n"
            "\n"
            "QTextBrowser{\n"
            "background: rgba(0,0,0,0.8);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size:24px;\n"
            "border-radius:15px\n"
            "}\n"
            "\n"
            )
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 281, 211))
        self.textBrowser_2.setStyleSheet("")
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form: QtWidgets.QWidget) -> None:
        """Sets the text and titles of the widgets.
        
         Args:
            Form: Object of Qt Widget.
        """

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Vault Plus "))
        self.textBrowser_2.setHtml(
            _translate(
                "Form", 
                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Calibri\'; font-size:24px; font-weight:400; font-style:normal;\">\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'century gothic\'; font-size:7.8pt;\"><br /></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'century gothic\'; font-size:16pt; font-weight:600;\">  </span><span style=\" font-size:24px; font-weight:600;\">Strong password has</span><span style=\" font-family:\'century gothic\'; font-size:16pt; font-weight:600;\">:</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'century gothic\'; font-size:7.8pt;\">    </span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'century gothic\'; font-size:12pt;\"> </span><span style=\" font-family:\'century gothic\'; font-size:14pt;\">  </span><span style=\" font-family:\'century gothic\'; font-size:12pt;\">➤ </span><span style=\" font-size:14pt;\">One UPPER case letter </span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'century gothic\'; font-size:12pt;\">   ➤ </span><span style=\" font-size:14pt;\">One lower case letter</span><span style=\" font-size:12pt;\"> </span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'century gothic\'; font-size:12pt;\">   ➤ </span><span style=\" font-size:14pt;\">One number</span></p>\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'century gothic\'; font-size:12pt;\">   ➤ </span><span style=\" font-size:14pt;\">At least 8 characters </span></p>\n"
                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'century gothic\'; font-size:7.8pt;\"><br /></p></body></html>"
                )
            )