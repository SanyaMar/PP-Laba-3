import sys


import PyQt5
from PyQt5.QtWidgets import QApplication, QAction, QFileDialog, QHBoxLayout, QLabel, QWidget, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap

from num_1 import first_annotation
from num_2 import second_annotation, dataset_2
from num_3 import annotation_3, dataset_3
from num_5 import Iterator


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_window()
        self.create_iter()
        
        self.add_menu_bar()
    
       
       

    def main_window(self) ->None:
        self.setWindowTitle('Images Cats and Dogs')
        self.setWindowIcon(QIcon('icon/cat_dog.png'))
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.setStyleSheet("background-color: #FFEEDD;") 


        button_cat=QPushButton('< Next cat', self)
        button_cat.setFixedSize(100, 50)
        button_cat.setStyleSheet('QPushButton {background-color: #B8B8FF}')
        button_dog=QPushButton('Next dog >', self)
        button_dog.setFixedSize(100, 50)
        button_dog.setStyleSheet('QPushButton {background-color: #B8B8FF}')

        pixmap = QPixmap('icon/main_img.jpg')   
        self.lbl = QLabel(self)
        self.lbl.setPixmap(pixmap)
        self.lbl.setAlignment(Qt.AlignCenter)  

        box = QHBoxLayout()
        box.addSpacing(1)
        box.addWidget(button_cat)
        box.addWidget(self.lbl)
        box.addWidget(button_dog)   
        
        self.centralWidget.setLayout(box)

        button_cat.clicked.connect(self.next_cat)
        button_dog.clicked.connect(self.next_dog)
        
        self.folderpath = ' '
        
        self.showMaximized()

    def create_iter(self) -> None:   
        self.cat = Iterator('cat', 'dataset_1')
        self.dog = Iterator('dog', 'dataset_1')
   
    def next_cat(self) -> None:
        
        lbl_size = self.lbl.size()
        next_image = next(self.cat)
        if next_image != None:
            img = QPixmap(next_image).scaled(
                lbl_size, aspectRatioMode=Qt.KeepAspectRatio)
            self.lbl.setPixmap(img)
            self.lbl.setAlignment(Qt.AlignCenter)
        else:
            self.create_iter()
            self.next_cat()

    def next_dog(self) -> None:
        
        lbl_size = self.lbl.size()
        next_image = next(self.dog)
        if next_image != None:
            img = QPixmap(next_image).scaled(
                lbl_size, aspectRatioMode=Qt.KeepAspectRatio)
            self.lbl.setPixmap(img)
            self.lbl.setAlignment(Qt.AlignCenter)
        else:
            self.create_iter()
            self.next_dog()
   

    
    def add_menu_bar(self) -> None:
        menu_bar = self.menuBar()

        self.file_menu = menu_bar.addMenu('&File')
        self.change_action = QAction(QIcon('icon/blue-folder.png'), '&Change dataset')
        self.change_action.triggered.connect(self.changeDataset)
        self.file_menu.addAction(self.change_action)

        self.annotation_menu = menu_bar.addMenu('&Annotation')
        self.create_annot_action = QAction(
            QIcon('icon/csv.png'), '&Create annotation')
        self.create_annot_action.triggered.connect(self.create_annotation)
        self.annotation_menu.addAction(self.create_annot_action)

        self.datasets_menu = menu_bar.addMenu('&Datasets')
        self.create_database_2_action = QAction(
            QIcon('icon/blue-folders.png'), '&Create dataset2')
        self.create_database_2_action.triggered.connect(self.createDataset2)
        self.datasets_menu.addAction(self.create_database_2_action)


   


    
    def create_annotation(self) -> None:
        
        if 'dataset_2' in str(self.folderpath):
            second_annotation()
        elif 'dataset_3' in str(self.folderpath):
            annotation_3()
        elif 'dataset_1' in str(self.folderpath):
            first_annotation()

    def createDataset2(self) -> None:
        
        dataset_2()
        self.create_database_3_action = QAction(
            QIcon('icon/blue-folders-stack.png'), '&Create dataset3')
        self.create_database_3_action.triggered.connect(self.createDataset3)
        self.datasets_menu.addAction(self.create_database_3_action)
       

    def createDataset3(self) -> None:
        
        dataset_3()

    def changeDataset(self) -> None:
        self.folderpath = self.folderpath = QFileDialog.getExistingDirectory(
                self, 'Select Folder')
    

def main() -> None:

    app = QApplication(sys.argv)
    window = Window()
    
    sys.exit(app.exec_())
   


if __name__ == '__main__':
    main()



