import sys
from PyQt5.QtWidgets import QApplication
from simplespacegame.common import resource_path
from simplespacegame.mainwindow import MainWindow
from simplespacegame.parser import parser


def main():
    app = QApplication(sys.argv)

    stylesheet = open(resource_path('mystyles.qss')).read()
    app.setStyleSheet(stylesheet)

    main_window = MainWindow(parser.parse_args())
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
