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
        
        self.mode = TEmode(4,1,4)
        self.mode.plot_root_equation(ax = self.ax)
        self.mode.plot_root(self.ax)
        
        
        # connect the signals and slots (buttons with functions)
        QtCore.QObject.connect(self.recalculateRoot_pushButton, QtCore.
                               SIGNAL('clicked()'), self.click_find_root)
    
    def click_find_root(self):
        ''' when user clicks the find root button, recalculate the root, then
             redraw the graph '''
        self.mode.recalculate_root()
        
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