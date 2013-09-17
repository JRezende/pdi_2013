__author__ = 'Server2'

import os
import cv2
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from resize_options import *
from numpy import *


class Resize(QMainWindow):
    def __init__(self):
        super(Resize, self).__init__()
        self.openFile()

    def openFile(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        if self.filename:
            self.resizeOptions()
            self.process_image(str(self.filename))

    def resizeOptions(self):
        self.window = QWidget(None, Qt.WindowSystemMenuHint)
        self.window.setGeometry(15, 30, 0, 0)
        self.ui = Ui_resizeOptions()
        self.ui.setupUi(self.window)
        self.window.show()

    def process_image(self, image_path):
        self.im = cv2.imread(image_path)
        cv2.imshow('Image loaded', self.im)
        self.run()

    def run(self):
        self.ratio = 100
        self.resize_im = array([])
        while True:
            ch = 0xFF & cv2.waitKey(50)
            if ch == 27:
                break

            if ch in [ord('s'), ord('S')]:
                if self.resize_im.any():
                    cv2.imwrite(str(self.filename), self.resize_im)
                    print 'Image Saved.'
                    break

            if ch in [ord('a'), ord('A')]:
                newFilename = QFileDialog.getSaveFileName(self, 'Save File As...', os.getenv('HOME'),
                                                          "Images (*.png *.xpm *.jpg)")
                if newFilename:
                    if self.resize_im.any():
                        cv2.imwrite(str(newFilename), self.resize_im)
                        print 'Image Saved as ' + newFilename
                        break

            if ch in [ord('r'), ord('R')]:
                ratio, ok = QInputDialog.getText(self, 'Set Image Ratio', 'Type ratio value in % (ex: 80): ')
                if ok:
                    if int(ratio) > 0 and int(ratio) <= 100:
                        self.ratio = int(ratio)
                        self.resizeImage()
                    else:
                        print 'Image scale must be between 1 and 100'

        cv2.destroyAllWindows()

    def resizeImage(self):
        ratio = 100/self.ratio
        newx, newy = self.im.shape[1] / ratio, self.im.shape[0] / ratio  # new size (w,h)
        self.resize_im = cv2.resize(self.im, (newx, newy))
        #cv2.imshow("original image", self.im)
        cv2.imshow("resize image", self.resize_im)
        print 'Image resized'
        cv2.waitKey(0)