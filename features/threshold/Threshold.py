__author__ = 'Server2'

import os
import cv2
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from threshold_options import *
from numpy import *
from matplotlib import pyplot as plt


class Threshold(QMainWindow):
    def __init__(self):
        super(Threshold, self).__init__()
        self.openFile()

    def openFile(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        if self.filename:
            self.thresholdOptions()
            self.process_image(str(self.filename))

    def thresholdOptions(self):
        self.window = QWidget(None, Qt.WindowSystemMenuHint)
        self.window.setGeometry(15, 30, 0, 0)
        self.ui = Ui_thresholdOptions()
        self.ui.setupUi(self.window)
        self.window.show()

    def process_image(self, image_path):
        self.im = cv2.imread(image_path, 0)
        cv2.imshow('Image loaded', self.im)
        self.run()

    def run(self):
        self.thresholded = array([])

        while True:
            ch = 0xFF & cv2.waitKey(50)
            if ch == 27:
                break

            if ch in [ord('t'), ord('T')]:
                threshold, ok = QInputDialog.getText(self, 'Set Threshold Value ', 'Type threshold value (ex: 127): ')
                if ok:
                    self.threshold = int(threshold) if int(threshold) >= 0 else 127
                    self.calculateThreshold()

        cv2.destroyAllWindows()

    def calculateThreshold(self):
        ret, thresh1 = cv2.threshold(self.im, 127, 255, cv2.THRESH_BINARY)
        ret, thresh2 = cv2.threshold(self.im, 127, 255, cv2.THRESH_BINARY_INV)
        ret, thresh3 = cv2.threshold(self.im, 127, 255, cv2.THRESH_TRUNC)
        ret, thresh4 = cv2.threshold(self.im, 127, 255, cv2.THRESH_TOZERO)
        ret, thresh5 = cv2.threshold(self.im, 127, 255, cv2.THRESH_TOZERO_INV)

        thresh = ['self.im', 'thresh1', 'thresh2', 'thresh3', 'thresh4', 'thresh5']
        titles = ['Original Image', 'Binary Threshold', 'Inverse Binary Threshold', 'Truncated Threshold',
                  'To Zero Threshold', 'To Zero Inverted Threshold']

        for i in xrange(6):
            plt.subplot(2, 3, i + 1), plt.imshow(eval(thresh[i]), 'gray')
            plt.title(titles[i])

        print 'Image segmentation using Otsu, threshold = ' + str(ret)
        plt.show()
        cv2.waitKey(0)
