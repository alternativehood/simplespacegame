from PyQt5.QtWidgets import QMainWindow
from simplespacegame.menu.main_menu import MainMenu

from .rc import texts


class MainWindow(QMainWindow):

    def __init__(self, args):
        super().__init__()

        self.args = args
        self.title = texts.common.APP_TITLE
        self.width = 1024
        self.height = 1024
        self.setWindowTitle(self.title)
        self.resize(self.width, self.height)
        self.show()

    def show_main_menu(self):
        self.active_page = MainMenu()
        self.setCentralWidget(self.active_page)
