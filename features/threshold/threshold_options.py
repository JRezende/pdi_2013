# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\threshold_options.ui'
#
# Created: Mon Sep 16 03:24:37 2013
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

class Ui_thresholdOptions(object):
    def setupUi(self, thresholdOptions):
        thresholdOptions.setObjectName(_fromUtf8("thresholdOptions"))
        thresholdOptions.resize(221, 83)
        thresholdOptions.setMinimumSize(QtCore.QSize(221, 83))
        thresholdOptions.setMaximumSize(QtCore.QSize(221, 83))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/Bad-Blood-Yolks-Angry.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        thresholdOptions.setWindowIcon(icon)
        self.textEdit = QtGui.QTextEdit(thresholdOptions)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 221, 85))
        self.textEdit.setMinimumSize(QtCore.QSize(221, 85))
        self.textEdit.setMaximumSize(QtCore.QSize(221, 85))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(thresholdOptions)
        QtCore.QMetaObject.connectSlotsByName(thresholdOptions)

    def retranslateUi(self, thresholdOptions):
        thresholdOptions.setWindowTitle(_translate("thresholdOptions", "Thresholding", None))
        self.textEdit.setHtml(_translate("thresholdOptions", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Image Segmentation using Threshold:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    Keymap:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    t - give threshold value</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    Esc - exit</span></p></body></html>", None))

