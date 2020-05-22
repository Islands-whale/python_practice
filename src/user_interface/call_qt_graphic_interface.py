import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog, QInputDialog,
                             QMessageBox)
from src.user_interface.qt_graphic_interface import QtUiForm
from src.josephus.josephus import RingSort
from src.file_reader.file_reader import ReaderFactory, ZipReader
from os.path import splitext
from zipfile import ZipFile


class CallQtUiForm(QWidget, QtUiForm):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)

        self.path_button.clicked.connect(self.choose_file)
        self.confirm_button.clicked.connect(self.show_ring)

    def choose_file(self):
        get_file_path, ok = QFileDialog.getOpenFileName(self, '请选择文件')
        if ok:
            self.path_edit.setText(get_file_path)

    def from_zip(self, path):
        try:
            with ZipFile(path) as fp:
                members = fp.namelist()
            member, ok = QInputDialog.getItem(self, '选择文件', '请选择文件', members)
            if ok:
                return ZipReader(path, member).next()

            return None

        except IOError:
            return None

    def from_txt_csv(self, path):
        reader = ReaderFactory.get_reader(self.file_type)
        if reader:
            if next(reader(path)) is None:
                return None

            return reader(path)

        return None

    def show_ring(self):
        self.out_browser.clear()
        self.file_type = splitext(self.path_edit.text())[-1]
        if self.file_type == '.zip':
            reader_generator = self.from_zip(self.path_edit.text())

        else:
            reader_generator = self.from_txt_csv(self.path_edit.text())

        try:
            assert reader_generator is not None
        except Exception:
            QMessageBox.critical(self, '错误', '文件路径错误，请重新选择！', QMessageBox.Yes)
        else:
            try:
                assert int(self.start_edit.text()) > 0
                assert int(self.step_edit.text()) > 0
            except Exception:
                QMessageBox.critical(self, '错误', '请输入正整数！', QMessageBox.Yes)

            else:
                ring = RingSort(start=int(self.start_edit.text()),
                                step=int(self.step_edit.text()),
                                reader=reader_generator)

                for i in ring:
                    self.out_browser.append(i.get_information())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface = CallQtUiForm()
    interface.show()
    sys.exit(app.exec_())
