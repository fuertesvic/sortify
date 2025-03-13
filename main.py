import sys
from PyQt6.QtWidgets import QApplication
from ui_main import MainWindow


if __name__ == '__main__':

    # Create app - Needed to set widgets on top
    app = QApplication([])

    # Main Window
    window = MainWindow()
    window.show() 
    
    # Start and handle the event loop
    sys.exit(app.exec())

   
    


