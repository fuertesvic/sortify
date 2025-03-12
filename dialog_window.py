from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton

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
