import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore    import *


class ExampleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Example Widget ScrollArea')
        self.initUi()

    def initUi(self):
        area = QScrollArea(self)
        area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QLabel(some_long_text, self) 

        area.setWidget(self.scrollAreaWidgetContents)
        button = QPushButton("Закрыть окно")
        button.clicked.connect(self.goMainWindow) 

        layoutV = QVBoxLayout() 
        layoutV.addWidget(area)
        layoutV.addWidget(button)
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.hide()

    def sizeHint(self):                                  
        return QSize(400, 200)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        start_main_button  = QPushButton('Start', self)
        start_main_button.move(40, 40)
        start_main_button.clicked.connect(self.start)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Test')

    def start(self):
        self.result_widget = ExampleWidget()
        self.result_widget.show() 


some_long_text = """
Есть всплывающее окно QWidget, вызываемое кнопкой Start на основном виджете. 
В него помещается текст, превышающий размер окна. 
Как я могу добавить в него вертикальную полосу прокрутки, чтобы видеть весь текст?
Есть всплывающее окно QWidget, вызываемое кнопкой Start на основном виджете. 
В него помещается текст, превышающий размер окна. 
Как я могу добавить в него вертикальную полосу прокрутки, чтобы видеть весь текст?
Есть всплывающее окно QWidget, вызываемое кнопкой Start на основном виджете. 
В него помещается текст, превышающий размер окна. 
Как я могу добавить в него вертикальную полосу прокрутки, чтобы видеть весь текст?
Есть всплывающее окно QWidget, вызываемое кнопкой Start на основном виджете. В него помещается текст, превышающий размер окна. 
Как я могу добавить в него вертикальную полосу прокрутки, чтобы видеть весь текст?
Есть всплывающее окно QWidget, вызываемое кнопкой Start на основном виджете. 
В него помещается текст, превышающий размер окна. 
Как я могу добавить в него вертикальную полосу прокрутки, чтобы видеть весь текст?
"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())