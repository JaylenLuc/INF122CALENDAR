#User class
from event import Event
from datetime import datetime
import os 
class User : 
    SUPPORTED_CALENDARS = 1
    def __init__(self, userID : int, userName : str):
        self.id = userID
        self.username = userName
        self.events = dict() # [int, Event]
        self.calendars = set() # 1 = gregorian calendar
        self.timetype = 24 

    def createCalendar(self, type : int):
        if (type > 0 and type <= User.SUPPORTED_CALENDARS):
            self.calendars.add(type)
        else:
            print("tried to add unsupported calendar type")

    def createEvent(self, title : str, startHour: int, endHour: int, startMin: int, endMin: int,
                    descr: str):
        #create unique ID for each event and check for conflicts
        start_time = str(startHour) + str(startMin)
        end_time = str(endHour) + str(endMin)

        #checks for valid start and end times
        if self.timetype == 24 and (end_time > start_time):
            try:
                datetime.strptime(start_time, '%H%M')
                datetime.strptime(end_time, '%H%M')
                
                while True:
                    bit_hash = os.urandom(16)

                    if bit_hash not in self.events:
                        new_event = Event(title,startHour,endHour,startMin,endMin,descr,bit_hash)
                        self.events[bit_hash] = new_event
                        break



            except ValueError:
                print('invalid time entry')
        else:
            print("potential end and start time error")

    def updateEvent(self, uniqueID: int):
        pass

    def removeEvent(self, uniqueID: int):
        pass

    

