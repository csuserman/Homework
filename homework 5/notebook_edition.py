# In order to run code, install tabulate by running this command in your terminal
# pip install tabulate

from tabulate import tabulate 

notes = [
    {'id': 1, 'text': 'Doing homework'},
    {'id': 2, 'text': 'Cleaning room'},
    {'id': 3, 'text': 'Prepering meal'},
    {'id': 4, 'text': 'Go to gym'}
]

def show_menu():
    menu = """
    \nCHOOSE OPTION
        1: SHOW ALL NOTES
        2: SHOW NOTE DETAILS
        3: CREATE NOTE
        4: UPDATE NOTE
        5: DELETE NOTE
        Q: QUIT THE APPLICATION
        M: SHOW MENU AGAIN\n
    """
    print(menu)

def show_all_notes(notes: list[dict]):
    print('-' * 50, '\nAll notes:')
    print(tabulate(notes, headers = 'keys', tablefmt = 'grid'), '\n')

def show_note_details(notes: list[dict]):
    try:
        note_id = int(input('Enter note ID: '))
    except ValueError:
        print('Invalid input. Please enter a valid integer for the note ID.\n')
    else:
        for note in notes:
            if note['id'] == note_id:
                print(f'{'-' * 50}\nNOTE {note_id} DETAILS:\nNote id: {note_id}\nNote text: {note['text']}\n')
                return
        print('Note ID not found.\n')

def create_note(notes: list[dict]):
    text = input('Enter note text: ')
    next_id = max(note['id'] for note in notes) + 1
    notes.append({'id': next_id, 'text': text})
    print(f'{'-' * 50}\nNEW NOTE WITH ID {next_id} CREATED\n')

def update_note():
    try:
        note_id = int(input('Enter note ID to update: '))
    except ValueError:
        print('Invalid input. Please enter a valid integer for the note ID.\n')
    else:
        for note in notes:
            if note['id'] == note_id:
                new_text = str(input('Enter new text: '))
                note['text'] = new_text
                print(f'{'-' * 50}\nNote {note_id} UPDATED.\n')
                return
        print('Note ID not found.\n')

def delete_note(notes: list[dict]):
    try:
        note_id = int(input('Enter note ID to delete: '))
    except ValueError:
        print('Invalid input. Please enter a valid integer for the note ID.\n')
    else:
        for note in notes:
            if note['id'] == note_id:
                notes.remove(note)
                print(f'{'-' * 50}\nNote {note_id} DELETED.\n')
                return
        print('Note ID not found.\n')

def quit_application():
    print('Quiting application.')
    exit()

options = {
    '1': show_all_notes,
    '2': show_note_details,
    '3': create_note,
    '4': update_note,
    '5': delete_note,
    'q': quit_application,
    'quit': quit_application,
    'm': show_menu,
    'menu': show_menu
}

show_menu()
while True:
    choice = input('Enter your choice: ').lower()
    action = options.get(choice)
    if action:
        try:
            action(notes)
        except TypeError:
            action()
    else:
        print('Invalid choice, please  again.\n')