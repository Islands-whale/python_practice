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

    def show_ring(self):
        self.screen.addstr(0, 0, "Please input a file path:",
                           curses.color_pair(3))
        path = self.screen.getstr().decode()

        ok = FileReader(path).check_path()
        if not ok:
            self.screen.addstr(4, 0, "Wrong: File path error!",
                               curses.color_pair(1))

        else:
            yes = FileReader(path).check_zip()
            if yes:
                self.screen.addstr(1, 0, "Please input a file member:",
                                   curses.color_pair(3))
                current_file = self.screen.getstr().decode()
                reader_generator = FileReader(path).from_zip(current_file)

            else:
                reader_generator = FileReader(path).from_txt_csv()

            if not reader_generator:
                self.screen.addstr(4, 0, "Wrong: File path error!",
                                   curses.color_pair(1))

            else:
                self.screen.addstr(2, 0, "Please input a starting position:",
                                   curses.color_pair(3))
                start = self.screen.getstr()

                self.screen.addstr(3, 0, "Please input a step number:",
                                   curses.color_pair(3))
                step = self.screen.getstr()

                ok = JosephusUseCase.check_number(start, step)
                if not ok:
                    self.screen.addstr(
                        4, 0, "Wrong: Please input positive integer!",
                        curses.color_pair(1))

                else:
                    ring_iterator = JosephusUseCase.create_josephus(
                        start, step, reader_generator)

                    self.screen.addstr(5, 0, "The sequence after sorting is:",
                                       curses.color_pair(2))
                    for each in ring_iterator:
                        self.cursor_y += 1
                        self.screen.addstr(self.cursor_y, 0, str(each),
                                           curses.color_pair(2))

        self.screen.addstr(curses.LINES - 1, 0,
                           "Please press any key to continue...",
                           curses.color_pair(3))
        self.screen.getkey()
        curses.endwin()


if __name__ == '__main__':
    interface = UiForm()
    interface.show_ring()
