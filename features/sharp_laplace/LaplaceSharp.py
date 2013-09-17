__author__ = 'Server2'

import os
import cv2
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from laplacesharp_options import *
from numpy import *


class LaplaceSharp(QMainWindow):
    def __init__(self):
        super(LaplaceSharp, self).__init__()
        self.openFile()

    def openFile(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        if self.filename:
            self.laplaceSharpOptions()
            self.process_image(str(self.filename))

    def laplaceSharpOptions(self):
        self.window = QWidget(None, Qt.WindowSystemMenuHint)
        self.window.setGeometry(15, 30, 0, 0)
        self.ui = Ui_laplaceSharpOptions()
        self.ui.setupUi(self.window)
        self.window.show()

    def process_image(self, image_path):
        self.im = cv2.imread(image_path)
        cv2.imshow('Image loaded', self.im)
        self.run()

    def run(self):
        self.aperture = 3
        self.scale = 1
        self.laplace_sharp = array([])
        self.ddepth = cv2.CV_16S

        while True:
            ch = 0xFF & cv2.waitKey(50)
            if ch == 27:
                break

            if ch in [ord('s'), ord('S')]:
                if self.laplace_sharp.any():
                    cv2.imwrite(str(self.filename), self.laplace_sharp)
                    print 'Image Saved.'
                    break

            if ch in [ord('a'), ord('A')]:
                newFilename = QFileDialog.getSaveFileName(self, 'Save File As...', os.getenv('HOME'),
                                                          "Images (*.png *.xpm *.jpg)")
                if newFilename:
                    if self.laplace_sharp.any():
                        cv2.imwrite(str(newFilename), self.laplace_sharp)
                        print 'Image Saved as ' + newFilename
                        break

            if ch in [ord('p'), ord('P')]:
                aperture, ok = QInputDialog.getText(self, 'Set Aperture Size', 'Type aperture value (ex: 3): ')
                if ok:
                    self.aperture = int(aperture) if int(aperture) % 2 == 1 and int(aperture) >= 0 else 3
                    self.setLaplaceSharp()

            if ch in [ord('c'), ord('C')]:
                scale, ok = QInputDialog.getText(self, 'Set Scale', 'Type scale value (ex: 1): ')
                if ok:
                    self.scale = int(scale)
                    self.setLaplaceSharp()
        cv2.destroyAllWindows()

    def setLaplaceSharp(self):
        self.im = cv2.GaussianBlur(self.im, (self.aperture, self.aperture), self.scale)
        gray = cv2.cvtColor(self.im, cv2.COLOR_BGR2GRAY)
        laplace_sharp = cv2.Laplacian(gray, self.ddepth, ksize=self.aperture, scale=self.scale)
        self.laplace_sharp = cv2.convertScaleAbs(laplace_sharp)
        cv2.imshow('Laplacian Sharpening', self.laplace_sharp)
        print 'Image sharpening using laplacian'
        cv2.waitKey(0)
