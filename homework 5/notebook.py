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
    print('\nCHOOSE OPTION')
    print('\t1: SHOW ALL NOTES')
    print('\t2: SHOW NOTE DETAILS')
    print('\t3: CREATE NOTE')
    print('\t4: UPDATE NOTE')
    print('\t5: DELETE NOTE')
    print('\tQ: QUIT THE APPLICATION')
    print('\tM: SHOW MENU AGAIN\n')

def show_all_notes():
    print('----------------------------------------------------------------------')
    print('All notes:')
    print(tabulate(notes, headers = 'keys', tablefmt = 'grid'), '\n')

def show_note_details():
    try:
        note_id = int(input('Enter note ID: '))
        truefalse = False
        for i in range(len(notes)):
            if notes[i]['id'] == note_id:
                print('----------------------------------------------------------------------')
                print(f'NOTE {note_id} DETAILS:\nNote id: {note_id}\nNote text: {notes[i]['text']}\n')
                truefalse = True
                break
        if not truefalse:
            print('Note ID not found.\n')
    except ValueError:
        print('Invalid input. Please enter a valid integer for the note ID.\n')

def create_note():
    text = str(input('Enter note text: '))
    new_id = max(note['id'] for note in notes) + 1
    notes.append({'id': new_id, 'text': text})
    print('----------------------------------------------------------------------')
    print(f'NEW NOTE WITH ID {new_id} CREATED\n')

def update_note():
    try:
        note_id = int(input('Enter note ID to update: '))
        truefalse = False
        for i in range(len(notes)):
            if notes[i]['id'] == note_id:
                new_text = str(input('Enter new text: '))
                notes[i]['text'] = new_text
                print('----------------------------------------------------------------------')
                print(f'Note {note_id} UPDATED.\n')
                truefalse = True
                break
        if not truefalse:
            print('Note ID not found.\n')
    except ValueError:
        print('Invalid input. Please enter a valid integer for the note ID.\n')

def delete_note():
    try:
        note_id = int(input('Enter note ID to delete: '))
        truefalse = False
        for i in range(len(notes)):
            if notes[i]['id'] == note_id:
                notes.pop(i)
                print('----------------------------------------------------------------------')
                print(f'Note {note_id} DELETED.\n')
                truefalse = True
                break
        if not truefalse:
            print('Note ID not found.\n')
    except ValueError:
        print('Invalid input. Please enter a valid integer for the note ID.\n')

def main():
    show_menu()
    while True:
        choice = str(input('Enter your choice: '))
        if choice == '1':
            show_all_notes()
        elif choice == '2':
            show_note_details()
        elif choice == '3':
            create_note()
        elif choice == '4':
            update_note()
        elif choice == '5':
            delete_note()
        elif choice.lower() == 'q' or choice.lower() == 'quit':
            print('Exiting application.')
            break
        elif choice.lower() == 'm' or choice.lower() == 'menu':
            show_menu()
        else:
            print('Invalid choice, please try again.\n')

main()