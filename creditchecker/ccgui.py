#!/usr/bin/env python

# :copyright:	2009-2010 Andrea Grandi
# :author: 	Andrea Grandi
# :contact: 	a.grandi@gmail.com
# :license: 	LGPL
# :version:	0.1

from PySide.QtCore import *
from PySide.QtGui import *
import sys

class CreditCheckerGUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.setWindowTitle("Credit Checker")
        
        # Create menu items
        self.create_menu()
        
        # Design main widget layout
        self.create_main_widget()
        
    def create_menu(self):
        self.menuBar().addAction("Configuration")
        self.menuBar().addAction("About")
        
    def create_main_widget(self):
        self.main_widget = QWidget()
        
        self.mainlayout = QVBoxLayout()
        self.headerlayout = QHBoxLayout()
        
        self.carrier_name = QLabel()
        
        self.carrier_logo = QLabel()
        self.carrier_logo.setMaximumWidth(100)
        
        self.dataw = QTableWidget(0, 3, self)
        self.dataw.verticalHeader().hide()
        self.dataw.horizontalHeader().hide()
        self.dataw.horizontalHeader().setStretchLastSection(True)
        self.dataw.setColumnWidth(0, 50)
        self.dataw.setColumnWidth(1, 450)
        
        self.headerlayout.addWidget(self.carrier_logo)
        self.headerlayout.addWidget(self.carrier_name)
        
        self.mainlayout.addLayout(self.headerlayout)
        self.mainlayout.addWidget(self.dataw)
        
        self.main_widget.setLayout(self.mainlayout)
        self.setCentralWidget(self.main_widget)
        
    def set_status(self, status):
        self.statusBar().showMessage(status)
        
    def clear_status(self):
        self.statusBar().clearMessage()
        
    def set_carrier_name(self, name):
        self.carrier_name.setText(name)
        
    def set_carrier_logo(self, logo):
        logo = QPixmap(logo)
        self.carrier_logo.setPixmap(logo)
        
    def add_line_info(self, info_name, info_data):
        self.dataw.insertRow(self.dataw.rowCount())
        
        name = QTableWidgetItem(info_name)
        data = QTableWidgetItem(info_data)
        
        self.dataw.setItem(self.dataw.rowCount() - 1, 1, name)
        self.dataw.setItem(self.dataw.rowCount() - 1, 2, data)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CreditCheckerGUI()
    
    w.set_carrier_name("<h2><b>Tre Italia</b></h2>")
    w.set_carrier_logo("images/tre_it.jpg")
    
    w.add_line_info("Available credit: ", "10,23")
    w.add_line_info("Naviga 3: ", "22,00 Mb / 100,00 Mb")
    w.add_line_info("Free SMS: ", "14 / 100")
    
    w.set_status("Info updated 14:29 - 28/02/2010")
    
    w.show()
    app.exec_()
    sys.exit()
