# coding: utf-8

import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from features.sharp_laplace import LaplaceSharp
from features.threshold import Threshold
from main.main_window import *
from features.histogram.Histogram import *
from features.watershed.Watershed import *
from features.to_gray.GrayScale import *
from features.blur_gaussian.GaussianBlur import *
from features.blur_mean.MeanBlur import *
from features.blur_median.MedianBlur import *
from features.sharp_laplace.LaplaceSharp import *
from features.otsu.Otsu import *
from features.threshold.Threshold import *
from features.auto_threshold.AutoThreshold import *
from features.high_resolution.HighRes import *
from features.resize.Resize import *
from about import *


class MainWindow:

    def exit2(self):
        quit()

    def about(self):
        About(parent=self.window)

    def process_histogram(self):
        Histogram()

    def process_watershed(self):
        Watershed()

    def process_gray_scale(self):
        GrayScale()

    def process_gaussian_filter(self):
        GaussianBlur()

    def process_mean_filter(self):
        MeanBlur()

    def process_median_filter(self):
        MedianBlur()

    def process_laplace_sharp(self):
        LaplaceSharp()

    def process_otsu(self):
        Otsu()

    def process_threshold(self):
        Threshold()

    def process_auto_threshold(self):
        AutoThreshold()

    def process_high_resolution(self):
        HighRes()

    def process_resize(self):
        Resize()

    def __init__(self):
        #init main window
        self.app = QApplication(sys.argv)
        #self.window = QDialog(None, Qt.WindowSystemMenuHint)
        self.window = QWidget(None, Qt.WindowSystemMenuHint)
        self.window.setGeometry(50, 50, 0, 0)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)

        #set events to primary buttons
        self.window.connect(self.ui.pushButton_2, SIGNAL('clicked()'), self.exit2)
        self.window.connect(self.ui.pushButton, SIGNAL('clicked()'), self.about)

        self.window.connect(self.ui.btn_histogram, SIGNAL('clicked()'), self.process_histogram)
        self.window.connect(self.ui.btn_watershed, SIGNAL('clicked()'), self.process_watershed)
        self.window.connect(self.ui.btn_to_gray_scale, SIGNAL('clicked()'), self.process_gray_scale)
        self.window.connect(self.ui.btn_gaussian_filter, SIGNAL('clicked()'), self.process_gaussian_filter)
        self.window.connect(self.ui.btn_mean_filter, SIGNAL('clicked()'), self.process_mean_filter)
        self.window.connect(self.ui.btn_median_filter, SIGNAL('clicked()'), self.process_median_filter)
        self.window.connect(self.ui.bnt_laplacian, SIGNAL('clicked()'), self.process_laplace_sharp)
        self.window.connect(self.ui.btn_otsu, SIGNAL('clicked()'), self.process_otsu)
        self.window.connect(self.ui.btn_threshold, SIGNAL('clicked()'), self.process_threshold)
        self.window.connect(self.ui.btn_auto_threshold, SIGNAL('clicked()'), self.process_auto_threshold)
        self.window.connect(self.ui.commandLinkButton_10, SIGNAL('clicked()'), self.process_high_resolution)
        self.window.connect(self.ui.commandLinkButton_12, SIGNAL('clicked()'), self.process_resize)

        #run the main window
        self.window.show()
        sys.exit(self.app.exec_())

#if __name__ == '__main__': MainWindow()