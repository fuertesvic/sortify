import os
from PyQt6.QtWidgets import (QMainWindow, QLabel, 
                            QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                            QPushButton, QFileDialog, QLineEdit,QTableView)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt
from image_tree_model import ImageTreeModel
from dialog_window import DialogWindow

class MainWindow(QMainWindow): # Main window inherits from MainWindow from Qt
    def __init__(self):
        super().__init__()
        self.set_window_settings()
        self.init_UI() 
        self.image_tree = ImageTreeModel()
        self.new_window = None

    def set_window_settings(self):
        """Sets the main window geometry, title and icon"""
        self.setWindowTitle("SortiFy but using Qt!")
        self.setGeometry(0, 0, 800, 600)                  
        self.setWindowIcon(QIcon("assets/icon_for_window.jpg"))       
    
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

        button1.clicked.connect(self.load_folder_view)
        button2.clicked.connect(self.ask_tag_dialog)
        button3.clicked.connect(self.close)

    def load_folder_view(self):
        self.ask_folder_dialog()
        path = self.selected_folder

        if path:
            for file in os.listdir(path):
                self.image_tree.add_image_to_model(file)
        self.show_tree_view()

    def ask_folder_dialog(self):
        self.clear_widgets()
        self.selected_folder = str(QFileDialog.getExistingDirectory(self, "Seleccioni una carpeta"))
        self.init_UI()
    
    def ask_tag_dialog(self):
        if self.new_window is None:
            self.new_window  = DialogWindow(self,"Tag", (200,200,200,200), "Set a tag:")
    
    def clear_widgets(self):
        """Deletes all widgets from the window"""
        while self.vbox.count():
            widget = self.vbox.takeAt(0).widget()
            if widget is not None:
                widget.deleteLater()  # Ensures proper deletion
    
    def myfunc(self):
        print(self.selection.currentIndex().row())

    def show_tree_view(self):
       
        tree_view_widget = QWidget()
        tree_layout = QVBoxLayout(tree_view_widget)
        
        view = QTableView()
        view.setModel(self.image_tree)
        
        add_tag_btn = QPushButton("Afegir Etiqueta")
        add_tag_btn.clicked.connect(self.add_tag_to_selected)
        back_btn = QPushButton("Menu Principal")
        back_btn.clicked.connect(self.init_UI)

        self.selection = view.selectionModel()
        
        tree_layout.addWidget(view)
        tree_layout.addWidget(add_tag_btn)
        tree_layout.addWidget(back_btn)
        self.setCentralWidget(tree_view_widget)

    def add_tag_to_selected(self):
        tag = None
        index = self.selection.currentIndex().row()
        dialog = DialogWindow("Etiqueta", (200,200,400,400), "introdueixi l'etiqueta")
        result = dialog.exec()
        if result == 1: tag = dialog.get_user_input() 
        if tag: self.image_tree.add_tag_to_image(index, tag)
    

       