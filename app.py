import sys

import users


from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QScrollBar, QScrollArea, QApplication, QMainWindow, QPushButton, QHBoxLayout,QComboBox,QStackedLayout,QLabel, QLineEdit  ,QGridLayout , QWidget, QLabel, QCalendarWidget ,QVBoxLayout
from PyQt6.QtGui import QIcon, QFont

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar Application")

        self.selected_user_index = 0
        self.date_class = ""
        self.users = []
        self.current_events_posted = []
        #for now add one user initially
        main_user = users.User(1,"user")
        self.users.append(main_user)

        # Set the central widget of the Window.

        self.setMinimumSize(QSize(1200, 1000))

        #major high level layouts and widgits/ sections 
        self.calendar_layout = QGridLayout() #canvas
        self.stacked_layout = QStackedLayout() #settings input
        self.events_list_widgit = QScrollArea() #left side events list interface
        self.events_list_widgit.setWidgetResizable(True)
        self.events_list_widgit.setFixedHeight(400)
        self.events_list_widgit.setVisible(True)
        self.settings_layout = QVBoxLayout() #settings layout 
        #self.settings_layout.setSizeConstraint(QSize(50, 50))

        #call creator functions to create the widgits 
        self._create_calendar_widgit()
        #initially you would want to popualate the events list but because theres no save feature a database must be implemented first
        self._create_events_list_widgit()
        self._create_settings_layout()
        self._create_stacked_add_settings_layout()
        self._create_stacked_remove_settings_layout()
        self._create_stacked_update_settings_layout()

        #after all stacked widgits are created and added to the stacklayout, add the stackedlayout to the settings_layout
        self.settings_layout.addLayout(self.stacked_layout)

        #create main_widgit and add calendar layout to it. main_widgit to be added to the central widgit
        main_widget = QWidget()
        main_widget.setLayout(self.calendar_layout)
        self.setCentralWidget(main_widget)

    #WIDGIT-CREATORS-----------------------------------------------------------------------------------------------------------------------------

    def _create_calendar_widgit(self):
        self.calendar = QCalendarWidget()
        self.calendar.setDateEditEnabled(True)
        self.calendar.setGridVisible(True)
        self.calendar.setSelectedDate(self.calendar.selectedDate())
        self.date_in_string = self.calendar.selectedDate().toString()
        self.calendar.selectionChanged.connect(self.calendar_date_slot)
        self.calendar_layout.addWidget(self.calendar,1,1)
        #date selection label
        self.label = QLabel("Selected Date Is : " + self.date_in_string)
        self.label.setFont(QFont("Courier", 15))
        self.label.setStyleSheet('color:green')
        self.calendar_layout.addWidget(self.label,0,1)

    def _create_events_list_widgit(self):
        self.child_widgit = QWidget()
        
        self.scroll_events_box_layout = QVBoxLayout()
        self.child_widgit.setLayout(self.scroll_events_box_layout)
        #self.scroll_events_box_layout.addStretch()
        
        self.events_list_widgit.setWidget(self.child_widgit)
        self.calendar_layout.addWidget(self.events_list_widgit, 2,1)

        #self.scroll_events_box_layout.addWidget(QLabel("NEWLABEL"))
    
    def _create_settings_layout(self):
        addeventbutton = QPushButton("Add Event")
        addeventbutton.setStyleSheet('color:green')
        addeventbutton.pressed.connect(self.reveal_settings_add)
        removeeventbutton = QPushButton("Remove Event")
        removeeventbutton.setStyleSheet('color:green')
        removeeventbutton.pressed.connect(self.reveal_settings_remove)
        updateeventbutton = QPushButton("Update Event")
        updateeventbutton.setStyleSheet('color:green')
        updateeventbutton.pressed.connect(self.reveal_settings_update)

        self.settings_layout.addWidget(addeventbutton)
        self.settings_layout.addWidget(removeeventbutton)
        self.settings_layout.addWidget(updateeventbutton)
        self.settings_date_selection = QLabel(self.calendar.selectedDate().toString())
        self.calendar.selectionChanged.connect(self.calendar_date_slot)
        self.settings_layout.addWidget(self.settings_date_selection)
        self.calendar_layout.addLayout(self.settings_layout,1,2)

    def _create_stacked_remove_settings_layout(self):  
        settings_remove_event = QWidget()
        remove_event_layout = QGridLayout()  
        settings_remove_event.setLayout(remove_event_layout)  
        remove_label = QLabel("NOT IMPLEMENTED")
        remove_event_layout.addWidget(remove_label,0,0)
        self.stacked_layout.addWidget(settings_remove_event)
    
    def _create_stacked_update_settings_layout(self):
        settings_update_event = QWidget()
        update_event_layout = QGridLayout()  
        settings_update_event.setLayout(update_event_layout)  
        update_label = QLabel("NOT IMPLEMENTED for update")
        update_event_layout.addWidget(update_label,0,0)
        self.stacked_layout.addWidget(settings_update_event)

    def _create_stacked_add_settings_layout(self):
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


    #SLOTS-----------------------------------------------------------------------------------------------------------------------------------------
    def calendar_date_slot(self):
        self.date_class = self.calendar.selectedDate()
        self.date_in_string = self.date_class.toString()
        #just pass in the QDate to the event class because it has relevant getters
        self.label.setText("Selected Date Is : " + self.date_in_string)
        self.settings_date_selection.setText("Selected Date Is : " + self.date_in_string)
        # self.events_title_day.setText(self.date_in_string)
        self.update_events_list()

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

            #here you populate the events_list 

            #self.events_list #this is the QVBoxLayout 
            self.update_events_list()
        else:
            print("title cannot be empty")
            
    def update_events_list(self):

        for event in self.current_events_posted:
            event.deleteLater()

        current_user = self.users[self.selected_user_index]

        self.current_events_posted = []
        if self.date_in_string in current_user.events:
            print("yes")
            for event in current_user.events[self.date_in_string]:
                new_label =QLabel(f"{event.title}\n Start Time {event.starthour}:{event.startmin}\n End Time {event.endhour}:{event.endmin}")
                self.current_events_posted.append(new_label)
                new_label.setStyleSheet("border: 1px solid black;") 
                self.scroll_events_box_layout.addWidget(new_label)
                print("DONE")
            
            #print(self.current_events_posted)
            



        
 
 
 
 
app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())