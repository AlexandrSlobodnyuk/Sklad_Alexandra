import sys
import os
from PyQt5 import QtWidgets

class ExampleApp(QtWidgets.QMainWindow, design1.Ui_MainWindow):
    def print_gcd(self):
        def gcd(a, b):
            if (b == 0):
                return a;
            else:
                return gcd(b, a % b);
        print(gcd(-2, 12), '- gcd of a and b')
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)  
        self.pushButton.clicked.connect(self.print_gcd)  
                                                            
    

def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = ExampleApp()  
    window.show()  
    app.exec_()  

if __name__ == '__main__':  
    main()  



class ExampleApp(QtWidgets.QMainWindow, design1.Ui_MainWindow):
    def print_gcd(self):
        def gcd(a, b):
            if (b == 0):
                return a;
            else:
                return gcd(b, a % b);
        print(gcd(-2, 12), '- gcd of a and b')
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)  
        self.pushButton.clicked.connect(self.print_gcd)  
                                                            
    

def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = ExampleApp()  
    window.show()  
    app.exec_()  

if __name__ == '__main__':  
    main()  
