import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel,
                            QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                            QPushButton, QFileDialog, QLineEdit)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow): # Main window inherits from MainWindow from Qt
    def __init__(self):
        super().__init__()
        self.set_window_settings()
        self.init_UI() 
        self.new_window = None

    def set_window_settings(self):
        """Sets the main window geometry, title and icon"""
        self.setWindowTitle("SortiFy but using Qt!")
        self.setGeometry(0, 0, 800, 600)                  
        self.setWindowIcon(QIcon("icon_for_window.jpg"))       
    
    def init_UI(self):
        """Prints the main menu screen with user options as buttons in a vertical layout (vbox)"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Title label
        title_label = QLabel("Benvingut/da a SortiFy!\nQuina acció vol realitzar?", central_widget)
        title_label.setFont(QFont("Verdana",15))
    
        # Option labels
        button1 = QPushButton("Navegar una carpeta: consultar / afegir / eliminar etiquetes",central_widget)
        button2 = QPushButton("Fer una cerca d'imatges que continguin una etiqueta concreta",central_widget)
        button3 = QPushButton("Surt del programa",central_widget)

        # Layout -- Method of organizing widgets
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(title_label, alignment = Qt.AlignmentFlag.AlignHCenter)
        self.vbox.addStretch()
        self.vbox.addWidget(button1, alignment = Qt.AlignmentFlag.AlignHCenter )
        self.vbox.addStretch()
        self.vbox.addWidget(button2, alignment = Qt.AlignmentFlag.AlignHCenter )
        self.vbox.addStretch()
        self.vbox.addWidget(button3, alignment = Qt.AlignmentFlag.AlignRight)

        central_widget.setLayout(self.vbox)

        button1.clicked.connect(self.ask_folder_dialog)
        button2.clicked.connect(self.ask_tag_dialog)
        button3.clicked.connect(self.close)

    def ask_folder_dialog(self):
        self.clear_widgets()
        self.selected_folder = str(QFileDialog.getExistingDirectory(self, "Seleccioni una carpeta"))
        print(f"Selected folder is {self.selected_folder} !")
        self.init_UI()
    
    def ask_tag_dialog(self):
        if self.new_window is None:
            self.new_window  = DialogWindow(self,"Tag", (200,200,200,200), "Set a tag:")

    def file_list_view(self):
        pass
    
    def clear_widgets(self):
        """Deletes all widgets from the window"""
        while self.vbox.count():
            widget = self.vbox.takeAt(0).widget()
            if widget is not None:
                widget.deleteLater()  # Ensures proper deletion
    
class DialogWindow(QWidget):  
    def __init__(self, parent_window, title, geometry, text):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(*geometry)
        self.label = QLabel(text, self)
        self.line_edit = QLineEdit(self)     
        self.line_edit.setPlaceholderText("Etiqueta")  
        self.button = QPushButton("Ok", self)
        self.button.setGeometry(10,40,100,40)
        self.button.clicked.connect(self.submit)
        self.show()

    def submit(self):
        text = self.line_edit.text()
        print(f"Hello {text}")

class Image():
    def __init__(self, name, format, size, mod_date):
        self.name = name
        self.format = format
        self.size = size
        self.mod_date = mod_date
    
    def read_metadata(self):
        pass

    def add_metadata(self):
        pass

def main():

# Create app - Needed to set widgets on top
    app = QApplication([])

    # Set the window
    window = MainWindow()
    window.show()

    # Start and handle the event loop
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

