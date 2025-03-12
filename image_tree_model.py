from PyQt6.QtCore import QAbstractItemModel, QModelIndex, Qt
from PyQt6.QtWidgets import QApplication, QTableView

class ImageTreeModel(QAbstractItemModel):
    def __init__(self, data = None):
        super().__init__()
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data[0]) if self._data else 0  # Ensure this method exists
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]
        return None
    
    # Implement the required `index()` method
    def index(self, row, column, parent=QModelIndex()):
        if self.hasIndex(row, column, parent):
            return self.createIndex(row, column)
        return QModelIndex()  # Return an invalid index if out of bounds

    # Implement the required `parent()` method (not needed for flat tables)
    def parent(self, index):
        return QModelIndex()  # Always return an invalid parent for a table

app = QApplication([])

data = [["Victor","Fuertes"], ["Clara","Cardoner"],["Helena","Centeno"]]
print(data)
model = ImageTreeModel(data)
print("Done")
view = QTableView()

view.setModel(model)
print("Even here")
view.show()

app.exec()