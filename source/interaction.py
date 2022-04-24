from database import DataBase


class Interaction(object):
    def __init__(self, db: DataBase) -> None:
        self.db = db

    def get_token(self) -> str:
        raise NotImplementedError(
            "you must implement get_token to use Interaction child")

    def _get_id_by_name(self, name: str, table: str) -> int:
        id = self.db.execute(f"""
            SELECT id FROM {table} WHERE name = \'{name}\';
        """)
        if len(id) != 0:
            return id[0][0]
        return None

    def _select(self, name: str, table: str) -> list:
        return self.db.execute(f"""
            SELECT id, name FROM {table} WHERE name = \'{name}\';
        """)

    def _exists(self, name: str, table: str) -> bool:
        return len(self._select(name, table)) != 0


class MasterInteraction(Interaction):
    def __init__(self, db: DataBase) -> None:
        super().__init__(db)

    def get_token(self) -> str:
        token = self.db.execute("""
            SELECT master_token FROM private_info;
        """)
        return token[0][0]

    def create_user(self, usr_name: str) -> int:
        if self._exists(usr_name, "users"):
            return -1
        self.db.execute(f"""
            INSERT INTO users(name) VAlUES(\'{usr_name}\')
        """)
        return 0

    def create_event(self, owner_name: str, event_name: str, descript: str, is_public: bool) -> int:
        if self._exists(event_name, "event_types"):
            return -1
        owner_id = self._get_id_by_name(owner_name, "users")
        if not owner_id:
            return -2
        self.db.execute(f"""
            INSERT INTO event_types(owner, name, description, is_pubic)
            VALUES({owner_id}, \'{event_name}\', \'{descript}\', \'{"TRUE" if is_public else "FALSE"}\');
        """)
        return 0

    def is_owner(self, owner_name, event_name: str) -> bool:
        if str(self.db.execute("""SELECT id from event_types WHERE\
        EXISTS(SELECT id FROM event_types WHERE name = \'{}\'AND owner = \'{}\');"""\
                .format(event_name, owner_name))) == "":
            return True
        return False

    def find_event(self, event):
        if str(self.db.execute("""SELECT id from event_types WHERE EXISTS(SELECT id FROM event_types WHERE\
        name = \'{}\')""".format(event))) == "":
            return False
        return True

    def plan_event(self, owner_name, event_name,  datetime):
        owner_id = self._get_id_by_name(owner_name, "users")
        if not owner_id:
            return -1
        if self.is_owner(owner_name, event_name):
            return -2
        if self.find_event(event_name):
            return -3
        self.db.execute(f"""
            INSERT INTO events(base_type, datetime)
            VALUES(\'{owner_id}\', \'{datetime}\');
        """)
        return 0


    def subscribe(self, username:str, event_name: str):
            owner_id = self._get_id_by_name(username, "users")
            if not owner_id:
                return -1
            if not self.is_owner(username, event_name):
                return -2
            if self.find_event(event_name):
                return -3
            self.db.execute(f"""
                INSERT INTO events(subscribed_users)
                VALUES(\'{owner_id}\');
            """)
            return 0



    @staticmethod
    def parse_err(method_name: str, err_code: int) -> str:
        unknown_code_msg = f"Unknown matching error code: {err_code} in method: {method_name}"
        match method_name:
            case "create_user":
                match err_code:
                    case  0: return "Привет!"
                    case -1: return "Пользователь с этим именем уже существует"
                    case  _: return unknown_code_msg
            case "create_event":
                match err_code:
                    case  0: return "Событие успешно создано!"
                    case -1: return "Событие с этим названием уже существует"
                    case -2: return "Пользователь с вашим именем не найден. Вам необходимо сначала вызвать комнду start"
                    case  _: return unknown_code_msg
            case "plan_event":
                match err_code:
                    case  0: return "Событие успешно запланировано"
                    case -1: return "Пользователь с вашим именем не найден. Вам необходимо сначала вызвать комнду start"
                    case -2: return """Отказано в доступе! Данный пользователь не является владельцем данного события. Только владелец может назначать время проведения события."""
                    case -3: return """Нельзя запланировать событие, не создав его"""
                    case  _: return unknown_code_msg
            case "subscribe":
                match err_code:
                    case 0: return "Подписка на событие оформлена!"
                    case -1: return "Вы уже и так подписаны на это событие"
                    case -2: return "Такого события пока не существует,но вы легко можете его создать!"


class LinkerInteraction(Interaction):
    def __init__(self, db: DataBase) -> None:
        super().__init__(db)

    def get_token(self) -> str:
        token = self.db.execute("""
            SELECT linker_token FROM private_info;
        """)
        return token[0][0]
