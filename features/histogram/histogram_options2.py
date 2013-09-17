# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\histogram_options2.ui'
#
# Created: Sun Sep 15 18:27:02 2013
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

class Ui_histogramOptions(object):
    def setupUi(self, histogramOptions):
        histogramOptions.setObjectName(_fromUtf8("histogramOptions"))
        histogramOptions.resize(320, 161)
        histogramOptions.setMinimumSize(QtCore.QSize(320, 161))
        histogramOptions.setMaximumSize(QtCore.QSize(320, 161))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./icons/Bad-Blood-Yolks-Slow.ico")), QtGui.QIcon.Normal,QtGui.QIcon.Off)
        histogramOptions.setWindowIcon(icon)
        self.textEdit = QtGui.QTextEdit(histogramOptions)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(0, 4, 320, 161))
        self.textEdit.setMinimumSize(QtCore.QSize(320, 161))
        self.textEdit.setMaximumSize(QtCore.QSize(320, 161))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(histogramOptions)
        QtCore.QMetaObject.connectSlotsByName(histogramOptions)

    def retranslateUi(self, histogramOptions):
        histogramOptions.setWindowTitle(_translate("histogramOptions", "Histogram Options", None))
        self.textEdit.setHtml(_translate("histogramOptions", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"> Histogram plotting </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            Keymap :</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            a - show histogram for color image in curve mode </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            b - show histogram in bin mode </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            c - show equalized histogram (always in bin mode) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            d - show histogram for color image in curve mode </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            e - show histogram for a normalized image in curve mode </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            Esc - exit </span></p></body></html>", None))

