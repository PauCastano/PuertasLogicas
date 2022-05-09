import sys
from PyQt5 import QtCore, QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtWidgets import (QApplication, QDialog,
        QFileDialog, QInputDialog, QMessageBox)

formulario = 'Aplicacion.ui'
form_class = uic.loadUiType(formulario)[0]

class MyWindowClass(QMainWindow, form_class):

    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.pantallas.setCurrentIndex(0)  # Activamos la pantalla inicial de menu

    def activa_menu(self):
        self.pantallas.setCurrentIndex(0) # cambiamos a la pantalla inicial de menu

    def activa_pantalla_niveles(self):
        self.pantallas.setCurrentIndex(1) # cambiamos a la pantalla de los niveles

    def activa_pantalla_tutoriales(self):
        self.pantallas.setCurrentIndex(2) # cambiamos a la pantalla de los tutoriales

    def activa_tutorial_and(self):
        self.pantallas.setCurrentIndex(3) # cambiamos a la pantalla del tutorial de la puerta AND



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyWindow = MyWindowClass(None)
    MyWindow.show()
    app.exec_()