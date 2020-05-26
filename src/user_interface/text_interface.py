import curses
from src.user_interface.file_reader_use_case import FileReader
from src.use_cases.josephus_use_case import JosephusUseCase


class UiForm:
    def __init__(self):
        self.screen = curses.initscr()
        self.cursor_y = 5
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    def check_path(self):
        self.screen.addstr(0, 0, "Please input a file path:",
                           curses.color_pair(3))
        self.path = self.screen.getstr().decode()

        return FileReader(self.path).check_path()

    def check_zip(self):
        return FileReader(self.path).check_zip()

    def from_zip(self):
        self.screen.addstr(1, 0, "Please input a file member:",
                           curses.color_pair(3))
        current_file = self.screen.getstr().decode()
        return FileReader(self.path).from_zip(current_file)

    def from_txt_csv(self):
        return FileReader(self.path).from_txt_csv()

    def check_number(self):
        self.screen.addstr(2, 0, "Please input a starting position:",
                           curses.color_pair(3))
        self.start = self.screen.getstr()

        self.screen.addstr(3, 0, "Please input a step number:",
                           curses.color_pair(3))
        self.step = self.screen.getstr()

        return JosephusUseCase.check_number(self.start, self.step)

    def show_ring(self, reader_generator):
        ring_iterator = JosephusUseCase.create_josephus(
            self.start, self.step, reader_generator)

        self.screen.addstr(5, 0, "The sequence after sorting is:",
                           curses.color_pair(2))
        for each in ring_iterator:
            self.cursor_y += 1
            self.screen.addstr(self.cursor_y, 0, str(each),
                               curses.color_pair(2))

    def close_window(self):
        self.screen.addstr(curses.LINES - 1, 0,
                           "Please press any key to continue...",
                           curses.color_pair(3))
        self.screen.getkey()
        curses.endwin()

    def execute(self):
        if not self.check_path():
            self.screen.addstr(4, 0, "Wrong: File path error!",
                               curses.color_pair(1))
        else:
            if self.check_zip():
                reader_generator = self.from_zip()
            else:
                reader_generator = self.from_txt_csv()

            if not reader_generator:
                self.screen.addstr(4, 0, "Wrong: File path error!",
                                   curses.color_pair(1))

            else:
                if not self.check_number():
                    self.screen.addstr(
                        4, 0, "Wrong: Please input positive integer!",
                        curses.color_pair(1))
                else:
                    self.show_ring(reader_generator)
        self.close_window()


if __name__ == '__main__':
    ui = UiForm()
    ui.execute()
