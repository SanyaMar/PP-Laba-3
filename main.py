import sys


import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QIcon, QPixmap

import num_1
import num_2
import num_3
import num_4
import num_5


class MainWindow():
    def __init__(self)-> None:
        super().__init__()
        
       

def main() -> None:

    app = QApplication(sys.argv)
    window = QWidget()
    window.show()
    sys.exit(app.exec_())
   


if __name__ == '__main__':
    main()