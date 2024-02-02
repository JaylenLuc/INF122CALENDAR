from PyQt6.QtWidgets import QColorDialog
from PyQt6.QtCore import *
class BetterColorDialog(QColorDialog):
    # ...
    def __init__(self, parent=None):
        super(BetterColorDialog, self).__init__(parent)

        # when you want to destroy the dialog set this to True
        
        self._want_to_close = False
    
    def closeEvent(self, evnt):
        print("here")
        if self._want_to_close:
            super(BetterColorDialog, self).closeEvent(evnt)
        else:
            evnt.ignore()
            #self.setWindowState(QtCore.Qt.WindowMinimized)