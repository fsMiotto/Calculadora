from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QLabel, QWidget, QPushButton
from components.constants import BIG_FONT_SIZE, SMALL_FONT_SIZE, MEDIUM_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 

        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMaximumHeight(2*BIG_FONT_SIZE)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(TEXT_MARGIN, TEXT_MARGIN-8, TEXT_MARGIN, TEXT_MARGIN-4)


class Info(QLabel):
    def __init__(self, text: str, parent: QWidget | None = None):
        super().__init__(text, parent)

        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px')
        self.setProperty('cssClass', 'specialButton')
        self.setMinimumSize(65, 65)

