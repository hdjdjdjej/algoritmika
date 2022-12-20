from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout

app = QApplication([])
hello_world = QWidget()
hello_world.setWindowTitle('Приложение >_<')
hello_world.resize(450, 250)
text = QLabel('Hallo, World!')
v_line = QVBoxLayout()
v_line.addWidget(text, alignment=Qt.AlignCenter)
hello_world.setLayout(v_line)
hello_world.show()
app.exec_()