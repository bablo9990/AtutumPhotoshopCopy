

from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.red_warning = "border-color: red; border-style: solid; border-width: 2px; font-weight: normal;"

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # Add toolbar and items
        self.toolbox = QToolBox()

        self.lineEdit_1 = QLineEdit()
        self.toolbox.addItem(self.lineEdit_1, "Вкладка 1")
        self.lineEdit_2 = QLineEdit()
        self.toolbox.addItem(self.lineEdit_2, "Вкладка 2")
        self.lineEdit_3 = QLineEdit()
        self.toolbox.addItem(self.lineEdit_3, "Вкладка 3")

        self.buttonAdd = QPushButton('Проверить')
        self.buttonAdd.clicked.connect(self.check)

        vbox = QGridLayout(self.centralWidget)
        vbox.addWidget(self.toolbox, 0, 0, 1, 2)
        vbox.addWidget(self.buttonAdd, 2, 1)

    def check(self):
        fields = [self.lineEdit_1, self.lineEdit_2, self.lineEdit_3]
        for field in fields:
            if field.text() != '' and field.text().isspace():
                field.setStyleSheet(self.red_warning)
            elif field.text() == '':
                field.setStyleSheet(self.red_warning)
            else:
                field.setStyleSheet('')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())