from  EventType import EventType
from interaction import *

class Event(EventType):
    subscribers = []
    def __init__(self, title: str, description: str, user: str, is_public: bool, datetime, duration):
        super().__init__(title, description, user, is_public)
        self.datetime = datetime
        self.duration = duration

    @staticmethod
    def add_participants(self, participant):
        participants = iter(participant)
        self.subscribers.append(participant)
        if self.is_public:
            for participant in participant:
                pass
        else:
            pass

    def kick_subscriber(self, participant):
        participant = iter(participant)
        self.subscribers.remove(participant)
        for participant in participant:
            pass




