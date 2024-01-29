#event class

class Event:
    def __init__(self, title : str, startHour: int, endHour: int, startMin: int, endMin: int,
                    descr: str, eventID : int):
        self.title = title
        self.starthour = startHour
        self.endhour = endHour
        self.startmin = startMin
        self.endmin = endMin
        self.description = descr
        self.id = eventID

