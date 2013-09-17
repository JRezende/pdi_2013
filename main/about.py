__author__ = 'Server2'

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from about_window import *
import cv2


class About(QMainWindow):

    def __init__(self, parent=None):
        super(About, self).__init__()
        self.window = QDialog(parent, Qt.WindowSystemMenuHint)
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
