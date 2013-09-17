# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\resize_options.ui'
#
# Created: Mon Sep 16 09:45:34 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_resizeOptions(object):
    def setupUi(self, resizeOptions):
        resizeOptions.setObjectName(_fromUtf8("resizeOptions"))
        resizeOptions.resize(361, 105)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/Bad-Blood-Yolks-On-fire.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        resizeOptions.setWindowIcon(icon)
        self.textEdit = QtGui.QTextEdit(resizeOptions)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 371, 111))
        self.textEdit.setMinimumSize(QtCore.QSize(371, 111))
        self.textEdit.setMaximumSize(QtCore.QSize(371, 111))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(resizeOptions)
        QtCore.QMetaObject.connectSlotsByName(resizeOptions)

    def retranslateUi(self, resizeOptions):
        resizeOptions.setWindowTitle(_translate("resizeOptions", "Resize Image", None))
        self.textEdit.setHtml(_translate("resizeOptions", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Resize Image:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    Keymap:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    r - set image size ratio in %</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    s - save file</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    a - save as...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    Esc - exit</span></p></body></html>", None))

