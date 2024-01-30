#User class
from event import Event
import os 
from PyQt6.QtWidgets import QCalendarWidget
class User : 
    SUPPORTED_CALENDARS = 1
    def __init__(self, userID : int, userName : str):
        self.id = userID
        self.username = userName
        self.events = dict() # [int, Event]
        self.calendars = set() # 1 = gregorian calendar
        self.calendars.add(1)
        self.timetype = 24 

    # def createCalendar(self, type : int):
    #     if (type > 0 and type <= User.SUPPORTED_CALENDARS):
    #         self.calendars.add(type)
    #     else:
    #         print("tried to add unsupported calendar type")
    def __str__(self):
        ret = ""
        for k,v in self.events.items():
            ret += f" {k}: { [i.__str__() for i in v] }\n"
        return ret
    def createEvent(self, title : str, startHour: int, endHour: int, startMin: int, endMin: int, curr_day):
        #create unique ID for each event and check for conflicts
        start_time = str(startHour) + str(startMin)
        end_time = str(endHour) + str(endMin)
        #checks for valid start and end times
        # if (not title):
        #     print("title cannot be empty")
        #     return 

        if self.timetype == 24 and  (int(startHour) < int(endHour)):
            try:
                # while True:
                #     bit_hash = os.urandom(16)
                new_event = Event(title,startHour,endHour,startMin,endMin, curr_day)
                if curr_day not in self.events:
                    self.events[curr_day] = []
                    self.events[curr_day].append(new_event)
                else:
                    self.events[curr_day].append(new_event)

                



            except ValueError:
                print('invalid time entry')
        else:
            print("potential end and start time error")

    def updateEvent(self, uniqueID: int):
        pass

    def removeEvent(self, uniqueID: int):
        pass

    

