# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\autothreshold_options.ui'
#
# Created: Mon Sep 16 08:41:33 2013
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

class Ui_autoThresholdOptions(object):
    def setupUi(self, autoThresholdOptions):
        autoThresholdOptions.setObjectName(_fromUtf8("autoThresholdOptions"))
        autoThresholdOptions.resize(267, 80)
        autoThresholdOptions.setMinimumSize(QtCore.QSize(267, 80))
        autoThresholdOptions.setMaximumSize(QtCore.QSize(267, 80))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/Bad-Blood-Yolks-Yarr.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        autoThresholdOptions.setWindowIcon(icon)
        self.textEdit = QtGui.QTextEdit(autoThresholdOptions)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 271, 85))
        self.textEdit.setMinimumSize(QtCore.QSize(271, 85))
        self.textEdit.setMaximumSize(QtCore.QSize(271, 85))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(autoThresholdOptions)
        QtCore.QMetaObject.connectSlotsByName(autoThresholdOptions)

    def retranslateUi(self, autoThresholdOptions):
        autoThresholdOptions.setWindowTitle(_translate("autoThresholdOptions", "Automatic Thresholding", None))
        self.textEdit.setHtml(_translate("autoThresholdOptions", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Image Segmentation using Automatic Threshold:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    Keymap:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    t - compute automatic threshold</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    Esc - exit</span></p></body></html>", None))

