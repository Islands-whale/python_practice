import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog, QInputDialog,
                             QMessageBox)
from src.user_interface.qt_graphic_interface import QtUiForm
from src.user_interface.file_reader import ZipReader
from src.user_interface.file_reader_use_case import FileReader
from src.use_cases.josephus_use_case import JosephusUseCase


class UiForm(QWidget, QtUiForm):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)

        self.path_button.clicked.connect(self.choose_file)
        self.confirm_button.clicked.connect(self.show_ring)

    def choose_file(self):
        file_path, ok = QFileDialog.getOpenFileName(self, '请选择文件')
        if ok:
            self.path.setText(file_path)

    def show_ring(self):
        self.out_browser.clear()
        path = self.path.text()

        ok = FileReader(path).check_path()
        if not ok:
            QMessageBox.critical(self, '错误', '文件路径错误，请重新选择！', QMessageBox.Yes)

        else:
            yes = FileReader(path).check_zip()
            if yes:
                members = ZipReader.get_file_list(path)
                current_file, ok = QInputDialog.getItem(
                    self, '选择文件', '请选择文件', members)
                if ok:
                    reader_generator = FileReader(path).from_zip(current_file)

            else:
                reader_generator = FileReader(path).from_txt_csv()

            if not reader_generator:
                QMessageBox.critical(self, '错误', '文件路径错误，请重新选择！',
                                     QMessageBox.Yes)

            else:
                ok = JosephusUseCase.check_number(self.start.text(),
                                                  self.step.text())
                if not ok:
                    QMessageBox.critical(self, '错误', '请输入正整数！',
                                         QMessageBox.Yes)

                else:
                    ring_iterator = JosephusUseCase.create_josephus(
                        self.start.text(), self.step.text(), reader_generator)

                    for each in ring_iterator:
                        self.out_browser.append(str(each))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface = UiForm()
    interface.show()
    sys.exit(app.exec_())
