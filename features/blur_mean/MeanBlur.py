__author__ = 'Server2'

import os
import cv2
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from meanblur_options import *
from numpy import *


class MeanBlur(QMainWindow):
    def __init__(self):
        super(MeanBlur, self).__init__()
        self.openFile()

    def openFile(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        if self.filename:
            self.meanBlurOptions()
            self.process_image(str(self.filename))

    def meanBlurOptions(self):
        self.window = QWidget(None, Qt.WindowSystemMenuHint)
        self.window.setGeometry(15, 30, 0, 0)
        self.ui = Ui_meanBlurOptions()
        self.ui.setupUi(self.window)
        self.window.show()

    def process_image(self, image_path):
        self.im = cv2.imread(image_path)
        cv2.imshow('Image loaded', self.im)
        self.run()

    def run(self):
        self.kernel = (3, 3)
        self.mean_blur = array([])
        while True:
            ch = 0xFF & cv2.waitKey(50)
            if ch == 27:
                break

            if ch in [ord('s'), ord('S')]:
                if self.mean_blur.any():
                    cv2.imwrite(str(self.filename), self.mean_blur)
                    print 'Image Saved.'
                    break

            if ch in [ord('a'), ord('A')]:
                newFilename = QFileDialog.getSaveFileName(self, 'Save File As...', os.getenv('HOME'),
                                                          "Images (*.png *.xpm *.jpg)")
                if newFilename:
                    if self.mean_blur.any():
                        cv2.imwrite(str(newFilename), self.mean_blur)
                        print 'Image Saved as ' + newFilename
                        break

            if ch in [ord('k'), ord('K')]:
                kernel, ok = QInputDialog.getText(self, 'Set Kernel Value', 'Type Kernel value (ex: 5): ')
                if ok:
                    self.kernel = (int(kernel), int(kernel)) if int(kernel) % 2 == 1 and int(kernel) >= 0 else (3, 3)
                    self.setMeanBlur()

        cv2.destroyAllWindows()

    def setMeanBlur(self):
        self.mean_blur = cv2.blur(self.im, self.kernel)
        string = 'Mean Blur : kernel_size - ' + str(self.kernel)
        cv2.putText(self.mean_blur, string, (20, 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255))
        cv2.imshow('Mean Blur', self.mean_blur)
        print 'Image blurred using kernel' + str(self.kernel)
        cv2.waitKey(0)