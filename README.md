# Notes Console Application

```sh
------------------------------------------------------------
                           ЗАМЕТКИ                           
------------------------------------------------------------
В этом приложении вы можете использовать следующие команды: 
add  - Добавить заметку
read - Просмотреть заметку
list - Вывести на экран список заметок
edit - Редактировать
del  - Удалить
help - Вызвать справку по командам
save - Сохранить заметки в файл
------------------------------------------------------------
```
### Lunch Notes App
```sh
python main.py
```
## The project contains functionality for working with notes.

### Implemented
- adding
- reading
- editing 
- deleting
- view all notes
- saving to the JSON file. 
- safe exit from the Notes app with saving interactive.

### The note contains 
- id - identifier of the note,
- title - title of the note, 
- msg - body of the note, 
- date_of_create - creation date and time, 
- date_of_update - date and time of update.

#### Save notes done in **JSON** format.

### Add note
```sh
Введите команду: add
------------------------------------------------------------
Добавление Заметки
------------------------------------------------------------
Введите заголовок заметки: t1
Введите тело заметки: m1

Заметка успешно добавлена.
```

### Read note
```sh
Введите команду: read

Введите ID заметки: 9b8de249-7ee7-40e5-afc2-e50fa9463c20
------------------------------------------------------------

ID: 9b8de249-7ee7-40e5-afc2-e50fa9463c20
Заголовок: tittle1
Заметка: message1
Дата создания: 10-04-23 02:22:33
Дата обновления: 10-04-23 02:28:13

------------------------------------------------------------
```
### List of all notes
```sh
Введите команду: list

------------------------------------------------------------
Всего заметок: 2.
------------------------------------------------------------

ID: d8ea773f-de18-49af-b2bf-02492a9c768c
Заголовок: t2
Заметка: m2
Дата создания: 10-04-23 02:22:52
Дата обновления: 10-04-23 02:22:52

------------------------------------------------------------
------------------------------------------------------------

ID: 9b8de249-7ee7-40e5-afc2-e50fa9463c20
Заголовок: t1
Заметка: m1
Дата создания: 10-04-23 02:22:33
Дата обновления: 10-04-23 02:22:33

------------------------------------------------------------
------------------------------------------------------------
```
### Edit note
```sh
Введите команду: edit

Введите ID заметки: 9b8de249-7ee7-40e5-afc2-e50fa9463c20

------------------------------------------------------------
Редактирование Заметки
------------------------------------------------------------
Опции редактирования:
t - Заголовок
m - Тело заметки
a - Всё
с - Отменить редактирование
------------------------------------------------------------
Выбeрите, что хотите отредактировать: a
------------------------------------------------------------
Введите заголовок заметки: tittle1   
Введите тело заметки: message1

Заметка успешно обновлена.
```
### Delete note
```sh
Введите команду: del

Введите ID заметки: 2065dd74-20c2-4500-a2c5-336fb6906f57

------------------------------------------------------------
Удаление Заметки
------------------------------------------------------------

Заметка успешно удалена.
```
### Save note
```sh
Введите команду: save

Успешное сохранение в файл.
```
### Exit
```sh
Введите команду: exit

------------------------------------------------------------
Выход из приложения Заметки
------------------------------------------------------------
Опции для сохранения:
y - Да
n - Нет
------------------------------------------------------------
Хотите ли вы сохранить заметки в файл: y
------------------------------------------------------------
```
### Exceptions - if you try this command when the collection of notes empty
```sh
Введите команду: list

Пока нет заметок. Можете добавить заметку с промощью команды add.

Введите команду: save

Пока нет заметок. Можете добавить заметку с промощью команды add.

Введите команду: read

Пока нет заметок. Можете добавить заметку с промощью команды add.

Введите команду: del 

Пока нет заметок. Можете добавить заметку с промощью команды add.

Введите команду: edit

Пока нет заметок. Можете добавить заметку с промощью команды add.

Введите команду: exit
```
### Structure Notes App

> **Main module - main.py is entry point** to the Notes app. Run the controller
run() method.

> **Controller module**. Accepts user input commands and delegates the presentation
of the data to the view, and the handling of the data to the model.
> >`run() - Run interaction with user.`
>
> >`execute_command(command: str, notes: Notes) - Execute the command received
from the user.`

> **Views module**. Presents the data to the user.
>
> >`display_get_user_command() - Displays to the user adding command 
interaction.`
> 
> >`display_help() - Displays to the user what commands are in the application.`
> 
> >`display_notes(sorted_notes: list) - Shows a list of notes sorted by 
date of update in descending order.`
> 
> >`display_add() - Displays to the user adding interaction.`
> 
> >`display_edit() - Displays to the user edit interaction.`
> 
> >`display_note(note: dict) - Display to the user a specific note.`
> 
> >`display_need_id() - Displays a prompt for a note ID.`
> 
> >`display_result(msg: str) - Displays a message to the user about successfully
completed commands.`
> 
> >`display_delete() - Displays to the user delete interaction.`
> 
> >`display_save_before_exit() - Displays to the user save interaction before
user exit from app.`

> **Model module**. Manages the collection of notes. **Notes** - class for 
working with a collection of notes.
> 
> >`__init__(self, data: list) - Initialize the Notes object.`
>
> >`__str__(self) - Represents Notes object as a string.` 
>
> >`__repr__(self) - String representation of an object that can be executed.` 
>
> >`__bool__(self) - An object of a Notes is associated with a boolean value.`
>
> >`__len__(self) - Method returns a positive integer that represents the 
length of the object.` 
>
> >`__get_note_by_id(self, id: str) - Get note by given ID.`
>
> >`get_notes(self) - Get sorted collections of notes by date_of_update 
field in descending order.`
>
> >`add(self, note: dict) - Add the note to the notes collection.`
>
> >`read(self, id: str) - Read the note from notes collection.`
>
> >`edit(self, note: dict, **kwargs) - Edit the note from notes collection.`
>
> >`delete(self, note: dict) - Delete the note from collection.`
>
> >`sort(self, field: str) - Sorts the list of notes by the given field. 
In descending order.`

>**Utils module**. Module for storing information to the file between program 
launches.
> 
> >`save_to_file(notes: list) - Save the list with notes to a file.`
> 
> >`load_from_json_file() - Load notes from file if file exists otherwise create
empty JSON file.`