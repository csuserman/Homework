# In order to run code, install tabulate by running this command in your terminal
# pip install tabulate

from tabulate import tabulate 

notes = [
            {"id": 1, "text": "Doing homework"},
            {"id": 2, "text": "Cleaning room"},
            {"id": 3, "text": "Preparing meal"},
            {"id": 4, "text": "Go to gym"}
        ]

class Notebook:
    def __init__(self):
        self.notes = notes

    def show_menu(self):
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

    def show_all_notes(self):
        if self.notes:
            print('-' * 50, ' \nAll notes:')
            print('\n', tabulate(self.notes, headers = 'keys', tablefmt = 'grid'), '\n')
        else:
            print("No notes available.")

    def show_note_details(self):
        try:
            note_id = int(input('Enter note ID: '))
        except ValueError:
            print('Invalid input. Please enter a valid integer for the note ID.\n')
        else:
            for note in self.notes:
                if note['id'] == note_id:
                    print(f'{'-' * 50}\nNOTE {note_id} DETAILS:\nNote id: {note_id}\nNote text: {note['text']}\n')
                    return
            print('Note ID not found.\n')

    def create_note(self):
        text = input('Enter note text: ')
        next_id = max(note['id'] for note in self.notes) + 1
        notes.append({'id': next_id, 'text': text})
        print(f'{'-' * 50}\nNEW NOTE WITH ID {next_id} CREATED\n')

    def update_note(self):
        try:
            note_id = int(input('Enter note ID to update: '))
        except ValueError:
            print('Invalid input. Please enter a valid integer for the note ID.\n')
        else:
            for note in self.notes:
                if note['id'] == note_id:
                    new_text = str(input('Enter new text: '))
                    note['text'] = new_text
                    print(f'{'-' * 50}\nNote {note_id} UPDATED.\n')
                    return
        print('Note ID not found.\n')

    def delete_note(self):
        try:
            note_id = int(input('Enter note ID to delete: '))
        except ValueError:
            print('Invalid input. Please enter a valid integer for the note ID.\n')
        else:
            for note in self.notes:
                if note['id'] == note_id:
                    notes.remove(note)
                    print(f'{'-' * 50}\nNote {note_id} DELETED.\n')
                    return
        print('Note ID not found.\n')

    def quit_application():
        print('Quiting application.')
        exit()

    def run(self):
        options = {
            '1': self.show_all_notes,
            '2': self.show_note_details,
            '3': self.create_note,
            '4': self.update_note,
            '5': self.delete_note,
            'q': self.quit_application,
            'quit': self.quit_application,
            'm': self.show_menu,
            'menu': self.show_menu
        }

        self.show_menu()
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

notebook = Notebook()
notebook.run()