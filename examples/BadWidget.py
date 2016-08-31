from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter


'''
The following is the traceback that only appears in PyDev's debug mode
Traceback (most recent call last):
  File "C:\Users\Skyler\workspace\CSV_Test\GuiWidget.py", line 24, in paintEvent
    painter.drawStaticText( 0, 0, 'Hello World' )
TypeError: arguments did not match any overloaded call:
  drawStaticText(self, Union[QPointF, QPoint], QStaticText): argument 1 has unexpected type 'int'
  drawStaticText(self, QPoint, QStaticText): argument 1 has unexpected type 'int'
  drawStaticText(self, int, int, QStaticText): argument 3 has unexpected type 'str'
Traceback (most recent call last):
  File "C:\Users\Skyler\workspace\CSV_Test\GuiWidget.py", line 24, in paintEvent
    painter.drawStaticText( 0, 0, 'Hello World' )
TypeError: arguments did not match any overloaded call:
  drawStaticText(self, Union[QPointF, QPoint], QStaticText): argument 1 has unexpected type 'int'
  drawStaticText(self, QPoint, QStaticText): argument 1 has unexpected type 'int'
  drawStaticText(self, int, int, QStaticText): argument 3 has unexpected type 'str'
'''

import sys

class MainWnd( QMainWindow ):
    
    def __init__( self ):
        '''class constructor'''
        
        #call super class constructor
        super( MainWnd, self ).__init__()
        
        self.setWindowTitle( 'Main Window' )
        self.showMaximized()
        
    def paintEvent( self, e ):
        '''paint Handler - called whenever the window needs to be repainted'''
        
        #get a reference to an object that paints the window
        painter = QPainter()
        
        #draw some text to the window's client area
        painter.drawStaticText( 0, 0, 'Hello World' )
        
        #update the window
        painter.end()
        
        


def main():
    app = QApplication( sys.argv )
    
    wnd = MainWnd()
    
    sys.exit( app.exec_( ) )

if __name__ == '__main__':
    main()