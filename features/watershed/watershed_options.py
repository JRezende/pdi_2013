# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\watershed_options.ui'
#
# Created: Sun Sep 15 18:50:43 2013
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

class Ui_watershedOptions(object):
    def setupUi(self, watershedOptions):
        watershedOptions.setObjectName(_fromUtf8("watershedOptions"))
        watershedOptions.setEnabled(False)
        watershedOptions.resize(340, 120)
        watershedOptions.setMinimumSize(QtCore.QSize(340, 120))
        watershedOptions.setMaximumSize(QtCore.QSize(340, 120))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./icons/Bad-Blood-Yolks-Evilish.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        watershedOptions.setWindowIcon(icon)
        self.textEdit = QtGui.QTextEdit(watershedOptions)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 341, 121))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(watershedOptions)
        QtCore.QMetaObject.connectSlotsByName(watershedOptions)

    def retranslateUi(self, watershedOptions):
        watershedOptions.setWindowTitle(_translate("watershedOptions", "Watershed", None))
        self.textEdit.setHtml(_translate("watershedOptions", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Watershed segmentation</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    Keymap:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">     1-7              - switch marker color</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">     SPACE         - update segmentation</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">     r                  - reset</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">     a                 - toggle autoupdate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">    ESC              - exit</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))

