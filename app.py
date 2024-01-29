import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

from PyQt6.QtWidgets import QHBoxLayout, QApplication,QMainWindow, QWidget, QLabel, QCalendarWidget ,QVBoxLayout
from PyQt6.QtGui import QIcon, QFont

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calendar Application")
        button = QPushButton("Press Me!")

        # Set the central widget of the Window.

        self.setMinimumSize(QSize(1200, 1000))
        vbox = QVBoxLayout()

        #Calendar widget
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.calendar_date_slot)
        vbox.addWidget(self.calendar)

        #date selection label
        self.label = QLabel("No Date Selected")
        self.label.setFont(QFont("Courier", 15))
        self.label.setStyleSheet('color:green')
        vbox.addWidget(self.label)

        #event buttons layout
        button_layout = QHBoxLayout()
        addeventbutton = QPushButton("Add Event")
        addeventbutton.setStyleSheet('color:green')
        removeeventbutton = QPushButton("Remove Event")
        removeeventbutton.setStyleSheet('color:green')
        updateeventbutton = QPushButton("Update Event")
        updateeventbutton.setStyleSheet('color:green')
        addeventbutton.resize(150, 50) 
        button_layout.addWidget(addeventbutton)
        button_layout.addWidget(removeeventbutton)
        button_layout.addWidget(updateeventbutton)
        vbox.addLayout(button_layout)

        calendar_widget = QWidget()
        calendar_widget.setLayout(vbox)
        self.setCentralWidget(calendar_widget)


    def calendar_date_slot(self):
        dateselected = self.calendar.selectedDate()
        date_in_string = str(dateselected.toPyDate())
 
        self.label.setText("Selected Date Is : " + date_in_string)
 
 
 
 
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())