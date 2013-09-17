# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\laplacesharp_options.ui'
#
# Created: Mon Sep 16 01:54:24 2013
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

class Ui_laplaceSharpOptions(object):
    def setupUi(self, laplaceSharpOptions):
        laplaceSharpOptions.setObjectName(_fromUtf8("laplaceSharpOptions"))
        laplaceSharpOptions.resize(378, 109)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/Bad-Blood-Yolks-Wut.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        laplaceSharpOptions.setWindowIcon(icon)
        self.textEdit = QtGui.QTextEdit(laplaceSharpOptions)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 381, 111))
        self.textEdit.setMinimumSize(QtCore.QSize(381, 111))
        self.textEdit.setMaximumSize(QtCore.QSize(381, 111))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(laplaceSharpOptions)
        QtCore.QMetaObject.connectSlotsByName(laplaceSharpOptions)

    def retranslateUi(self, laplaceSharpOptions):
        laplaceSharpOptions.setWindowTitle(_translate("laplaceSharpOptions", "Laplace Sharpening", None))
        self.textEdit.setHtml(_translate("laplaceSharpOptions", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Set Laplacian Sharpening to Image:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    Keymap:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    p - choose aperture size (must be positive and odd)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    c - choose scale value</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    s - save file</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    a - save as...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    Esc - exit</span></p></body></html>", None))

