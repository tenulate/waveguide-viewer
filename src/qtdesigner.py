# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'waveguide viewer.ui'
#
# Created: Mon Jul 16 00:57:09 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_WaveguideViewer_MainWindow(object):
    def setupUi(self, WaveguideViewer_MainWindow):
        WaveguideViewer_MainWindow.setObjectName(_fromUtf8("WaveguideViewer_MainWindow"))
        WaveguideViewer_MainWindow.resize(769, 618)
        self.centralwidget = QtGui.QWidget(WaveguideViewer_MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setMargin(1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.selectMode_tab = QtGui.QWidget()
        self.selectMode_tab.setObjectName(_fromUtf8("selectMode_tab"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.selectMode_tab)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.textBrowser = QtGui.QTextBrowser(self.selectMode_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QtCore.QSize(300, 16777215))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.horizontalLayout.addWidget(self.textBrowser)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.mode_comboBox = QtGui.QComboBox(self.selectMode_tab)
        self.mode_comboBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.mode_comboBox.setObjectName(_fromUtf8("mode_comboBox"))
        self.mode_comboBox.addItem(_fromUtf8(""))
        self.mode_comboBox.addItem(_fromUtf8(""))
        self.mode_comboBox.addItem(_fromUtf8(""))
        self.verticalLayout_3.addWidget(self.mode_comboBox)
        spacerItem = QtGui.QSpacerItem(20, 60, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.selectMode_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(20, 0))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.m_spinBox = QtGui.QSpinBox(self.selectMode_tab)
        self.m_spinBox.setMinimumSize(QtCore.QSize(67, 0))
        self.m_spinBox.setMaximum(100)
        self.m_spinBox.setObjectName(_fromUtf8("m_spinBox"))
        self.horizontalLayout_2.addWidget(self.m_spinBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.selectMode_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(20, 0))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.n_spinBox = QtGui.QSpinBox(self.selectMode_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.n_spinBox.sizePolicy().hasHeightForWidth())
        self.n_spinBox.setSizePolicy(sizePolicy)
        self.n_spinBox.setMinimumSize(QtCore.QSize(67, 0))
        self.n_spinBox.setMinimum(1)
        self.n_spinBox.setMaximum(100)
        self.n_spinBox.setObjectName(_fromUtf8("n_spinBox"))
        self.horizontalLayout_3.addWidget(self.n_spinBox)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.selectMode_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(20, 0))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.c_doubleSpinBox = QtGui.QDoubleSpinBox(self.selectMode_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c_doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.c_doubleSpinBox.setSizePolicy(sizePolicy)
        self.c_doubleSpinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.c_doubleSpinBox.setMinimum(1.01)
        self.c_doubleSpinBox.setMaximum(10.0)
        self.c_doubleSpinBox.setSingleStep(0.1)
        self.c_doubleSpinBox.setProperty("value", 3.0)
        self.c_doubleSpinBox.setObjectName(_fromUtf8("c_doubleSpinBox"))
        self.horizontalLayout_4.addWidget(self.c_doubleSpinBox)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.mode_CancelButton = QtGui.QPushButton(self.selectMode_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mode_CancelButton.sizePolicy().hasHeightForWidth())
        self.mode_CancelButton.setSizePolicy(sizePolicy)
        self.mode_CancelButton.setMinimumSize(QtCore.QSize(50, 0))
        self.mode_CancelButton.setObjectName(_fromUtf8("mode_CancelButton"))
        self.horizontalLayout_7.addWidget(self.mode_CancelButton)
        spacerItem5 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.mode_OKButton = QtGui.QPushButton(self.selectMode_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mode_OKButton.sizePolicy().hasHeightForWidth())
        self.mode_OKButton.setSizePolicy(sizePolicy)
        self.mode_OKButton.setMinimumSize(QtCore.QSize(50, 0))
        self.mode_OKButton.setObjectName(_fromUtf8("mode_OKButton"))
        self.horizontalLayout_7.addWidget(self.mode_OKButton)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem7)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.selectMode_tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(200, 0))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.horizontalLayout_5.addWidget(self.textBrowser_2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalSlider = QtGui.QSlider(self.tab_2)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setSliderPosition(50)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(False)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.horizontalLayout_9.addWidget(self.verticalSlider)
        self.mpl_rootFinder = MplWidget(self.tab_2)
        self.mpl_rootFinder.setMinimumSize(QtCore.QSize(500, 500))
        self.mpl_rootFinder.setObjectName(_fromUtf8("mpl_rootFinder"))
        self.horizontalLayout_9.addWidget(self.mpl_rootFinder)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_2)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.recalculateRoot_pushButton = QtGui.QPushButton(self.tab_2)
        self.recalculateRoot_pushButton.setObjectName(_fromUtf8("recalculateRoot_pushButton"))
        self.horizontalLayout_6.addWidget(self.recalculateRoot_pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        WaveguideViewer_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(WaveguideViewer_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        WaveguideViewer_MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(WaveguideViewer_MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(WaveguideViewer_MainWindow)

    def retranslateUi(self, WaveguideViewer_MainWindow):
        WaveguideViewer_MainWindow.setWindowTitle(QtGui.QApplication.translate("WaveguideViewer_MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("WaveguideViewer_MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Select your waveguide mode:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Modes in a coaxial waveguide come in 3 types</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">TE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">The </span><span style=\" font-size:10pt; font-style:italic;\">electric field</span><span style=\" font-size:10pt;\"> is tansverse to the direction of the wave</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">TM</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">Magnetic field</span><span style=\" font-size:10pt;\"> is transverse</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">TEM</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Both the </span><span style=\" font-size:10pt; font-style:italic;\">electric and magnetic fields</span><span style=\" font-size:10pt;\"> are transverse</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Each type (excluding TEM) has infinitely many modes, referred to by its </span><span style=\" font-size:10pt; font-weight:600;\">m and n</span><span style=\" font-size:10pt;\"> values.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">m</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Number of nodes (zeros of field) around the circumference of annulus </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">(m = 0,1,2,3...)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">n</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Number of nodes minus one, from inner to outter radius </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">(n = 1,2,3,4...)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">c</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">ratio of outter radius to inner radius of waveguide</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">(c &gt; 1)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.mode_comboBox.setItemText(0, QtGui.QApplication.translate("WaveguideViewer_MainWindow", "TE (Transverse Electric)", None, QtGui.QApplication.UnicodeUTF8))
        self.mode_comboBox.setItemText(1, QtGui.QApplication.translate("WaveguideViewer_MainWindow", "TM (Transverse Magnetic)", None, QtGui.QApplication.UnicodeUTF8))
        self.mode_comboBox.setItemText(2, QtGui.QApplication.translate("WaveguideViewer_MainWindow", "TEM (Transverse Electric-Magnetic)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("WaveguideViewer_MainWindow", "m", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("WaveguideViewer_MainWindow", "n", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("WaveguideViewer_MainWindow", "c", None, QtGui.QApplication.UnicodeUTF8))
        self.mode_CancelButton.setText(QtGui.QApplication.translate("WaveguideViewer_MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.mode_OKButton.setText(QtGui.QApplication.translate("WaveguideViewer_MainWindow", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.selectMode_tab), QtGui.QApplication.translate("WaveguideViewer_MainWindow", "Select Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_2.setHtml(QtGui.QApplication.translate("WaveguideViewer_MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Calculate Waveguide Root</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">The tangential part of the electric field is required to be zero at a perfectly conducting metallic boundary. For given  values of </span><span style=\" font-size:10pt; font-weight:600;\">c</span><span style=\" font-size:10pt;\"> and </span><span style=\" font-size:10pt; font-weight:600;\">n</span><span style=\" font-size:10pt;\">, a unique root (reffered to by the Greek letter </span><span style=\" font-size:10pt; font-style:italic;\">chi</span><span style=\" font-size:10pt;\">) is needed to ensure the zero boundary condition.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">For a given value of </span><span style=\" font-size:10pt; font-weight:600;\">n</span><span style=\" font-size:10pt;\">, </span><span style=\" font-size:10pt; font-style:italic;\">chi</span><span style=\" font-size:10pt;\"> should be the n</span><span style=\" font-size:10pt; vertical-align:super;\">th</span><span style=\" font-size:10pt;\"> root of the graph. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Click and drag the root of the graph to correct it, then click &quot;recalculate root&quot;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("WaveguideViewer_MainWindow", "Less X-Axis Points", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("WaveguideViewer_MainWindow", "More X-Axis points", None, QtGui.QApplication.UnicodeUTF8))
        self.recalculateRoot_pushButton.setText(QtGui.QApplication.translate("WaveguideViewer_MainWindow", "Recalculate Root", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("WaveguideViewer_MainWindow", "Calculate Root", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("WaveguideViewer_MainWindow", "Page", None, QtGui.QApplication.UnicodeUTF8))

from mplwidget import MplWidget
