import sys

import users


from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout,QComboBox,QStackedLayout,QLabel, QLineEdit  ,QGridLayout , QWidget, QLabel, QCalendarWidget ,QVBoxLayout
from PyQt6.QtGui import QIcon, QFont

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calendar Application")
        # button = QPushButton("Press Me!")
        self.selected_user_index = 0
        self.date_class = ""
        self.date_in_string = ""
        self.users = []
        #for now add one user initially
        main_user = users.User(1,"user")
        self.users.append(main_user)
        # Set the central widget of the Window.

        self.setMinimumSize(QSize(1200, 1000))
        calendar_layout = QGridLayout()
        self.events_list_widgit = QWidget()
        self.events_list = QVBoxLayout()
        events_title = QLabel("Events for selected day:")
        self.events_title_day = QLabel()
        self.events_list.addWidget(events_title)
        self.events_list.addWidget(self.events_title_day)
        self.events_list_widgit.setLayout(self.events_list)
        #Calendar widget
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setSelectedDate(self.calendar.selectedDate())
        self.events_title_day.setText(self.calendar.selectedDate().toString())
        self.calendar.selectionChanged.connect(self.calendar_date_slot)
        calendar_layout.addWidget(self.calendar,1,1)
        calendar_layout.addWidget(self.events_list_widgit,1,0)
        #date selection label
        self.label = QLabel(self.calendar.selectedDate().toString())
        self.label.setFont(QFont("Courier", 15))
        self.label.setStyleSheet('color:green')
        calendar_layout.addWidget(self.label,2,1)

        #event buttons layout
        settings_layout = QVBoxLayout()

        addeventbutton = QPushButton("Add Event")
        addeventbutton.setStyleSheet('color:green')
        addeventbutton.pressed.connect(self.reveal_settings_add)
        removeeventbutton = QPushButton("Remove Event")
        removeeventbutton.setStyleSheet('color:green')
        removeeventbutton.pressed.connect(self.reveal_settings_remove)
        updateeventbutton = QPushButton("Update Event")
        updateeventbutton.setStyleSheet('color:green')
        updateeventbutton.pressed.connect(self.reveal_settings_update)

        settings_layout.addWidget(addeventbutton)
        settings_layout.addWidget(removeeventbutton)
        settings_layout.addWidget(updateeventbutton)
        self.settings_date_selection = QLabel(self.calendar.selectedDate().toString())
        self.calendar.selectionChanged.connect(self.calendar_date_slot)
        settings_layout.addWidget(self.settings_date_selection)
        self.stacked_layout = QStackedLayout()
        #here is where u add layouts for each function to the stacked_layout 

        #add event widgit and layout 
        settings_add_event_ = QWidget() #then add a layout to taht QWidget and thats gonna be the settings for each button
        add_event_layout = QGridLayout()
        add_event_layout.setSpacing(0)
        settings_add_event_.setLayout(add_event_layout)
        self.calendar.selectionChanged.connect(self.calendar_date_slot)
        set_name_label = QLabel()
        set_name_label.setText("Enter event name: ")
        add_event_layout.addWidget(set_name_label,0,0)
        self.set_name = QLineEdit()
        add_event_layout.addWidget(self.set_name,0,1)
        self.hour_combo_box = QComboBox()
        self.hour_combo_box.setFixedWidth(100)
        self.hour_combo_box.addItems([str(i) for i in range(24)])
        hour_combo_box_label = QLabel("set your event start hour: ")
        add_event_layout.addWidget(hour_combo_box_label)
        add_event_layout.addWidget(self.hour_combo_box)
        min_combo_box_label = QLabel("set your event start minute: ")
        self.min_combo_box = QComboBox()
        self.min_combo_box.setFixedWidth(100)
        self.min_combo_box.addItems([str(i) for i in range(60)])
        add_event_layout.addWidget(min_combo_box_label)
        add_event_layout.addWidget(self.min_combo_box)

        self.hour_combo_boxe = QComboBox()
        self.hour_combo_boxe.setFixedWidth(100)
        self.hour_combo_boxe.addItems([str(i) for i in range(24)])
        hour_combo_box_labele = QLabel("set your event end hour: ")
        add_event_layout.addWidget(hour_combo_box_labele)
        add_event_layout.addWidget(self.hour_combo_boxe)
        min_combo_box_labele = QLabel("set your event end minute: ")
        self.min_combo_boxe = QComboBox()
        self.min_combo_boxe.setFixedWidth(100)
        self.min_combo_boxe.addItems([str(i) for i in range(60)])
        add_event_layout.addWidget(min_combo_box_labele)
        add_event_layout.addWidget(self.min_combo_boxe)
        add_event_button = QPushButton()
        add_event_button.released.connect(self.add_event)
        add_event_button.setText("Add Event")
        add_event_layout.addWidget(add_event_button)
        self.stacked_layout.addWidget(settings_add_event_)

        #remove event QWidgit 
        settings_remove_event = QWidget()
        remove_event_layout = QGridLayout()  
        settings_remove_event.setLayout(remove_event_layout)  
        remove_label = QLabel("NOT IMPLEMENTED")
        remove_event_layout.addWidget(remove_label,0,0)
        self.stacked_layout.addWidget(settings_remove_event)

        #update event QWidgit
        settings_update_event = QWidget()
        update_event_layout = QGridLayout()  
        settings_update_event.setLayout(update_event_layout)  
        update_label = QLabel("NOT IMPLEMENTED for update")
        update_event_layout.addWidget(update_label,0,0)
        self.stacked_layout.addWidget(settings_update_event)

 

        settings_layout.addLayout(self.stacked_layout)
        calendar_layout.addLayout(settings_layout,1,2)
        #calendar_layout.addWidget(settings_add_event_,2,2)
    
        main_widget = QWidget()
        main_widget.setLayout(calendar_layout)
        self.setCentralWidget(main_widget)
        #main_widget.        
        print(type(self.calendar.selectedDate().toString()))
        print(self.calendar.selectedDate().toString())

    def calendar_date_slot(self):
        self.date_class = self.calendar.selectedDate()
        self.date_in_string = self.date_class.toString()
        #just pass in the QDate to the event class because it has relevant getters
        self.label.setText("Selected Date Is : " + self.date_in_string)
        self.settings_date_selection.setText("Selected Date Is : " + self.date_in_string)
        self.events_title_day.setText(self.date_in_string)

    def reveal_settings_add(self):
        self.stacked_layout.setCurrentIndex(0)

    def reveal_settings_remove(self):
        self.stacked_layout.setCurrentIndex(1)

    def reveal_settings_update(self):
        self.stacked_layout.setCurrentIndex(2)

    def add_event(self):
        if (self.set_name.text()):
            current_user = self.users[self.selected_user_index]
            
        #add event and use date_class to determine which set of events to show 
            print(self.date_in_string)
            current_user.createEvent( self.set_name.text(), self.hour_combo_box.currentText(), self.hour_combo_boxe.currentText(), 
                                    self.min_combo_box.currentText(), self.min_combo_boxe.currentText(), self.date_in_string)
            print(current_user)
        else:
            print("title cannot be empty")

        
 
 
 
 
app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())