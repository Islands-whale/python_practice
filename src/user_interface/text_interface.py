import curses
from src.josephus.josephus import RingSort
from src.file_reader.file_reader import ReaderFactory, ZipReader
from os.path import splitext


class TextUiForm:
    def __init__(self):
        self.screen = curses.initscr()
        self.cursor_y = 3
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    def get_data(self):
        self.screen.addstr(0, 0, "Please input a file path:",
                           curses.color_pair(3))
        path = self.screen.getstr()
        self.file_type = splitext(path)[-1]
        if self.file_type == '.zip':
            reader_generator = self.from_zip(path)

        else:
            reader_generator = self.from_txt_csv(path)

        try:
            assert reader_generator is not None
        except Exception:
            self.screen.addstr(4, 0, "Wrong: File path error!",
                               curses.color_pair(1))
        else:
            try:
                self.screen.addstr(2, 0, "Please input a starting position:",
                                   curses.color_pair(3))
                start = self.screen.getstr()
                assert int(start) > 0
                self.screen.addstr(3, 0, "Please input a step number:",
                                   curses.color_pair(3))
                step = self.screen.getstr()
                assert int(step) > 0
            except Exception:
                self.screen.addstr(4, 0,
                                   "Wrong: Please input positive integer!",
                                   curses.color_pair(1))

            else:
                ring = RingSort(start, step, reader_generator)

                self.screen.addstr(3, 0, "The sequence after sorting is:",
                                   curses.color_pair(2))
                for i in ring:
                    self.cursor_y += 1
                    self.screen.addstr(self.cursor_y, 0, i.get_information(),
                                       curses.color_pair(2))
        finally:
            self.screen.addstr(curses.LINES - 1, 0,
                               "Please press any key to continue...",
                               curses.color_pair(3))
            self.screen.getkey()
            curses.endwin()

    def from_zip(self, path):
        self.screen.addstr(1, 0, "Please input a file member:",
                           curses.color_pair(3))
        member = self.screen.getstr()
        return ZipReader(path, member).next()

    def from_txt_csv(self, path):
        reader = ReaderFactory.get_reader(self.file_type)
        if reader:
            if next(reader(path)) is None:

                return None

            return reader(path)

        return None


if __name__ == '__main__':
    interface = TextUiForm()
    interface.get_data()
