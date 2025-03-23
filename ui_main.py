# Logic regarding the GUI and user interactions
import os
from PyQt6.QtWidgets import (QMainWindow, QLabel,QTreeView,
                            QWidget, QVBoxLayout, QAbstractItemView,
                            QPushButton, QFileDialog,QTableView)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt
from image_tree_model import ImageTreeModel
from dialog_window import DialogWindow
from metadata_manager import write_tag_in_metadata, read_tag_in_metadata, remove_tags_from_image

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
        button2.clicked.connect(self.load_folder_view)
        button3.clicked.connect(self.close)

    def load_folder_view(self):
        """Asks the user to select a directory, then sets the file data into the image_tree, and then calls for the view"""
        self.ask_folder_dialog()
        path = self.selected_folder
        if path:
            for file in os.listdir(path):
                tag = read_tag_in_metadata(path +'/' +file)
                self.image_tree.add_image_to_model(file, tag)
        self.show_tree_view()

    def ask_folder_dialog(self):
        """Clears the screen and opens a directory dialog"""
        self.clear_widgets()
        self.selected_folder = str(QFileDialog.getExistingDirectory(self, "Seleccioni una carpeta"))
    
    def clear_widgets(self):
        """Deletes all widgets from the window"""
        while self.vbox.count():
            widget = self.vbox.takeAt(0).widget()
            if widget is not None:
                widget.deleteLater()  # Ensures proper deletion
    
    def show_tree_view(self):
        
        # TreeView Setup - parent widget
        tree_view_widget = QWidget()

        # Layout for multiple items -> tree view + buttons, child of tree_view_widget
        tree_layout = QVBoxLayout(tree_view_widget)
        
        # Table
        view = QTableView()
        view.setModel(self.image_tree)
        
        add_tag_btn = QPushButton("Afegir Etiqueta")
        add_tag_btn.clicked.connect(self.add_tag_to_selected)
        # select_all_btn = QPushButton("Selecciona tots")
        # select_all_btn.clicked.connect(self.select_all_items)
        remove_tag_btn = QPushButton("Esborrar Etiquetes")
        remove_tag_btn.clicked.connect(self.remove_tags_of_selected)
        back_btn = QPushButton("Menu Principal")
        back_btn.clicked.connect(self.init_UI)
        
        # Allow to select multiple items
        view.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)

        # When one cell is selected, select all row
        view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        # Allow selection and store it in self.selection
        self.selection = view.selectionModel()
        
        # Add UI elements to layout
        tree_layout.addWidget(view)
        tree_layout.addWidget(add_tag_btn)
        # tree_layout.addWidget(select_all_btn)
        tree_layout.addWidget(remove_tag_btn)
        tree_layout.addWidget(back_btn)
        self.setCentralWidget(tree_view_widget)
        self.image_tree.search_image_with_tag("a")

    def add_tag_to_selected(self):
        """Asks the user to input a tag and adds it to the currently selected images"""
        tag = None
        dialog = DialogWindow("Etiqueta", (200,200,175,100), "introdueixi l'etiqueta")  # Ask for tag
        result = dialog.exec()
        if result == 1: tag = dialog.get_user_input()   # Ensure the dialog was accepted
        selected_rows =  {index.row() for index in self.selection.selectedIndexes()}
        if tag:             # Ensure there is a tag introduced
            for row_index in selected_rows:
                self.image_tree.add_tag_to_image(row_index,tag)
                path = f"{self.selected_folder}/{self.image_tree.images[row_index]['name']}"
                write_tag_in_metadata(path, tag)
                
    def remove_tags_of_selected(self):
        selected_rows =  {index.row() for index in self.selection.selectedIndexes()}

        for row_index in selected_rows:
            self.image_tree.remove_tags_from_image(row_index)
            path = f"{self.selected_folder}/{self.image_tree.images[row_index]['name']}"
            remove_tags_from_image(path)
    
    def search_images_with_tag(self):
        dialog = DialogWindow("Etiqueta", (200,200,175,100), "introdueixi l'etiqueta")  # Ask for tag
        tag = dialog.exec()
        self.show_tree_view(tag)