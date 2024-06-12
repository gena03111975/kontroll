import File_operation
import Nat
import IU

number = 6  # сколько знаков МИНИМУМ может быть в тексте заметки


def add():
    note = IU.create_note(number)
    array = File_operation.read_file()
    for notes in array:
        if Nat.Note.get_id(note) == Nat.Note.get_id(notes):
            Nat.Note.set_id(note)
    array.append(note)
    File_operation.write_file(array, 'a')
    print('Заметка добавлена...')


def show(text):
    logic = True
    array = File_operation.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Nat.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Nat.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Nat.Note.get_date(notes):
                print(Nat.Note.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки...')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = File_operation.read_file()
    logic = True
    for notes in array:
        if id == Nat.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = IU.create_note(number)
                Nat.Note.set_title(notes, note.get_title())
                Nat.Note.set_body(notes, note.get_body())
                Nat.Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(Nat.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    File_operation.write_file(array, 'a')