# This class is used to implement a Model/View Architecture
# It inherits from QAbstractItemModel, which ensures proper & efficient data handling, loading and visualization
# In other words, we keep a data structure holding the image: tags data, so we don't have to open every image every time.
from PyQt6.QtCore import QAbstractItemModel, QModelIndex, Qt

class ImageTreeModel(QAbstractItemModel):
    def __init__(self, data = None):
        super().__init__()
        self.images = data if data else []
        self.file_set = set()

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
        if image_name in self.file_set:
            return
        self.file_set.add(image_name)
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.images.append({"name":image_name, "tags": tags})
        self.endInsertRows()

    def add_tag_to_image(self, index, tag):
        
        tags = self.images[index]["tags"] 
        if tags:    
            self.images[index]["tags"] = ",".join([tags, tag])
        else:
            self.images[index]["tags"] = tag

    
    def remove_tags_from_image(self, index):
        self.images[index]["tags"] = ''

    def search_image_with_tag(self, tag):
        print("Search Image with tag called")
        print([tag in item['tags']for item in self.images]) 

    # Required method
    def index(self, row, column, parent=QModelIndex()):
        if self.hasIndex(row, column, parent):
            return self.createIndex(row, column)
        return QModelIndex()  # Return an invalid index if out of bounds

    # Required method
    def parent(self, index):
        return QModelIndex()  # Always return an invalid parent for a table
