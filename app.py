import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

from PyQt6.QtWidgets import QHBoxLayout,QStackedLayout,QLabel, QLineEdit  ,QGridLayout ,QApplication,QMainWindow, QWidget, QLabel, QCalendarWidget ,QVBoxLayout
from PyQt6.QtGui import QIcon, QFont

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calendar Application")
        button = QPushButton("Press Me!")

        # Set the central widget of the Window.

        self.setMinimumSize(QSize(1200, 1000))
        calendar_layout = QGridLayout()

        #Calendar widget
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.calendar_date_slot)
        calendar_layout.addWidget(self.calendar,1,1)

        #date selection label
        self.label = QLabel("No Date Selected")
        self.label.setFont(QFont("Courier", 15))
        self.label.setStyleSheet('color:green')
        calendar_layout.addWidget(self.label,2,1)

        #event buttons layout
        settings_layout = QVBoxLayout()

        addeventbutton = QPushButton("Add Event")
        addeventbutton.setStyleSheet('color:green')

        removeeventbutton = QPushButton("Remove Event")
        removeeventbutton.setStyleSheet('color:green')

        updateeventbutton = QPushButton("Update Event")
        updateeventbutton.setStyleSheet('color:green')

        settings_layout.addWidget(addeventbutton)
        settings_layout.addWidget(removeeventbutton)
        settings_layout.addWidget(updateeventbutton)

        stacked_layout = QStackedLayout()
        #here is where u add layouts for each function to the stacked_layout 
        #self.settings_add_event_ = QWidget() then add a layout to taht QWidget and thats gonna be the settings for each button
        settings_layout.addLayout(stacked_layout)


    
        stacked_layout.addWidget(QLineEdit())


        calendar_layout.addLayout(settings_layout,1,2)
    
        main_widget = QWidget()
        main_widget.setLayout(calendar_layout)
        self.setCentralWidget(main_widget)
        #main_widget.        


    def calendar_date_slot(self):
        date_class = self.calendar.selectedDate()
        date_in_string = str(date_class.toString())
        #just pass in the QDate to the event class because it has relevant getters
        self.label.setText("Selected Date Is : " + date_in_string)
 
 
 
 
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())