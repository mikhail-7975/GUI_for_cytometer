import sys

import serial

from PyQt5.QtWidgets import * #QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QDialog):
    sendDataString = ""
    speeds = ['115200', '57600', '38400', '19200', '9600', '4800', '2400', '1200']
    currentConnectionSpeed = 0#int(speeds[0])
    connectionStatmentString = "disconnected"

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 layout - pythonspot.com'
        self.left = 50
        self.top = 50
        self.width = 320
        self.height = 100


        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
        self.journalGroupBox = QGroupBox("Journal")
        journalLayout = self.initJournalGroupbox()#QGridLayout()
        self.journalGroupBox.setLayout(journalLayout)
     
        self.SettingsGroupBox = QGroupBox("Settings")
        settingsLayout = self.initSettingsGroupbox()
        self.SettingsGroupBox.setLayout(settingsLayout)


        self.StatmentGroupBox = QGroupBox("Statment")
        statmentLayout = self.initStatmentGroupbox()
        self.StatmentGroupBox.setLayout(statmentLayout)
        
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        windowLayout = QGridLayout()
        windowLayout.addWidget(self.journalGroupBox, 0, 0)
        windowLayout.addWidget(self.SettingsGroupBox, 0, 1)
        windowLayout.addWidget(self.StatmentGroupBox, 1, 0, 1, 2)
        self.setLayout(windowLayout)
        
        self.show()

    def initJournalGroupbox(self):    
        area = QScrollArea(self)
        area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QLabel("... text ..." * 10, self) 

        area.setWidget(self.scrollAreaWidgetContents)
        
        layoutV = QGridLayout() 
        layoutV.addWidget(area, 0, 0)

        return layoutV

    def initSettingsGroupbox(self):
        layout2 = QGridLayout()
        layout2.setColumnStretch(1, 4)
        layout2.setColumnStretch(2, 4)


        sendWidgetLine = 0
        layout2.addWidget(QLabel("Send data to port:"), sendWidgetLine, 0)

        self.inpLine = QLineEdit("")
        layout2.addWidget(self.inpLine, sendWidgetLine, 1)

        sendButton = QPushButton("Send")
        sendButton.clicked.connect(self.on_click)
        layout2.addWidget(sendButton, sendWidgetLine, 2)

        speedWidgetLine = 1
        layout2.addWidget(QLabel("Connection speed:"), speedWidgetLine, 0)
        self.connectionSpeed = QComboBox(self)
        self.connectionSpeed.addItems(self.speeds)
        layout2.addWidget(self.connectionSpeed, speedWidgetLine, 1)

        self.connectButton = QPushButton("Connect")
        self.connectButton.clicked.connect(self.on_click_connectButton)
        layout2.addWidget(self.connectButton, 2, 3)

        return layout2

    def initStatmentGroupbox(self):

        layout2 = QGridLayout()
        layout2.setColumnStretch(1, 4)
        layout2.setColumnStretch(2, 4)


        statmentWidgetLine = 0
        layout2.addWidget(QLabel("Connection:"), statmentWidgetLine, 0)

        self.statmentLine = QLabel(self.connectionStatmentString)
        layout2.addWidget(self.statmentLine, statmentWidgetLine, 1)

        speedWidgetLine = 1
        layout2.addWidget(QLabel("Speed:"), speedWidgetLine, 0)

        self.connectionSprrdLine = QLabel(str(self.currentConnectionSpeed))
        layout2.addWidget(self.connectionSprrdLine, speedWidgetLine, 1)
       
        return layout2

    def on_click(self):
        if (self.connectionStatmentString == "connected"):
            self.sendDataString = self.inpLine.text()
            print(self.sendDataString)

    def on_click_connectButton(self):
        print("try connect")
        

        if (self.connectionStatmentString == "disconnected"):
            self.connectionStatmentString = "connected"
            self.connectButton.setText("disconnect")
            self.currentConnectionSpeed = int(self.connectionSpeed.currentText())
        else:
            self.connectionStatmentString = "disconnected"
            self.connectButton.setText("connect")
            self.currentConnectionSpeed = 0

        self.connectionSprrdLine.setText(str(self.currentConnectionSpeed))
        self.statmentLine.setText(self.connectionStatmentString)
        self.show()
#        self.StatmentGroupBox.update() 
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())