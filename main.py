import sys
import os
from PyQt6.QtWidgets import QApplication
from ui_main import MainWindow
from image_tree_model import ImageTreeModel

if __name__ == '__main__':
    # # Create app - Needed to set widgets on top
    # app = QApplication([])

    # # Set the window
    # window = MainWindow()
    # window.show()

    # # Start and handle the event loop
    # sys.exit(app.exec())

    mytree = ImageTreeModel()

    path = "assets/pokemon"
    for file in os.listdir(path):
        mytree.add_image_to_model(file)
    print(mytree.images)
    


