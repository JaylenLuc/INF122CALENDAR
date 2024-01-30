#event class

class Event:
    def __init__(self, title : str, startHour: int, endHour: int, startMin: int, endMin: int,
                    date_string):
        self.title = title
        self.starthour = startHour
        self.endhour = endHour
        self.startmin = startMin
        self.endmin = endMin
        self.date_string = date_string
    
    def __str__(self):
        return f"{self.title}, {self.starthour}, {self.endhour}, {self.startmin}, {self.endmin} FOR {self.date_string}"

