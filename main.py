import sys
from components.main_window import MainWindow
from PySide6.QtWidgets import QApplication 
from components.constants import WINDOW_ICON_PATH
from components.components import Display, Info, Button, ButtonsGrid
from styles import setupTheme



if __name__ == '__main__':

    #criando a janela
    app = QApplication(sys.argv)
    window = MainWindow()

    #personalizando
    app.setStyleSheet(setupTheme()) #setando o tema
    window.setIcon(WINDOW_ICON_PATH) # criando o icone

    #Corpo

    #info
    info = Info('texto aqui')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    display.setPlaceholderText('Digite algo')   
    window.addWidgetToVLayout(display)

    #Grid
    buttons_grid = ButtonsGrid(display, info, window)
    window.v_layout.addLayout(buttons_grid) 

    #info
    #Botao
    #buttons_grid.addWidget(Button('1'), 0, 0)
    #buttons_grid.addWidget(Button('2'), 0, 1)
    #buttons_grid.addWidget(Button('3'), 0, 2)

    #buttons_grid.addWidget(Button('4'), 1, 0)
    #buttons_grid.addWidget(Button('0'), 2, 1, 1, 1)

    window.show()
    app.exec()