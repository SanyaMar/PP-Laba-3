import sys


import PyQt5
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QMainWindow, QPushButton
from PyQt5.QtCore import Qt, QSize, QEvent
from PyQt5.QtGui import QIcon, QPixmap

import num_1
import num_2
import num_3
import num_4
import num_5


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_window()
        self.create_iter()
       

    def main_window(self) ->None:
        self.setWindowTitle('Images Cats and Dogs')
        self.setWindowIcon(QIcon('icon/cat_dog.png'))
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        menu_bar = self.menuBar()

        self.file_menu = menu_bar.addMenu('&Create annotation')
        self.edit_menu = menu_bar.addMenu('&Create dataset')
        self.help_menu = menu_bar.addMenu('&File')

        button_cat=QPushButton('< Next cat', self)
        button_cat.setFixedSize(100, 50)
        button_dog=QPushButton('Next dog >', self)
        button_dog.setFixedSize(100, 50)

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
        
        self.folderpath = ' '
        self.lbl = QLabel(self)
        self.showMaximized()

    def create_iter(self) -> None:   
        self.brownbears = num_5.iterator('cat', 'dataset_1')
        self.polarbears = num_5.iterator('dog', 'dataset_1')

def main() -> None:

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
   


if __name__ == '__main__':
    main()


