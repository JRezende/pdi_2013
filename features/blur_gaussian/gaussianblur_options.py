# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gaussianblur_options.ui'
#
# Created: Sun Sep 15 20:38:18 2013
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

class Ui_gaussianBlurOptions(object):
    def setupUi(self, gaussianBlurOptions):
        gaussianBlurOptions.setObjectName(_fromUtf8("gaussianBlurOptions"))
        gaussianBlurOptions.resize(371, 107)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/Bad-Blood-Yolks-Want.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        gaussianBlurOptions.setWindowIcon(icon)
        self.textEdit = QtGui.QTextEdit(gaussianBlurOptions)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 371, 111))
        self.textEdit.setMinimumSize(QtCore.QSize(371, 111))
        self.textEdit.setMaximumSize(QtCore.QSize(371, 111))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(gaussianBlurOptions)
        QtCore.QMetaObject.connectSlotsByName(gaussianBlurOptions)

    def retranslateUi(self, gaussianBlurOptions):
        gaussianBlurOptions.setWindowTitle(_translate("gaussianBlurOptions", "Gaussian Blur", None))
        self.textEdit.setHtml(_translate("gaussianBlurOptions", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Set Gaussian Blur to Image:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    Keymap:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    i - choose sigma value</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    k - choose kernel size (must be positive and odd)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    s - save file</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    a - save as...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    Esc - exit</span></p></body></html>", None))

