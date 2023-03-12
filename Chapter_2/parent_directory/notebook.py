import datetime

last_id = 0

class Note:
    ''' Represent a note in the notebook. Match against a
    string in searches and store tags for each note'''
    def __init__(self, memo, tags=''):
        '''initialize a note with memo and optional
        sapce-sparated tags. Automatically set the note's
        creation date and unique id'''
        self.memo = memo
        self.tags = tags
        self.create_data = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        ''' Determine if this note matches the fileter
        text, Return true if it matches, False otherwise

        Search is case senitive and match both text and
        tags.'''
        return filter in self.memo or filter in self.tags

class Notebook:
    ''' Represent a collection of notes that can be tagged,
    modified, and searched'''
    def __init__(self):
        ''' Initialize a notebook with an empty list.'''
        self.notes = []

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        '''Locate the note with the given id.'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        '''Find the note with the given id and change its
        memo to the given value'''
        self._find_note(note_id).memo = memo


    def modify_tags(self, note_id, tags):
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter):
        return (note for note in self.notes
                if note.match(filter))



