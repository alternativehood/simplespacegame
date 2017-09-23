from PyQt5 import Qt

from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QLabel, QGridLayout
from simplespacegame.rc.texts import mainmenu as texts


class MainMenu(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()
        layout.setSpacing(0)

        main_text = QLabel(texts.MENU_LABEL)
        main_text.setProperty('Header', True)
        main_text.setAlignment(Qt.AlignCenter)
        layout.addWidget(main_text)

        self.btn_start = QPushButton(texts.START_BUTTON)
        self.btn_settings = QPushButton(texts.SETTINGS_BUTTON)
        self.btn_authors = QPushButton(texts.AUTHORS_BUTTON)
        self.btn_exit = QPushButton(texts.EXIT_BUTTON)

        layout.addWidget(self.btn_start)
        layout.addWidget(self.btn_settings)
        layout.addWidget(self.btn_authors)
        layout.addWidget(self.btn_exit)

        gridlayout = QGridLayout()
        gridlayout.setColumnStretch(0, 1)
        gridlayout.setColumnStretch(1, 0)
        gridlayout.setColumnStretch(2, 1)
        gridlayout.setRowStretch(0, 1)
        gridlayout.setRowStretch(1, 0)
        gridlayout.setRowStretch(2, 1)
        gridlayout.addLayout(layout, 1, 1)

        self.setLayout(gridlayout)
