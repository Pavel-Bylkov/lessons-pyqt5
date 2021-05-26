from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel,
                             QHBoxLayout, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

app = QApplication([])
win = QWidget()
#win.statusBar().showMessage('Ready')
win.setWindowTitle("Первое приложение")
win.resize(700, 500)

text = QLabel("Hello world")
btn = QPushButton("Button")

v_line = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line1.addWidget(text, alignment=Qt.AlignCenter)
v_line.addLayout(h_line1)
h_line2 = QHBoxLayout()
h_line2.addWidget(btn, alignment=Qt.AlignCenter)
v_line.addLayout(h_line2)
win.setLayout(v_line)

def hello():
    if text.text() == "Hello world":
        text.setText("Bye")
    else:
        text.setText("Hello world")


btn.clicked.connect(hello)

win.show()
app.exec()