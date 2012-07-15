from coaxial_modes import *

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class InputWindow(QDialog):
    
    def __init__(self, parent=None):
        super(InputWindow, self).__init__(parent)
        
        # list of coaxial modes
        self.modes = []
        
        # Make labels describing inputs
        cLabelInput = QLabel("c")
        mLabelInput = QLabel("m")
        nLabelInput = QLabel("n")
        modeLabelInput = QLabel("Mode")
        
        # labels describing Mode data
        cLabelOutput = QLabel('<b>c</b>')
        mLabelOutput = QLabel('<b>m</b>')
        nLabelOutput = QLabel('<b>n</b>')
        modeLabelOutput = QLabel('<b>Mode</b>')
        rootLabelOutput = QLabel("<b>Root</b>")
        chiMinusLabelOutput = QLabel("<b>(c-1) root</b>")
        chiPlusLabelOutput = QLabel("<b>(c+1) root</b>")
        
        # mode inputs
        # c input
        self.cDoubleSpinBox = QDoubleSpinBox()
        self.cDoubleSpinBox.setMinimum(1.10)
        self.cDoubleSpinBox.setMaximum(10.0)
        self.cDoubleSpinBox.setSingleStep(0.1)
        self.cDoubleSpinBox.setProperty('value', 2.5)
        # m input
        self.mSpinBox = QSpinBox()
        self.mSpinBox.setMinimum(0)
        self.mSpinBox.setMaximum(100)
        self.mSpinBox.setProperty('value', 0)
        # n input
        self.nSpinBox = QSpinBox()
        self.nSpinBox.setMinimum(1)
        self.nSpinBox.setMaximum(100)
        self.nSpinBox.setProperty('value', 1)
        # mode input
        self.modeComboBox = QComboBox()
        self.modeComboBox.addItems(['TE', 'TM', 'TEM'])
        # check box to increase m/n after clicking 'Add Mode'
        self.nCheckBox = QCheckBox('increment')
        self.mCheckBox = QCheckBox('increment')
             
        # Labels showing mode data
        self.modeLabel = QLabel('')
        self.mLabel = QLabel('')
        self.nLabel = QLabel('')
        self.cLabel = QLabel('')
        self.rootLabel = QLabel('')
        self.chiPlusLabel = QLabel('')
        self.chiMinusLabel = QLabel('')
        
        # Buttons
        addButton = QPushButton("Add Mode")
        addButtonLayout = QHBoxLayout()
        addButtonLayout.addStretch()
        addButtonLayout.addWidget(addButton)
        
        nextButton = QPushButton("Next")
        nextButtonLayout = QHBoxLayout()
        nextButtonLayout.addStretch()
        nextButtonLayout.addWidget(nextButton)
        
        # spacers
        fixed_spacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        spacer = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        stretch = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Maximum)
        
        # input layout
        inputLayout = QGridLayout()
        
        inputLayout.addWidget(cLabelInput, 0, 0)
        inputLayout.addWidget(self.cDoubleSpinBox, 0, 1)
        inputLayout.addItem(fixed_spacer, 0, 2)
        
        inputLayout.addWidget(mLabelInput, 0, 3)
        inputLayout.addWidget(self.mSpinBox, 0, 4)
        inputLayout.addItem(fixed_spacer, 0, 5)
        
        inputLayout.addWidget(nLabelInput, 0, 6)
        inputLayout.addWidget(self.nSpinBox, 0, 7)
        inputLayout.addItem(fixed_spacer, 0, 8)
        
        inputLayout.addWidget(modeLabelInput, 0, 9)
        inputLayout.addWidget(self.modeComboBox, 0, 10)
        inputLayout.addItem(spacer, 0, 11)
        inputLayout.addLayout(addButtonLayout, 0, 12)
        
        inputLayout.addWidget(self.mCheckBox, 1, 4)
        inputLayout.addWidget(self.nCheckBox, 1, 7)
        
        # output layout
        spacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        outputLayout = QGridLayout()
        outputLayout.addItem(spacer, 0, 0)
        outputLayout.addWidget(modeLabelOutput, 0, 1)
        outputLayout.addWidget(self.modeLabel, 1, 1)
        outputLayout.addWidget(cLabelOutput, 0, 2)
        outputLayout.addWidget(self.cLabel, 1, 2)
        outputLayout.addWidget(mLabelOutput, 0, 3)
        outputLayout.addWidget(self.mLabel, 1, 3)
        outputLayout.addWidget(nLabelOutput, 0, 4)
        outputLayout.addWidget(self.nLabel, 1, 4)
        outputLayout.addWidget(rootLabelOutput, 0, 5)
        outputLayout.addWidget(self.rootLabel, 1, 5)
        outputLayout.addWidget(chiPlusLabelOutput, 0, 6)
        outputLayout.addWidget(self.chiPlusLabel, 1, 6)
        outputLayout.addItem(spacer, 0, 7)
        outputLayout.addWidget(chiMinusLabelOutput, 0, 8)
        outputLayout.addWidget(self.chiMinusLabel, 1, 8)
        outputLayout.addItem(spacer, 0, 9)
        
        self.listWidget = QListView()
        outputLayout.addWidget(self.listWidget, 3, 1, 1, 8)
        
        displayLayout = QVBoxLayout()
        displayLayout.addLayout(inputLayout)
        displayLayout.addSpacing(10)
        displayLayout.addLayout(outputLayout)
        displayLayout.addStretch()
        
        self.setLayout(displayLayout)
        
        # connect
        self.connect(addButton, SIGNAL("clicked()"),
                     self.addMode)
        
        # make pretty 
        self.setWindowTitle("Coaxial Modes")
        self.setWindowIcon(QIcon('icon.png'))
        
    def addMode(self):
        # get current input values
        c = self.cDoubleSpinBox.value()
        m = self.mSpinBox.value()
        n = self.nSpinBox.value()
        mode_type = self.modeComboBox.currentText()
        
        # add this mode to the list
        if mode_type == 'TE':
            self.modes.append(TEmode(m,n,c))
        elif mode_type == 'TM':
            self.modes.append(TMmode(m,n,c))
        else:
            print "error"
        
        # update input mode values
        if self.nCheckBox.checkState():
            self.update_n()
        if self.mCheckBox.checkState():
            self.update_m()
            
        self.displayModes()
    
    def displayModes(self):
        # go through modes and display them (int text form)
        c_list = ''
        m_list = ''
        n_list = ''
        root_list = ''
        mode_type_list = ''
        chi_minus_list = ''
        chi_plus_list = ''
        
        for mode in self.modes:
            c = mode.c
            m = mode.m
            n = mode.n
            root = mode.root
            mode_type = mode.mode
            label, marcuvitz_root = mode.marcuvitz()
            
            if label == '(c+1)*chi':
                chi_plus_list = chi_plus_list + '%.3f' % marcuvitz_root + '\n'
                chi_minus_list = chi_minus_list + '-\n'
            elif label == '(c-1)*chi':
                chi_plus_list = chi_plus_list+'-\n'
                chi_minus_list = chi_minus_list + '%.3f' % marcuvitz_root + '\n'
            else:
                print 'error'
            
            c_list = c_list+str(c)+'\n'
            m_list = m_list+str(m)+'\n'
            n_list = n_list+str(n)+'\n'
            root_list = root_list+'%.3f' % root + '\n'
            mode_type_list = mode_type_list+str(mode_type)+'\n'
            
        self.cLabel.setText(c_list)
        self.mLabel.setText(m_list)
        self.nLabel.setText(n_list)
        self.rootLabel.setText(root_list)  
        self.modeLabel.setText(mode_type_list)
        self.chiPlusLabel.setText(chi_plus_list)
        self.chiMinusLabel.setText(chi_minus_list)
        
    def update_n(self):
        # makes it easy to keep clicking "Add mode" and have the n values increment
        n = self.nSpinBox.value()
        self.nSpinBox.setValue(n+1)
    
    def update_m(self):
        # makes it easy to keep clicking "Add mode" and have the m values increment
        m = self.mSpinBox.value()
        self.mSpinBox.setValue(m+1)
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = InputWindow()
    form.show()
    
    app.exec_()