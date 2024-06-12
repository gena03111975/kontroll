from datetime import datetime
import uuid


class Nat:
    def __init__(self, id = str(uuid.uuid1())[0:3],  title = "текст", body = "текст", date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def get_id(nat):
        return nat.id

    def get_title(nat):
        return nat.title

    def get_body(nat):
        return nat.body

    def get_date(nat):
        return nat.date

    def set_id(nat):
        nat.id = str(uuid.uuid1())[0:3]

    def set_title(nat, title):
        note.title = title

    def set_body(nat, body):
        nat.body = body

    def set_date(nat):
        nat.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(nat):
        return nat.id + ';' + nat.title + ';' + nat.body + ';' + nat.date

    def map_note(nat):
        return '\nID: ' + note.id + '\n' + 'Название: ' + note.title + '\n' + 'Описание: ' + note.body + '\n' + 'Дата публикации: ' + note.date