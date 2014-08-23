''' combines qt designer generated class files and program logic class files
    to produce single mode wave guide viewer '''

# import the main window from the pyuic4 converted .ui file    
from qtdesigner import Ui_WaveguideViewer_MainWindow

# for coaxial modes logic
from coaxial_modes import TMmode, TEmode, TEMmode

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
        self.root_canvas = self.mpl_rootFinder.canvas
        self.root_fig = self.root_canvas.fig
        self.root_ax = self.root_canvas.ax
        self.field_canvas = self.mpl_fieldplot.canvas
        self.field_fig = self.field_canvas.fig
        self.field_ax = self.field_canvas.ax
        
        # set up the initial wave guide mode
        self.set_waveguide_mode()
        self.plot_root()
        
        # connect the signals and slots (buttons with functions)
        
        # Mode selector window
        # When pressing "OK" and "Cancel" 
        QtCore.QObject.connect(self.mode_OKButton, QtCore.
                               SIGNAL('clicked()'), self.click_mode_ok)
        QtCore.QObject.connect(self.mode_CancelButton, QtCore.
                               SIGNAL('clicked()'), self.click_mode_cancel)
        
        QtCore.QObject.connect(self.mode_comboBox, QtCore.
                               SIGNAL('currentIndexChanged(int)'), self.changing_mode_combobox)
                
        # Root Calculator window
        # when pressing "recalculate root" 
        QtCore.QObject.connect(self.recalculateRoot_pushButton, QtCore.
                               SIGNAL('clicked()'), self.click_recalculate_root)
        QtCore.QObject.connect(self.recalculateRoot_pushButton, QtCore.
                               SIGNAL('clicked()'), self.plot_field)
        # when pressing "enter" after editing the x range values 
        QtCore.QObject.connect(self.rootMinX_lineEdit, QtCore.
                               SIGNAL('returnPressed()'), self.set_new_x_range)
        QtCore.QObject.connect(self.rootMaxX_lineEdit, QtCore.
                               SIGNAL('returnPressed()'), self.set_new_x_range)
        # When sliding the Y value bar 
        QtCore.QObject.connect(self.rootYRange_verticalSlider, QtCore.
                               SIGNAL('valueChanged(int)'), self.slide_yvalue_root)
        # "Less / More X axis points" button
        QtCore.QObject.connect(self.lessXPoints_pushButton, QtCore.
                               SIGNAL('clicked()'), self.click_less_x_points)
        QtCore.QObject.connect(self.moreXPoints_pushButton, QtCore.
                               SIGNAL('clicked()'), self.click_more_x_points)
        
        
        # Field plotting window
    
        QtCore.QObject.connect(self.E_field_checkBox, QtCore.
                               SIGNAL('stateChanged(int)'), self.click_field_checkbox)
        QtCore.QObject.connect(self.H_field_checkBox, QtCore.
                               SIGNAL('stateChanged(int)'), self.click_field_checkbox)
        QtCore.QObject.connect(self.n_phi_spinBox, QtCore.
                               SIGNAL('valueChanged(int)'), self.plot_field)
        QtCore.QObject.connect(self.n_rho_spinBox, QtCore.
                               SIGNAL('valueChanged(int)'), self.plot_field)
                
        # change the open tabbed window
        self.tabWidget.setCurrentIndex(0)
        
    def set_waveguide_mode(self):
        ''' using the m, n and c values the user has selected from the spin boxes,
            saves the waveguide mode '''
        
        m = self.m_spinBox.value()
        n = self.n_spinBox.value()
        c = self.c_doubleSpinBox.value()
        index = self.mode_comboBox.currentIndex()
        
        if index == 0:
            self.mode = TEmode(m,n,c)
        elif index == 1:
            self.mode = TMmode(m,n,c)
        elif index == 2:
            self.mode = TEMmode(c)
    
    def plot_root(self):
        ''' plots the radial root equation in the root equation axis '''
        self.root_ax.clear()
        self.mode.plot_root(self.root_ax)
        self.mode.plot_root_equation(self.root_ax)
        # save the axis y range
        self.root_ymin, self.root_ymax = self.root_ax.get_ylim()
        self.root_xmin, self.root_xmax = self.root_ax.get_xlim()
        
        # update the minimum / maximum x text
        self.rootMinX_lineEdit.setText(str(self.root_xmin))
        self.rootMaxX_lineEdit.setText(str(self.root_xmax))
    
    def slide_yvalue_root(self):
        ''' when vertical slide bar is moved, update the y-range 
            want the y range to change exponentially so that we can easily range
            from say 10^(-5) to 10^(2) easily'''
        
        # we want to map the slider values (s) to 10^(y) values 
        # in a way so that smin -> 10^(ymin), smax -> 10^(ymax)
        min_s = float(self.rootYRange_verticalSlider.minimum())
        max_s = float(self.rootYRange_verticalSlider.maximum())
        ds = max_s-min_s
        # work in log scale
        log_max_y = 3
        log_min_y = -7
        d_log_y = log_max_y-log_min_y
        
        # slider value (s)
        s = self.rootYRange_verticalSlider.value()
        log_range_factor = d_log_y * (s-min_s) / ds + log_min_y
        ymin, ymax = 10**(log_range_factor) * np.array([self.root_ymin, 
                                                     self.root_ymax])
        self.root_ax.set_ylim(ymin, ymax)
        self.root_canvas.draw()
        
    def set_new_x_range(self):
        ''' set a new x range in the root plot '''
        
        # convert the line edit text to a float and set new range
        try:
            x_min = float(self.rootMinX_lineEdit.text())
            x_max = float(self.rootMaxX_lineEdit.text())
            self.mode.rootplot.set_xlim(x_min, x_max)
        # if can't convert text to float, return line edit to previous value
        except ValueError:
            x_min, x_max = self.root_ax.get_xlim()
            self.rootMinX_lineEdit.setText(str(x_min))
            self.rootMaxX_lineEdit.setText(str(x_max))
            
    def plot_field(self):
        ''' plot the field in the matplotlib axis '''
        self.field_ax.clear()
        # how many points to plot
        n_phi = self.n_phi_spinBox.value()
        n_rho = self.n_rho_spinBox.value()
        # plot the field
        self.mode.plot_field(self.field_ax, n_rho=n_rho, n_phi=n_phi)
        # make we're only showing the desired fields
        # click_field_checkbox replots the H and E fields, but only plots those 
        # that have been checked off
        self.click_field_checkbox()
        
        # Note a self.field_canvas.draw() is not necessary b/c click_field_checkbox
        # already performs that action
         
    def click_recalculate_root(self):
        ''' what to do when recalculate root is clicked '''
        
        # calculate the new root from the graph
        self.mode.recalculate_root()
        
        # if this root is out of range of the x axis, update the x axis
        root = self.mode.root
        xmin, xmax = self.root_ax.get_xlim()
        if root > xmax:
            new_xmax = 1.1*root
            self.mode.rootplot.set_xlim(xmin, new_xmax)
            self.rootMaxX_lineEdit.setText(str(new_xmax).strip('[]'))
            
        self.mode.drag.draw()
        
    def click_more_x_points(self):
        ''' what to do when "more x points" button is clicked in root calculator '''
        
        n = self.mode.rootplot.Npoints
        upper_limit = 2**12
        # if "less" button is not enabled, enable it
        if not self.lessXPoints_pushButton.isEnabled():
            self.lessXPoints_pushButton.setEnabled(True)
        # if n is too high set upper bound
        if n >= upper_limit:
            self.mode.rootplot.set_Npoints(upper_limit)
            # don't allow more button presses
            self.moreXPoints_pushButton.setEnabled(False)
        else:
            self.mode.rootplot.set_Npoints(2*n)
        
        self.mode.rootplot.plot()
        
    def click_less_x_points(self):
        ''' what to do when "less x points" button is clicked in root calculator '''
        
        n = self.mode.rootplot.Npoints
        lower_limit = 4
        
        # if "more" button is not enabled, enable it
        if not self.moreXPoints_pushButton.isEnabled():
            self.moreXPoints_pushButton.setEnabled(True)
        # if n is too low set lower bound
        if n <= lower_limit:
            self.mode.rootplot.set_Npoints(lower_limit)
            # don't allow more button presses
            self.lessXPoints_pushButton.setEnabled(False)
        else:
            self.mode.rootplot.set_Npoints(int(n/2))
        
        self.mode.rootplot.plot()
                
    def click_mode_ok(self):
        ''' what to do when clicking "OK" for the mode selection screen 
            - change current mode information, goto plot to find root'''
        
        # if the previous mode was TE or TM then we need to disconnect all 
        # the events associated with finding the roots of their equations
        if self.mode.mode is not 'TEM':
            # disconnect the previous signal / slot for the old mode
            QtCore.QObject.disconnect(self.recalculateRoot_pushButton, 
                                      QtCore.SIGNAL('clicked()'), 
                                      self.mode.recalculate_root)
            # need to disconnect the matplotlib calls for mode
            self.mode.drag.disconnect()
        
        # update the mode info
        self.set_waveguide_mode()
        
        # if it's a TEM mode selected then no need to plot a radial equation
        # just plot the E and H fields. 
        if self.mode.mode is 'TEM':
            self.plot_field()
            self.tabWidget.setCurrentIndex(2)
            return
        
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
        elif mode_type == 'TEM':
            self.mode_comboBox.setCurrentIndex(2)
        else:
            self.mode_comboBox.setCurrentIndex(0)
            
    def changing_mode_combobox(self):
        ''' what to do when changing the mode combo box
            if a TE or TM mode is selected, then the m and n spin boxes should be
            enabled.
            If a TEM mode is selected, they should be disabled as TEM mode doesn't have
            any m,n values associated with it '''
        index = self.mode_comboBox.currentIndex()
        
        if index == 2:
            ''' TEM mode is chosen, make m,n disabled '''
            self.m_spinBox.setEnabled(False)
            self.n_spinBox.setEnabled(False)
            
        else:
            self.m_spinBox.setEnabled(True)
            self.n_spinBox.setEnabled(True)
        
    def click_field_checkbox(self):
        ''' what to do when clicking on the E_field and H_field check boxes in the
            field plot window. 
        '''
        # If E field is checked then the Electric field should be displayed 
        # (set its quiver to visible)
        if self.E_field_checkBox.isChecked():
            self.mode.E_field.set_visible(True)
        else:
            self.mode.E_field.set_visible(False)
        # Likewise with H_field
        if self.H_field_checkBox.isChecked():
            self.mode.H_field.set_visible(True)
        else:
            self.mode.H_field.set_visible(False)
        
        self.field_canvas.draw()
          
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