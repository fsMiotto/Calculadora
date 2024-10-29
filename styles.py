# QSS - Estilos do QT for Python
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
# Dark Theme
# https://qdarkstylesheet.readthedocs.io/en/latest/
import qdarkstyle
from components.constants import DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR, PRIMARY_COLOR

custom_qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


def setupTheme():
    darkstyle_qss = qdarkstyle.load_stylesheet()
    combined_qss = darkstyle_qss + custom_qss
    return combined_qss