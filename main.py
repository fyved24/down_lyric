import sys

from PySide6.QtWidgets import QApplication

from mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    app.exec()
"""
nuitka --standalone --mingw64 --show-memory --show-progress --nofollow-imports --plugin-enable=pyside6 --follow-import-to=mainwindow --follow-import-to=forms  --output-dir=o main.py

"""
