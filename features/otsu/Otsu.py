__author__ = 'Server2'

import os
import cv2
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from otsu_options import *
from numpy import *


class Otsu(QMainWindow):
    def __init__(self):
        super(Otsu, self).__init__()
        self.openFile()

    def openFile(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        if self.filename:
            self.otsuOptions()
            self.process_image(str(self.filename))

    def otsuOptions(self):
        self.window = QWidget(None, Qt.WindowSystemMenuHint)
        self.window.setGeometry(15, 30, 0, 0)
        self.ui = Ui_otsuOptions()
        self.ui.setupUi(self.window)
        self.window.show()

    def process_image(self, image_path):
        self.im = cv2.imread(image_path, 0)
        cv2.imshow('Image loaded', self.im)
        self.run()

    def run(self):
        self.otsu = array([])

        while True:
            ch = 0xFF & cv2.waitKey(50)
            if ch == 27:
                break

            if ch in [ord('s'), ord('S')]:
                if self.otsu.any():
                    cv2.imwrite(str(self.filename), self.otsu)
                    print 'Image Saved.'
                    break

            if ch in [ord('a'), ord('A')]:
                newFilename = QFileDialog.getSaveFileName(self, 'Save File As...', os.getenv('HOME'),
                                                          "Images (*.png *.xpm *.jpg)")
                if newFilename:
                    if self.otsu.any():
                        cv2.imwrite(str(newFilename), self.otsu)
                        print 'Image Saved as ' + newFilename
                        break

            if ch in [ord('o'), ord('O')]:
                self.calculateOtsu()

        cv2.destroyAllWindows()

    def calculateOtsu(self):
        ret, self.otsu = cv2.threshold(self.im, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        cv2.imshow('Otsu segmentation', self.otsu)
        print 'Image segmentation using Otsu, threshold = '+ str(ret)
        cv2.waitKey(0)
