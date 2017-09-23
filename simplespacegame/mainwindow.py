from PyQt5.QtWidgets import QMainWindow

from .rc import texts


class MainWindow(QMainWindow):

    def __init__(self, args):
        super().__init__()

        self.args = args
        self.title = texts.TEXT_APP_TITLE
        self.width = 1024
        self.height = 1024
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)
        self.show()
