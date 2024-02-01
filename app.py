import sys

import users

from functools import partial
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QFrame,QScrollBar, QScrollArea, QApplication, QMainWindow, QPushButton, QHBoxLayout,QComboBox,QStackedLayout,QLabel, QLineEdit  ,QGridLayout , QWidget, QLabel, QCalendarWidget ,QVBoxLayout
from PyQt6.QtGui import QIcon, QFont

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendar Application")

        self.selected_user_index = 0
        self.date_class = ""
        self.users = []
        self.curr_selection = -1
  
        self.current_events_posted = []
        #for now add one user initially
        main_user = users.User(1,"user")
        self.users.append(main_user)
        self.current_event_selected = None

        # Set the central widget of the Window.

        self.setMinimumSize(QSize(1200, 1000))

        #major high level layouts and widgits/ sections 
        self.calendar_layout = QGridLayout() #canvas
        self.stacked_layout = QStackedLayout() #settings input
        self.scroll_area_bed = QVBoxLayout()
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
        #self.calendar.setStyleSheet("background-color :  #C3B1E1")
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
        self.label.setStyleSheet('color: black')
        self.calendar_layout.addWidget(self.label,0,1)

    def _create_events_list_widgit(self):
        self.child_widgit = QWidget()
        
        self.scroll_events_box_layout = QVBoxLayout()
        self.child_widgit.setLayout(self.scroll_events_box_layout)
        #self.scroll_events_box_layout.addStretch()
        events_list_label = QLabel("All your events")
        self.events_list_widgit.setWidget(self.child_widgit)
        self.scroll_area_bed.addWidget(events_list_label)
        self.scroll_area_bed.addWidget(self.events_list_widgit)
        self.calendar_layout.addLayout(self.scroll_area_bed, 2,1)

        #self.scroll_events_box_layout.addWidget(QLabel("NEWLABEL"))
    
    def _create_settings_layout(self):
        self.eventsettingscombobox = QComboBox()
        #self.eventsettingscombobox.setStyleSheet("QPushButton { text-align: left; background-color : #C3B1E1; border: 1px solid black; line-height: 1.8;border-radius: 155px;}")
        # addeventbutton = QPushButton("Add Event")
        # addeventbutton.setStyleSheet('color:green')
        self.eventsettingscombobox.currentIndexChanged.connect(self.reveal_settings)
        self.eventsettingscombobox.addItem("Add Event")
        self.eventsettingscombobox.addItem("Remove Event")
        self.eventsettingscombobox.addItem("Update Event")
        self.settings_layout.addWidget(self.eventsettingscombobox)
        self.settings_date_selection = QLabel(self.calendar.selectedDate().toString())
        self.settings_layout.addWidget(self.settings_date_selection)
        self.calendar_layout.addLayout(self.settings_layout,1,2)

    def _create_stacked_remove_settings_layout(self):  
        settings_remove_event = QWidget()
        remove_event_layout = QGridLayout()  
        settings_remove_event.setLayout(remove_event_layout)  
        remove_label = QLabel("Select an Event to Remove by clicking on the event on the bottom left section")
        remove_label_sel = QLabel("Selected Event: ")
        remove_event_layout.addWidget(remove_label,0,0)
        remove_event_layout.addWidget(remove_label_sel,1,0)
        self.remove_event_line = QLabel()
        self.remove_event_line.setText("No event selected")
        self.remove_event_line.setStyleSheet("border: 1px solid black;")
        self.remove_event_line.setFixedSize(220, 50)
        remove_event_layout.addWidget(self.remove_event_line,1,1)

        self.remove_button = QPushButton("Remove Selected Event")
        self.remove_button.clicked.connect(self.remove_event)
        remove_event_layout.addWidget(self.remove_button, 2,0)
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
        #self.calendar.selectionChanged.connect(self.calendar_date_slot)
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
        self.curr_selection = -1
        self.update_events_list()
        

    def event_selection(self,event):
        # self.current_event_selected = event
        # print(event)
        # setStyleSheet("background-color : yellow") 
        print("clicked: ", event)
        current_event = int(event)
        if current_event != self.curr_selection and self.curr_selection != -1:
            self.current_events_posted[self.curr_selection].setStyleSheet("QPushButton { text-align: left; background-color : #d3d3d3; border: 1px solid black; line-height: 1.8;border-radius: 155px;}")
        self.curr_selection = current_event
        self.current_events_posted[self.curr_selection].setStyleSheet("QPushButton { text-align: left; background-color : #C3B1E1; border: 1px solid black; line-height: 1.8;border-radius: 155px;}")

        selection_settings = self.eventsettingscombobox.currentIndex()

        match selection_settings:
            case 1:
                self.remove_event_line.setText(f"{self.curr_selection} " + self.users[self.selected_user_index].events[self.date_in_string][self.curr_selection].title) 



    def reveal_settings(self):
        current_index = self.eventsettingscombobox.currentIndex()
        if self.curr_selection != -1:
            self.current_events_posted[self.curr_selection].setStyleSheet("QPushButton { text-align: left; background-color : #d3d3d3; border: 1px solid black; line-height: 1.8;border-radius: 155px;}")
        self.curr_selection = -1
        try:
            self.remove_event_line.setText("No event selected")
        except AttributeError:
            pass
        match current_index:
            case 0 : 
                self.stacked_layout.setCurrentIndex(0)
            case 1 : #remove 
                self.stacked_layout.setCurrentIndex(1)
            case 2: #update
                self.stacked_layout.setCurrentIndex(2)
    
    def remove_event(self):
        current_user = self.users[self.selected_user_index]
        if self.curr_selection != -1:
            del current_user.events[self.date_in_string][self.curr_selection]
        self.curr_selection = -1
        self.remove_event_line.setText("No event selected")
        self.update_events_list()
        
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
        print("on switch: ",self.curr_selection)
        if self.date_in_string in current_user.events:
            for ind, event in enumerate(current_user.events[self.date_in_string]):
                #3rd index
                new_label = QPushButton()
                new_label.setText(f"{ind}: {event.title}\n Start Time {event.starthour}:{event.startmin}\n End Time {event.endhour}:{event.endmin}")
                new_label.clicked.connect(partial(self.event_selection,f"{ind}"))
                curr_color = ""
                
                if self.curr_selection == -1 or ind != self.curr_selection:
                    curr_color = "#d3d3d3"
                else:
                     curr_color = "#C3B1E1"
                new_label.setStyleSheet(f"QPushButton {{ text-align: left; background-color : {curr_color}; border: 1px solid black; line-height: 1.8;border-radius: 155px;}}")
                self.current_events_posted.append(new_label)
                
                self.scroll_events_box_layout.addWidget(new_label)
                print("DONE")
            #self.add_slots_to_events()
            
            #print(self.current_events_posted)
    


            



        
 
 
 
 
app = QApplication(sys.argv)

window = MainWindow()
window.show()
sys.exit(app.exec())