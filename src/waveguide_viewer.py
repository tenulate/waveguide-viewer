''' combines qt designer generated class files and program logic class files
    to produce single mode wave guide viewer '''

# import the main window from the pyuic4 converted .ui file    
from qtdesigner import Ui_WaveguideViewer_MainWindow

# for coaxial modes logic
from coaxial_modes import TMmode, TEmode

# Numpy module
import numpy as np

# for command-line arguments
import sys
# Qt4 bindings for core Qt functionalities (non-GUI)
from PyQt4 import QtCore
# Python Qt4 bindings for GUI objects
from PyQt4 import QtGui

class WaveGuideViewer(QtGui.QMainWindow, Ui_WaveguideViewer_MainWindow):
    '''Integrate Qt designer created window with program logic'''
    
    def __init__(self, parent = None):
        # Initialize the super class
        super(WaveGuideViewer, self).__init__()
        # set up the windows / user interfaces created in qtdesigner
        self.setupUi(self)
        
        # canvas / axis / figures
        self.canvas = self.mpl_rootFinder.canvas
        self.ax = self.canvas.ax
        
        # set up the initial wave guide mode
        self.set_waveguide_mode()
        self.plot_root()
        
        # connect the signals and slots (buttons with functions)
        QtCore.QObject.connect(self.recalculateRoot_pushButton, QtCore.
                               SIGNAL('clicked()'), self.click_recalculate_root)
        QtCore.QObject.connect(self.mode_OKButton, 
                               QtCore.SIGNAL('clicked()'), self.click_mode_ok)
        QtCore.QObject.connect(self.mode_CancelButton, QtCore.
                               SIGNAL('clicked()'), self.click_mode_cancel)
        
    def set_waveguide_mode(self):
        ''' using the m, n and c values the user has selected from the spin boxes,
            saves the waveguide mode '''
        
        try:
            del(self.mode)
            print self.mode
            print 'hi'
        except:
            pass
        
        m = self.m_spinBox.value()
        n = self.n_spinBox.value()
        c = self.c_doubleSpinBox.value()
        index = self.mode_comboBox.currentIndex()
        
        if index == 0:
            self.mode = TEmode(m,n,c)
        elif index == 1:
            self.mode = TMmode(m,n,c)
        else:
            self.mode = TEmode(m,n,c)
    
    def plot_root(self):
        ''' plots the radial root equation in the root equation axis '''
        self.ax.clear()
        self.mode.plot_root_equation(self.ax)
        self.mode.plot_root(self.ax)
    
    def click_recalculate_root(self):
        ''' what to do when recalculate root is clicked '''
        self.mode.recalculate_root()
        self.plot_root()
        
    def click_mode_ok(self):
        ''' what to do when clicking "OK" for the mode selection screen '''
        
        # disconnect the previous signal / slot for the old mode
        QtCore.QObject.disconnect(self.recalculateRoot_pushButton, 
                                  QtCore.SIGNAL('clicked()'), 
                                  self.mode.recalculate_root)
        # need to disconnect the matplotlib calls for mode
        self.mode.drag.disconnect()
        
        # update the mode info, and plot new radial equation
        self.set_waveguide_mode()
        
        # connect signal / slot for the new updated mode
        QtCore.QObject.connect(self.recalculateRoot_pushButton, QtCore.
                               SIGNAL('clicked()'), self.mode.recalculate_root)
        
        # change the open tabbed window
        self.tabWidget.setCurrentIndex(1)
        
        # plot this new root data
        self.plot_root()
        
    def click_mode_cancel(self):
        ''' what to do when clicking on the "cancel" button for the mode selection screen 
            - restore the m, n, c, mode type values in the combo/spin boxes '''
        m, n, c, mode_type = self.mode.m, self.mode.n, self.mode.c, self.mode.mode
        
        # set the spin boxes
        self.m_spinBox.setValue(m)
        self.n_spinBox.setValue(n)
        self.c_doubleSpinBox.setValue(c)
        
        # set the combo box
        if mode_type == 'TE':
            self.mode_comboBox.setCurrentIndex(0)
        elif mode_type == 'TM':
            self.mode_comboBox.setCurrentIndex(1)
        else:
            self.mode_comboBox.setCurrentIndex(2)
        
          
if __name__ == '__main__':
    # create the GUI application
    app = QtGui.QApplication(sys.argv)
    # instantiate the main window
    wgv = WaveGuideViewer()
    # show it
    wgv.show()
    # start the Qt main loop execution, exiting from this script
    # with the same return code of Qt application
    sys.exit(app.exec_())