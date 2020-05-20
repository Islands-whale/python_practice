import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QInputDialog, QMessageBox, QTextBrowser)
from src.josephus.josephus import RingSort
from src.file_reader.file_reader import TxtReader, CsvReader, ZipReader


class RingGraphicInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.start = 1
        self.step = 1
        self.init_interface()

    def init_interface(self):
        self.setGeometry(400, 200, 400, 450)
        self.setWindowTitle('约瑟夫环')

        start_laber = QLabel('起始值：', self)
        start_laber.move(20, 20)

        step_laber = QLabel('步进：', self)
        step_laber.move(20, 60)

        self.start_number = QLabel('1', self)
        self.start_number.move(80, 20)

        self.step_number = QLabel('1', self)
        self.step_number.move(80, 60)

        self.start_button = QPushButton('修改起始值', self)
        self.start_button.move(200, 20)

        self.step_button = QPushButton('修改步进', self)
        self.step_button.move(200, 60)

        self.ok_button = QPushButton('OK', self)
        self.ok_button.move(100, 100)

        self.show_data = QTextBrowser(self)
        self.show_data.move(20, 150)

        self.show()

    def connect_button(self):
        self.start_button.clicked.connect(self.get_start_data)
        self.step_button.clicked.connect(self.get_step_data)
        self.ok_button.clicked.connect(self.is_ok)

    def get_start_data(self):
        num, ok = QInputDialog.getInt(self, '修改起始值', '请输入起始值：', min=1)
        if ok:
            self.start = num
            self.start_number.setText(str(num))

    def get_step_data(self):
        num, ok = QInputDialog.getInt(self, '修改步进', '请输入步进：', min=1)
        if ok:
            self.step = num
            self.step_number.setText(str(num))

    def is_ok(self):
        reply = QMessageBox.question(
            self, '确认', '是否确认?',
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
            QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.show_ring()

    def show_ring(self):
        file_reader = TxtReader(r'data\people.txt').next()
        ring = RingSort(self.start, self.step, file_reader)

        self.show_data.clear()
        for i in ring:
            self.show_data.append(i.get_information())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface = RingGraphicInterface()
    interface.connect_button()
    sys.exit(app.exec_())
