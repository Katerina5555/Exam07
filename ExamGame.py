import sys
from PySide6 import QtWidgets


class ExamGame(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = ExamGame()
    myWindow.show()

    app.exec()