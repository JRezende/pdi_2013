__author__ = 'Server2'

import os
import cv2
import numpy as np
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from features.to_gray.grayscale_options import *


class GrayScale(QMainWindow):
    def __init__(self):
        super(GrayScale, self).__init__()
        self.openFile()

    def openFile(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        if self.filename:
            self.grayScaleOptions()
            self.process_image(str(self.filename))

    def grayScaleOptions(self):
        self.window = QWidget(None, Qt.WindowSystemMenuHint)
        self.window.setGeometry(15, 30, 0, 0)
        self.ui = Ui_grayScaleOptions()
        self.ui.setupUi(self.window)
        self.window.show()

    def process_image(self, image_path):
        self.im = cv2.imread(image_path)
        self.gray = cv2.cvtColor(self.im, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('Image loaded', self.im)
        cv2.imshow('Image in gray scale', self.gray)
        self.run()

    def run(self):
        while True:
            ch = 0xFF & cv2.waitKey(50)
            if ch == 27:
                break
            if ch in [ord('s'), ord('S')]:
                cv2.imwrite(str(self.filename), self.gray)
                print 'Image Saved.'
                break
            if ch in [ord('a'), ord('A')]:
                newFilename = QFileDialog.getSaveFileName(self, 'Save File As...', os.getenv('HOME'),
                                                          "Images (*.png *.xpm *.jpg)")
                if newFilename:
                    cv2.imwrite(str(newFilename), self.gray)
                    print 'Image Saved as ' + newFilename
                    break
        cv2.destroyAllWindows()

