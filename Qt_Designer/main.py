from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QSizePolicy, QSlider, QSpacerItem, \
    QVBoxLayout, QWidget
import sys
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pq
import pyqtgraph.opengl as gl
import numpy as np


class Plott_3D(QWidget):
    def __init__(self,arr_real,arr_imag, parent=None):
        super(Plott_3D,self).__init__(parent = parent)
        #self.horizontalLayout = QHBoxLayout(self)
        self.arr_real = arr_real
        self.arr_imag = arr_imag
        self.w = gl.GLViewWidget()
        self.w.setBackgroundColor('w')
        #self.horizontalLayout.addWidget(self.w)
        self.w.show()
        self.w.setWindowTitle('pyqtgraph example: GLSurfacePlot')
        self.w.setCameraPosition(distance=200)
        self.a = gl.GLAxisItem(text_scale=0.5)
        self.a.setSize(len(self.arr_real), len(self.arr_imag),int(round(np.amax(self.arr_real+self.arr_imag))))

        self.a.setColor([1, 0, 0], [0, 0, 0], [0, 0, 1])
        self.a.translate(-10,-10,-10)
        self.w.addItem(self.a)
        """
        self.gx = gl.GLGridItem()
        self.gx.rotate(90, 0, 1, 0)
        self.gx.translate(-10, 30, 30)
        self.gx.scale(4, 4, 1)
        self.gx.setSpacing(5,5,100)

        self.w.addItem(self.gx)
        self.gy = gl.GLGridItem()
        self.gy.rotate(90, 1, 0, 0)
        self.gy.translate(30, -10, 30)
        self.gy.scale(4, 4, 1)
        self.gy.setSpacing(5, 5, 100)
        self.w.addItem(self.gy)
        self.gz = gl.GLGridItem()
        self.gz.translate(30, 30, -10)
        self.gz.scale(4, 4, 1)
        self.gz.setSpacing(5, 5, 100)
        self.w.addItem(self.gz)
        """
        self.x = self.arr_real
        self.y = self.arr_imag
        self.z = self.x.reshape(len(self.arr_real), 1) + self.y.reshape(1, len(self.arr_imag))
        self.p2 = gl.GLSurfacePlotItem(z=self.z, shader='normalColor')
        self.p2.translate(-10, -10, -11)
        self.w.addItem(self.p2)
        #self.w.orbit(45, 45)
        #self.w.setBackgroundColor('')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = np.linspace(0,100,100)
    Real = 100*np.sin(a/5)/(0.5*a+1)

    Imag = 100*np.sin(a/5)/(0.5*a+1)

    w = Plott_3D(Real,Imag)


    #w.show()
    sys.exit(app.exec_())