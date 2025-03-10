import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel,
                            QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                            QPushButton)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow): # Main window inherits from MainWindow from Qt
    def __init__(self):
        super().__init__()
        self.set_window_settings()
        self.init_UI() 

    def set_window_settings(self):
        self.setWindowTitle("SortiFy but using Qt!")
        self.setGeometry(0, 0, 800, 600)                  
        self.setWindowIcon(QIcon("icon_for_window.jpg"))       
    
    def init_UI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Title label
        title_label = QLabel("Benvingut/da a SortiFy!\nQuina acció vol realitzar?", central_widget)
        title_label.setFont(QFont("Verdana",15))
    
        # Option labels
        button1 = QPushButton("Opció 1Opció 1Opció 1Opció 1",central_widget)
        button2 = QPushButton("Opció 2Opció 1Opció 1Opció 1",central_widget)
        button3 = QPushButton("Opció 3Opció 1",central_widget)

        # Layout -- Method of organizing widgets
        vbox = QVBoxLayout()
        vbox.addWidget(title_label, alignment = Qt.AlignmentFlag.AlignHCenter)
        vbox.addStretch()
        vbox.addWidget(button1, alignment = Qt.AlignmentFlag.AlignHCenter )
        vbox.addStretch()
        vbox.addWidget(button2, alignment = Qt.AlignmentFlag.AlignHCenter )
        vbox.addStretch()
        vbox.addWidget(button3, alignment = Qt.AlignmentFlag.AlignRight)

        
        central_widget.setLayout(vbox)

   

# Create app - Needed to set widgets on top
app = QApplication([])

# Set the window
window = MainWindow()
window.show()

# Start and handle the event loop
sys.exit(app.exec())




