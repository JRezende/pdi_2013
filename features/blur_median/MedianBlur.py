__author__ = 'Server2'

import os
import cv2
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from medianblur_options import *
from numpy import *


class MedianBlur(QMainWindow):
    def __init__(self):
        super(MedianBlur, self).__init__()
        self.openFile()

    def openFile(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        if self.filename:
            self.medianBlurOptions()
            self.process_image(str(self.filename))

    def medianBlurOptions(self):
        self.window = QWidget(None, Qt.WindowSystemMenuHint)
        self.window.setGeometry(15, 30, 0, 0)
        self.ui = Ui_medianBlurOptions()
        self.ui.setupUi(self.window)
        self.window.show()

    def process_image(self, image_path):
        self.im = cv2.imread(image_path)
        cv2.imshow('Image loaded', self.im)
        self.run()

    def run(self):
        self.aperture = 3
        self.median_blur = array([])
        while True:
            ch = 0xFF & cv2.waitKey(50)
            if ch == 27:
                break

            if ch in [ord('s'), ord('S')]:
                if self.median_blur.any():
                    cv2.imwrite(str(self.filename), self.median_blur)
                    print 'Image Saved.'
                    break

            if ch in [ord('a'), ord('A')]:
                newFilename = QFileDialog.getSaveFileName(self, 'Save File As...', os.getenv('HOME'),
                                                          "Images (*.png *.xpm *.jpg)")
                if newFilename:
                    if self.median_blur.any():
                        cv2.imwrite(str(newFilename), self.median_blur)
                        print 'Image Saved as ' + newFilename
                        break

            if ch in [ord('p'), ord('P')]:
                aperture, ok = QInputDialog.getText(self, 'Set Aperture Size', 'Type aperture value (ex: 5): ')
                if ok:
                    self.aperture = int(aperture) if int(aperture) % 2 == 1 and int(aperture) >= 0 else 3
                    self.setMedianBlur()

        cv2.destroyAllWindows()

    def setMedianBlur(self):
        self.median_blur = cv2.medianBlur(self.im, self.aperture)
        string = 'Median Blur : aperture - ' + str(self.aperture)
        cv2.putText(self.median_blur, string, (20, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255))
        cv2.imshow('Median Blur', self.median_blur)
        print 'Image blurred using aperture' + str(self.aperture)
        cv2.waitKey(0)