from PyQt6.QtCore import QAbstractItemModel, QModelIndex, Qt

class ImageTreeModel(QAbstractItemModel):
    def __init__(self, data = None):
        super().__init__()
        self.images = data if data else []

    def rowCount(self, parent=None):
        return len(self.images) if self.images else 0

    def columnCount(self, parent=None):
        return len(self.images[0]) if self.images else 0  

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or role != Qt.ItemDataRole.DisplayRole:
            return None
        item = self.images[index.row()]
        if index.column() == 0:
            return item["name"]
        elif index.column() == 1:
            return item["tags"] 
        return None
    
    def add_image_to_model(self, image_name, tags=None):
        if tags is None:
            tags = []
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.images.append({"name":image_name, "tags": tags})
        self.endInsertRows()

    def add_tag_to_image(self, index, tags):
        self.images[index]["tags"] = tags
    
    # Required method
    def index(self, row, column, parent=QModelIndex()):
        if self.hasIndex(row, column, parent):
            return self.createIndex(row, column)
        return QModelIndex()  # Return an invalid index if out of bounds

    # Required method
    def parent(self, index):
        return QModelIndex()  # Always return an invalid parent for a table

# app = QApplication([])

# data = [{"name":"Image1", "tags": "ocean"},    
#         {"name":"Image 2","tags": "mountain"}]

# model = ImageTreeModel(data)
# model.add_image_to_model("Image 3","sunset")
# model.add_image_to_model("Image 4")
# model.add_tag_to_image(2,"MyTag")

# view = QTableView()

# view.setModel(model)
# view.show()

# app.exec()