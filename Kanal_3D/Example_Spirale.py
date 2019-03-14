
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import numpy as np

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 40
w.show()
w.setWindowTitle('pyqtgraph example: GLLinePlotItem')

gx = gl.GLGridItem()
gx.rotate(90, 0, 1, 0)
gx.translate(-10, 0, 0)
w.addItem(gx)
gy = gl.GLGridItem()
gy.rotate(90, 1, 0, 0)
gy.translate(0, -10, 0)
w.addItem(gy)
gz = gl.GLGridItem()
gz.translate(0, 0, -10)
w.addItem(gz)

val = np.random.rand(100)*10 + np.random.rand(100)*1j*10
angel = np.linspace(0,5*np.pi,100)
val = 10 * np.exp(1j*angel)*(abs(np.random.rand(100))+1)


x = val.real
z = val.imag
y = np.linspace(0,100,100)

pts = np.vstack([x, y, z]).transpose()

plt = gl.GLLinePlotItem(pos=pts,  antialias=True)
plt.translate(0,-10,0)
    #color=pg.glColor((i, n * 1.3))
    #width=(i + 1) / 10.

w.addItem(plt)

if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
