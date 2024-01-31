#event class

class Event:
    def __init__(self, title : str, startHour: int, endHour: int, startMin: int, endMin: int,
                    date_string):
        self.title = title
        self.starthour =  "0" + startHour if len(startHour) == 1 else startHour
        self.endhour = "0" + endHour if len(endHour) == 1 else endHour
        self.startmin = "0" + startMin if len(startMin) == 1 else startMin
        self.endmin = "0" + endMin if len(endMin) == 1 else endMin
        self.date_string = date_string
    
    def __str__(self):
        return f"{self.title}, {self.starthour}, {self.endhour}, {self.startmin}, {self.endmin} FOR {self.date_string}"

