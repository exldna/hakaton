from Event import Event
from interaction import Interaction
class User:
    def __init__(self, name):
        self.name = name

    def subcribe(self, title,  datetime):
        Interaction.get_event(title, datetime)