#event class

class Event:
    @staticmethod
    def data_reprocess(startHour: int, endHour: int, startMin: int, endMin: int):
        return [
            "0" + startHour if len(startHour) == 1 else startHour,
            "0" + endHour if len(endHour) == 1 else endHour,
            "0" + startMin if len(startMin) == 1 else startMin,
            "0" + endMin if len(endMin) == 1 else endMin
        ]

    def __init__(self, title : str, startHour: int, endHour: int, startMin: int, endMin: int,
                    date_string):
        self.title = title
        new_data_list = Event.data_reprocess(startHour,endHour,startMin,endMin)
        self.starthour =  new_data_list[0]
        self.endhour = new_data_list[1]
        self.startmin = new_data_list[2]
        self.endmin = new_data_list[3]
        self.date_string = date_string
    
    def __str__(self):
        return f"{self.title}, {self.starthour}, {self.endhour}, {self.startmin}, {self.endmin} FOR {self.date_string}"

