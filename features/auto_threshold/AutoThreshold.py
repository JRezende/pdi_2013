__author__ = 'Server2'

import os
import cv2
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from autothreshold_options import *
from numpy import *
from matplotlib import pyplot as plt


class AutoThreshold(QMainWindow):
    def __init__(self):
        super(AutoThreshold, self).__init__()
        self.openFile()

    def openFile(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        if self.filename:
            self.autoThresholdOptions()
            self.process_image(str(self.filename))

    def autoThresholdOptions(self):
        self.window = QWidget(None, Qt.WindowSystemMenuHint)
        self.window.setGeometry(15, 30, 0, 0)
        self.ui = Ui_autoThresholdOptions()
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
                self.calculateAutoThreshold()

        cv2.destroyAllWindows()

    def calculateAutoThreshold(self):
        self.im = cv2.medianBlur(self.im, 5)

        ret, th1 = cv2.threshold(self.im, 127, 255, cv2.THRESH_BINARY)
        th2 = cv2.adaptiveThreshold(self.im, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 1)
        th3 = cv2.adaptiveThreshold(self.im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 1)

        plt.subplot(2, 2, 1), plt.imshow(self.im, 'gray')
        plt.title('Input image:')
        plt.subplot(2, 2, 2), plt.imshow(th1, 'gray')
        plt.title('Global Thresholding')
        plt.subplot(2, 2, 3), plt.imshow(th2, 'gray')
        plt.title('Adaptive Mean Thresholding')
        plt.subplot(2, 2, 4), plt.imshow(th3, 'gray')
        plt.title('Adaptive Gaussian Thresholding')

        plt.show()

        print 'Image segmentation using automatic threshold, global threshold = ' + str(ret)
        plt.show()
        cv2.waitKey(0)
