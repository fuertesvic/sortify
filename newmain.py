import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel,
                            QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow): # Main window inherits from MainWindow from Qt
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SortiFy but using Qt!")
        self.setGeometry(0, 0, 800, 600)                   # First 2 are to set the window placing on screen
        self.setWindowIcon(QIcon("icon_for_window"))       # Set Window Icon
        label = QLabel(self, text="Benvingut/da a SortiFy!")
        label.setFont(QFont("Helvetica",25))
        label.setGeometry(0,0,800,100)
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

# Create app - Needed to set widgets on top
app = QApplication([])

# Set the window
window = MainWindow()
window.show()

# Start and handle the event loop
sys.exit(app.exec())




