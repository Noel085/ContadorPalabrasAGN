import sys
from PyQt5 import QtWidgets, uic

class ContadorPalabras(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Carga de nuestra vista
        uic.loadUi("contadorPalabras.ui", self)
        self.btnContar.clicked.connect(self.contarPalabras)
    
    def contarPalabras(self):
        #Recuperar texto
        texto=self.edtCaracteres.text()
        #separar las plabras
        textoSeparado=texto.split()
        print(textoSeparado)
        #contar las palabras
        
        #contar caracteres
        
        print("Se ha precionado el boton")
        
    
    
app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec())

