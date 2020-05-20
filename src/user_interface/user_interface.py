import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QInputDialog, QMessageBox, QTextBrowser)
from src.josephus.josephus import RingSort
from src.file_reader.file_reader import ReaderFactory
from os.path import splitext


class RingGraphicInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.start = 1
        self.step = 1
        self.path = ''
        self.init_interface()

    def init_interface(self):
        self.setGeometry(400, 200, 400, 450)
        self.setWindowTitle('约瑟夫环')

        path_laber = QLabel('文件路径：', self)
        path_laber.move(20, 20)

        start_laber = QLabel('起始值：', self)
        start_laber.move(20, 60)

        step_laber = QLabel('步进：', self)
        step_laber.move(20, 100)

        self.file_path = QLabel(' ' * 20, self)
        self.file_path.move(80, 20)

        self.start_number = QLabel('1', self)
        self.start_number.move(80, 60)

        self.step_number = QLabel('1', self)
        self.step_number.move(80, 100)

        self.path_button = QPushButton('选择文件路径', self)
        self.path_button.move(250, 20)

        self.start_button = QPushButton('修改起始值', self)
        self.start_button.move(250, 60)

        self.step_button = QPushButton('修改步进', self)
        self.step_button.move(250, 100)

        self.ok_button = QPushButton('OK', self)
        self.ok_button.move(140, 140)

        self.show_data = QTextBrowser(self)
        self.show_data.move(60, 180)

        self.show()

    def connect_button(self):
        self.path_button.clicked.connect(self.get_file)
        self.start_button.clicked.connect(self.get_start_data)
        self.step_button.clicked.connect(self.get_step_data)
        self.ok_button.clicked.connect(self.is_ok)

    def get_file(self):
        paths = ['data\\people.txt', 'data\\people.csv']
        path, ok = QInputDialog.getItem(self, '选择路径', '请选择路径：', paths)
        if ok:
            self.path = path
            self.file_path.setText(path)

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
        file_type = splitext(self.path)[-1]
        reader = ReaderFactory.get_reader(file_type)

        file_reader = reader(self.path).next()
        ring = RingSort(self.start, self.step, file_reader)

        self.show_data.clear()
        for i in ring:
            self.show_data.append(i.get_information())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface = RingGraphicInterface()
    interface.connect_button()
    sys.exit(app.exec_())
