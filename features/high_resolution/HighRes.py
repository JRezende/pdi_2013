__author__ = 'Server2'

import os
import cv2
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class HighRes(QMainWindow):
    def __init__(self):
        super(HighRes, self).__init__()
        self.openFile()

    def openFile(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        if self.filename:
            self.process_image(str(self.filename))

    def process_image(self, image_path):
        self.im = cv2.imread(image_path)

        self.small = self.im
        for i in xrange(3):
            self.small = cv2.pyrDown(self.small)

        def onmouse(event, x, y, flags, param):
            h, w = self.im.shape[:2]
            h1, w1 = self.small.shape[:2]
            x, y = 1.0 * x * h / h1, 1.0 * y * h / h1
            zoom = cv2.getRectSubPix(self.im, (800, 600), (x + 0.5, y + 0.5))
            cv2.imshow('zoom', zoom)

        cv2.imshow('Preview', self.small)
        cv2.setMouseCallback('Preview', onmouse)
        cv2.waitKey()
        cv2.destroyAllWindows()