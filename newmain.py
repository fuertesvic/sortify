import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel,
                            QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow): # Main window inherits from MainWindow from Qt
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SortiFy but using Qt!")
        self.setGeometry(0, 0, 800, 600)                  
        self.setWindowIcon(QIcon("icon_for_window.jpg"))       # Set Window Icon
        self.initUI() 
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label = QLabel(self, text="Benvingut/da a SortiFy!")
        label.setFont(QFont("Helvetica",25))
        label.setGeometry(0,0,800,100)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        label1 = QLabel("First Label",self)
        label2 = QLabel("Second Label",self)
        label3 = QLabel("Third Label",self)
        label4 = QLabel("Fourth Label",self)
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        central_widget.setLayout(vbox)




# Create app - Needed to set widgets on top
app = QApplication([])

# Set the window
window = MainWindow()
window.show()

# Start and handle the event loop
sys.exit(app.exec())




