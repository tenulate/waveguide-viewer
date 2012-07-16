''' A widget class to embed matplotlib graphs into Qt '''

from PyQt4 import QtGui
# The backend, Qt specific figure canvas from matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
# The abstract Figure class from matplotlib, can be used with all backends
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    ''' Class to define a Canvas which can be embedded into Qt '''
    
    def __init__(self):
        # create a new abstract figure
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        
        # set the parent of the abstract Figure to the present canvas
        FigureCanvas.__init__(self, self.fig)
        # set expanding size policies in horizontal and vertical direction
        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        # As size policies have changed, update them
        FigureCanvas.updateGeometry(self)
        
class MplWidget(QtGui.QWidget):
    ''' Class for a matplotlib widget to sit in Qt '''
    
    def __init__(self, parent = None):
        # Use setup of base class QWidget - parent tells us which window to put
        # things in
        QtGui.QWidget.__init__(self, parent)
        # Set up an mpl capable canvas
        self.canvas = MplCanvas()
        # Make a Qt vertical box to put the canvas in - so that the vertical box
        # can take care of the layout stuff in the window
        self.vbl = QtGui.QVBoxLayout()
        # put canvas in the vertical box
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)