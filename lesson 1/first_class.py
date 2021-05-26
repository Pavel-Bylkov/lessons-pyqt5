from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel,
                             QHBoxLayout, QPushButton, QVBoxLayout, QLCDNumber)
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.config()
        self.setupUi()
        self.count = 0
        self.connects()

    def config(self):
        self.setWindowTitle("Первое приложение")
        self.resize(700, 500)

    def setupUi(self):
        self.text = QLabel("Hello world")
        self.btn = QPushButton("Button")
        self.display = QLCDNumber()

        v_line = QVBoxLayout()
        v_line.addWidget(self.display)
        h_line1 = QHBoxLayout()
        h_line1.addWidget(self.text, alignment=Qt.AlignCenter)
        v_line.addLayout(h_line1)
        h_line2 = QHBoxLayout()
        h_line2.addWidget(self.btn, alignment=Qt.AlignCenter)
        v_line.addLayout(h_line2)
        self.setLayout(v_line)

    def connects(self):
        self.btn.clicked.connect(self.hello)

    def hello(self):
        if self.text.text() == "Hello world":
            self.text.setText("Click!")
            self.display.display("click")
            self.count += 1
        else:
            self.text.setText("Hello world")


def main():
    app = QApplication([])
    win = Window()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()