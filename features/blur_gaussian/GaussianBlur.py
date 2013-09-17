__author__ = 'Server2'

import os
import cv2
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from gaussianblur_options import *
from numpy import *


class GaussianBlur(QMainWindow):
    def __init__(self):
        super(GaussianBlur, self).__init__()
        self.openFile()

    def openFile(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        if self.filename:
            self.gaussianBlurOptions()
            self.process_image(str(self.filename))

    def gaussianBlurOptions(self):
        self.window = QWidget(None, Qt.WindowSystemMenuHint)
        self.window.setGeometry(15, 30, 0, 0)
        self.ui = Ui_gaussianBlurOptions()
        self.ui.setupUi(self.window)
        self.window.show()

    def process_image(self, image_path):
        self.im = cv2.imread(image_path)
        cv2.imshow('Image loaded', self.im)
        self.run()

    def run(self):
        self.sigma = 0.0
        self.kernel = (3, 3)
        self.gaussian_blur = array([])
        while True:
            ch = 0xFF & cv2.waitKey(50)
            if ch == 27:
                break

            if ch in [ord('s'), ord('S')]:
                if self.gaussian_blur.any():
                    cv2.imwrite(str(self.filename), self.gaussian_blur)
                    print 'Image Saved.'
                    break

            if ch in [ord('a'), ord('A')]:
                newFilename = QFileDialog.getSaveFileName(self, 'Save File As...', os.getenv('HOME'),
                                                          "Images (*.png *.xpm *.jpg)")
                if newFilename:
                    if self.gaussian_blur.any():
                        cv2.imwrite(str(newFilename), self.gaussian_blur)
                        print 'Image Saved as ' + newFilename
                        break

            if ch in [ord('i'), ord('I')]:
                sigma, ok = QInputDialog.getText(self, 'Set Sigma Value', 'Type Sigma value (ex: 0.3): ')
                if ok:
                    self.sigma = float(sigma)
                    self.setGaussianBlur()

            if ch in [ord('k'), ord('K')]:
                kernel, ok = QInputDialog.getText(self, 'Set Kernel Value', 'Type Kernel value (ex: 5): ')
                if ok:
                    self.kernel = (int(kernel), int(kernel)) if int(kernel) % 2 == 1 and int(kernel) >= 0 else (3, 3)
                    self.setGaussianBlur()

        cv2.destroyAllWindows()

    def setGaussianBlur(self):
        self.gaussian_blur = cv2.GaussianBlur(self.im, self.kernel, self.sigma)
        string = 'Gaussian Blur : kernel_size - ' + str(self.kernel) + 'sigma -  ' + str(self.sigma)
        cv2.putText(self.gaussian_blur, string, (20, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255))
        cv2.imshow('Gaussian Blur', self.gaussian_blur)
        print 'Image blurred using kernel' + str(self.kernel) + ' and sigma = ' + str(self.sigma)
        cv2.waitKey(0)