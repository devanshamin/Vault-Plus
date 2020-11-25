from PyQt5 import QtCore, QtGui, QtWidgets

import src.images

class Demo(object):
    """Display sequence demo GUI to the user."""

    def setupUi(self, Form: QtWidgets.QWidget) -> None:
        """Creates the widget objects in the proper containers and assigns the proper object names to them.
        
        Args:
            Form: Object of QWidget.
        """

        Form.setObjectName("Form")
        #Form.setFixedSize(580, 669)
        Form.setFixedSize(463, 590)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        fg = QtWidgets.QWidget.frameGeometry(Form)
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        Form.move(fg.topLeft())
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        #self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 561, 651))
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 441, 571))
        self.textBrowser_2.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "font-family:Calibri;\n"
            "background: rgba(0,0,0,0.8);\n"
            "font-size:24px;\n"
            "border-radius:15px"
            )
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form: QtWidgets.QWidget) -> None:
        """Sets the text and titles of the widgets.
        
        Args:
            Form: Object of QWidget.
        """

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Vault Plus "))
        self.textBrowser_2.setHtml(
            _translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Calibri\'; font-size:24px; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">	              User Sequence</span><span style=\" font-size:16pt; color:#ff0000;\"> </span></p>\n"
            "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; text-decoration: underline; color:#ffffff;\">Part 1</span></p>\n"
            "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\"> 0:\'A\' | </span><span style=\" font-size:12pt; font-weight:600; color:#00aaff;\">1:\'B\'</span><span style=\" font-size:12pt; color:#ffffff;\"> | 2:\'C\' | </span><span style=\" font-size:12pt; font-weight:600; color:#55ff00;\">3:\'D\'</span><span style=\" font-size:12pt; color:#ffffff;\"> | 4:\'E\' | 5:\'F\' | 6:\'G\' |  7:\'H\' | 8:\'I\' |</span><span style=\" font-size:12pt; color:#000000;\"> </span><span style=\" font-size:12pt; font-weight:600; color:#ff2f2f;\">9:\'J\'</span><span style=\" font-size:12pt; color:#000000;\"> </span></p>\n"
            "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; text-decoration: underline; color:#ffffff;\">Part 2</span></p>\n"
            "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#000000;\"> </span><span style=\" font-size:12pt; color:#ffffff;\">0:\'K\' | </span><span style=\" font-size:12pt; font-weight:600; color:#55ff00;\">1:\'L\'</span><span style=\" font-size:12pt; color:#ffffff;\"> | </span><span style=\" font-size:12pt; font-weight:600; color:#ff2f2f;\">2:\'M\'</span><span style=\" font-size:12pt; color:#000000;\"> </span><span style=\" font-size:12pt; color:#ffffff;\">| 3:\'N\' | 4:\'O\' | </span><span style=\" font-size:12pt; font-weight:600; color:#00aaff;\">5:\'P\'</span><span style=\" font-size:12pt; color:#ffffff;\"> | 6:\'Q\' | 7:\'R\' | 8:\'S\' | 9:\'T\'</span></p>\n"
            "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; text-decoration: underline; color:#ffffff;\">Part 3</span></p>\n"
            "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#000000;\"> </span><span style=\" font-size:12pt; color:#ffffff;\">0:\'U\' | </span><span style=\" font-size:12pt; font-weight:600; color:#55ff00;\">1:\'V\'</span><span style=\" font-size:12pt; color:#55ff00;\"> </span><span style=\" font-size:12pt; color:#ffffff;\">| </span><span style=\" font-size:12pt; font-weight:600; color:#00aaff;\">2:\'W\'</span><span style=\" font-size:12pt; color:#ffffff;\"> | 3:\'X\' | </span><span style=\" font-size:12pt; font-weight:600; color:#ff2f2f;\">4:\'Y\'</span><span style=\" font-size:12pt; color:#ffffff;\"> | 5:\'Z\' </span></p>\n"
            "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">		      Log in</span><span style=\" font-size:8pt; font-weight:600; color:#55ffff;\"> </span><span style=\" font-size:24px;\"> </span></p>\n"
            "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Enter Master Password: </span><span style=\" font-size:12pt; color:#ffffff;\">Example123 </span></p>\n"
            "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">After successfully entering the master password you will receive a random code via email. Every 60 seconds a new code is sent.</span></p>\n"
            "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Your code is </span><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">913-251-421</span></p>\n"
            "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">You will select</span></p>\n"
            "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">• First 3 digits from Part 1</span><span style=\" font-size:14pt; color:#000000;\">    </span><span style=\" font-size:14pt; font-weight:600; color:#ff2f2f;\"> 9</span><span style=\" font-size:14pt; font-weight:600; color:#00aaff;\">1</span><span style=\" font-size:14pt; font-weight:600; color:#55ff00;\">3 </span><span style=\" font-size:14pt; color:#000000;\"> </span><span style=\" font-family:\'Wingdings\'; font-size:14pt;\">à</span><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">  </span><span style=\" font-size:14pt; font-weight:600; color:#ff2f2f;\">J</span><span style=\" font-size:14pt; font-weight:600; color:#00aaff;\">B</span><span style=\" font-size:14pt; font-weight:600; color:#55ff00;\">D</span></p>\n"
            "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">• Next 3 digits from Part 2</span><span style=\" font-size:14pt; color:#ffffff;\"> </span><span style=\" font-size:14pt; color:#000000;\">  </span><span style=\" font-size:14pt; color:#ff2f2f;\"> </span><span style=\" font-size:14pt; font-weight:600; color:#ff2f2f;\">2</span><span style=\" font-size:14pt; font-weight:600; color:#00aaff;\">5</span><span style=\" font-size:14pt; font-weight:600; color:#55ff00;\">1  </span><span style=\" font-family:\'Wingdings\'; font-size:14pt;\">à</span><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">  </span><span style=\" font-size:14pt; font-weight:600; color:#ff2f2f;\">M</span><span style=\" font-size:14pt; font-weight:600; color:#00aaff;\">P</span><span style=\" font-size:14pt; font-weight:600; color:#55ff00;\">L</span></p>\n"
            "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ffffff;\">• Last 3 digits from Part 3</span><span style=\" font-size:14pt; color:#000000;\">     </span><span style=\" font-size:14pt; font-weight:600; color:#ff2f2f;\">4</span><span style=\" font-size:14pt; font-weight:600; color:#00aaff;\">2</span><span style=\" font-size:14pt; font-weight:600; color:#55ff00;\">1  </span><span style=\" font-family:\'Wingdings\'; font-size:14pt;\">à</span><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">  </span><span style=\" font-size:14pt; font-weight:600; color:#ff2f2f;\">Y</span><span style=\" font-size:14pt; font-weight:600; color:#00aaff;\">W</span><span style=\" font-size:14pt; font-weight:600; color:#55ff00;\">V</span></p>\n"
            "<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Enter OTP: </span><span style=\" font-size:14pt; font-weight:600; color:#ff2f2f;\">J</span><span style=\" font-size:14pt; font-weight:600; color:#00aaff;\">B</span><span style=\" font-size:14pt; font-weight:600; color:#55ff00;\">D </span><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\"> </span><span style=\" font-size:14pt; font-weight:600; color:#ff2f2f;\">M</span><span style=\" font-size:14pt; font-weight:600; color:#00aaff;\">P</span><span style=\" font-size:14pt; font-weight:600; color:#55ff00;\">L </span><span style=\" font-size:14pt; font-weight:600; color:#ff2f2f;\">Y</span><span style=\" font-size:14pt; font-weight:600; color:#00aaff;\">W</span><span style=\" font-size:14pt; font-weight:600; color:#55ff00;\">V</span><span style=\" font-size:24px;\"> </span></p></body></html>")
            )