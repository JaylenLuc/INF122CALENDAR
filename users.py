#User class
from event import Event
import os 
from PyQt6.QtWidgets import QCalendarWidget
class User : 
    SUPPORTED_CALENDARS = 1
    def __init__(self, userID : int, userName : str):
        self.id = userID
        self.username = userName
        self.events = dict() # [str, Event]
        self.calendars = set() # 1 = gregorian calendar
        self.calendars.add(1)
        self.timetype = 24 

    def __str__(self):
        ret = ""
        for k,v in self.events.items():
            ret += f" {k}: { [i.__str__() for i in v] }\n"
        return ret
    def sort_ad_hoc(self, curr_day):
        self.events[curr_day].sort(key=lambda event : (event.starthour, event.startmin))

    def createEvent(self, title : str, startHour: str, endHour: str, startMin: str, endMin: str, curr_day: str):
        #create unique ID for each event and check for conflicts
        # start_time = str(startHour) + str(startMin)
        # end_time = str(endHour) + str(endMin)

        if self.timetype == 24 and  (int(startHour) < int(endHour) or (int(startHour) == int(endHour) and int(startMin) < int(endMin))):
            try:
                # while True:
                #     bit_hash = os.urandom(16)
                new_event = Event(title,startHour,endHour,startMin,endMin, curr_day)

                if curr_day not in self.events:
                    self.events[curr_day] = []
                    self.events[curr_day].append(new_event)
                else:
                    #sort by startHour first to last event
                    self.events[curr_day].append(new_event)
                    self.sort_ad_hoc(curr_day)


                    # hour_difference = int(self.events[curr_day][0].starthour) - int(startHour)
                    # if hour_difference < 0:
                    #     self.events[curr_day].append(new_event)
                    # elif hour_difference > 0:
                    #     self.events[curr_day].insert(0, new_event)
                    # else:
                    #     min_difference = int(self.events[curr_day][0].startmin) - int(startMin)
                    #     if min_difference < 0 or min_difference == 0:
                    #         self.events[curr_day].append(new_event)
                    #     elif min_difference > 0:
                    #         self.events[curr_day].insert(0, new_event)
                        
                        
            except ValueError:
                print('invalid time entry')
        else:
            print("potential end and start time error")

    def updateEvent(self, uniqueID: int):
        pass

    def removeEvent(self, uniqueID: int):
        pass

    

