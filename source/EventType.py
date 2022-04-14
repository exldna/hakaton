class EventType:
    def __init__(self, title: str, description: str, user: str, is_public: bool):
        self.title = title
        self.description = description
        self.is_public = is_public
        self.user = user

    def change_description(self, new_description)->None:
        self.description = new_description

    def set_restriction(self, restriction: bool)->None:
        self.is_public = restriction



