from PyQt5 import uic, QtWidgets
import sys



class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        self.ui = uic.loadUi('test.ui', self)
        self.show()
        self.ui.button.clicked.connect(self.DoSomething)
        self.ui.slider.valueChanged.connect(self.update)
        self.ui.text.setPlainText("0")

    def update(self):

        self.a = self.ui.slider.value()
        self.ui.text.setPlainText(str(self.a))
        #print(b)



    def DoSomething(self):
        print ("button clicked")  # or message box  or something else


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())
