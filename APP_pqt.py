import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtWidgets import (QApplication, QDialog,
        QFileDialog, QInputDialog, QMessageBox)

formulario = 'Aplicacion.ui'
form_class = uic.loadUiType(formulario)[0]

class MyWindowClass(QMainWindow, form_class):
    MESSAGE = """Prueba de menús con capas de formulario y \n
    barra de botones con iconos y compilacion con recursos\n
    version 1.01 abril 2019"""

    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.pantallas.setCurrentIndex(0)  # Activamos la pantalla 1

    def activap0(self):
        self.pantallas.setCurrentIndex(0) # cambiamos a la pantalla 2

    def activap1(self):
        self.pantallas.setCurrentIndex(1) # cambiamos a la pantalla 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyWindow = MyWindowClass(None)
    MyWindow.show()
    app.exec_()