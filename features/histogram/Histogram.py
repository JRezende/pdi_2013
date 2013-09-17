__author__ = 'Server2'

import os
import cv2

from PyQt4 import QtGui
import numpy as np

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from features.histogram.histogram_options2 import *


bins = np.arange(256).reshape(256, 1)


class Histogram(QtGui.QMainWindow):
    def __init__(self):
        super(Histogram, self).__init__()
        self.openFile()

    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        if filename:
            self.histogramOptions()
            self.process_image(str(filename))

    def histogramOptions(self):
        self.window = QWidget(None, Qt.WindowSystemMenuHint)
        self.window.setGeometry(15, 30, 0, 0)
        self.ui = Ui_histogramOptions()
        self.ui.setupUi(self.window)
        self.window.show()

    def close(self):
        self.close()

#METHODS BELLOW ARE FROM PYTHON CV2 SAMPLES
    def hist_curve(self, im):
        h = np.zeros((300, 256, 3))
        if len(im.shape) == 2:
            color = [(255, 255, 255)]
        elif im.shape[2] == 3:
            color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        for ch, col in enumerate(color):
            hist_item = cv2.calcHist([im], [ch], None, [256], [0, 256])
            cv2.normalize(hist_item, hist_item, 0, 255, cv2.NORM_MINMAX)
            hist = np.int32(np.around(hist_item))
            pts = np.int32(np.column_stack((bins, hist)))
            cv2.polylines(h, [pts], False, col)
        y = np.flipud(h)
        return y

    def hist_lines(self, im):
        h = np.zeros((300, 256, 3))
        if len(im.shape) != 2:
            print "hist_lines applicable only for grayscale images"
            print "so converting image to grayscale for representation"
            im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        hist_item = cv2.calcHist([im], [0], None, [256], [0, 256])
        cv2.normalize(hist_item, hist_item, 0, 255, cv2.NORM_MINMAX)
        hist = np.int32(np.around(hist_item))
        for x, y in enumerate(hist):
            cv2.line(h, (x, 0), (x, y), (255, 255, 255))
        y = np.flipud(h)
        return y

    def process_image(self, image_path):
        im = cv2.imread(image_path)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.imshow('image', im)
        while True:
            k = cv2.waitKey(0) & 0xFF
            if k == ord('a'):
                curve = self.hist_curve(im)
                cv2.imshow('histogram', curve)
                cv2.imshow('image', im)
                print 'a'
            elif k == ord('b'):
                print 'b'
                lines = self.hist_lines(im)
                cv2.imshow('histogram', lines)
                cv2.imshow('image', gray)
            elif k == ord('c'):
                print 'c'
                equ = cv2.equalizeHist(gray)
                lines = self.hist_lines(equ)
                cv2.imshow('histogram', lines)
                cv2.imshow('image', equ)
            elif k == ord('d'):
                print 'd'
                curve = self.hist_curve(gray)
                cv2.imshow('histogram', curve)
                cv2.imshow('image', gray)
            elif k == ord('e'):
                print 'e'
                norm = cv2.normalize(gray, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
                lines = self.hist_lines(norm)
                cv2.imshow('histogram', lines)
                cv2.imshow('image', norm)
            elif k == 27:
                print 'ESC'
                cv2.destroyAllWindows()
                break

        cv2.destroyAllWindows()