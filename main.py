import sys

from components.main_window import MainWindow
from PySide6.QtWidgets import QApplication 
from components.constants import WINDOW_ICON_PATH
from components.components import Display, Info, Button
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
    window.addToVLayout(info)

    # Display
    display = Display()
    display.setPlaceholderText('Digite algo')   
    window.addToVLayout(display)

    #info
    button = Button('Texto do bottao')
    window.addToVLayout(button)

    


    window.show()
    app.exec()