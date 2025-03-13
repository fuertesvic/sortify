from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton,QDialog, QApplication


class DialogWindow(QDialog):  
    def __init__(self, title, geometry, text):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(*geometry)
        self.label = QLabel(text, self)
        self.line_edit = QLineEdit(self)     
        self.line_edit.setPlaceholderText("Etiqueta")  
        self.button = QPushButton("Ok", self)
        self.button.setGeometry(10,40,100,40)
        self.button.clicked.connect(self.submit)
        

    def submit(self):
        self.user_input = self.line_edit.text()
        super().accept()
        
    def get_user_input(self):
        return self.user_input  # Return the stored user input

if __name__ == '__main__':
    app = QApplication([])
    mywindow = DialogWindow('Title',(200,200,200,200), "Hello")