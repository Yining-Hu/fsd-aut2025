'''
In Python, you can use a "hashable" object as a dictionary key. 
By default, objects of user-defined classes are not hashable because they don't have a __hash__() method defined. 
To use them as dictionary keys, you should explicitly define how to hash them.
This means you should implement __eq__ and __hash__.
'''

class Note:
    _value = 0

    def __init__(self, value) -> None:
        self._value = value

    def __str__(self) -> str:
        return "notes of $" + str(self._value)

    def get_value(self):
        return self._value

    # Implement __eq__ and __hash__ for using Note objects as keys in a dictionary
    def __eq__(self, other):
        return isinstance(other, Note) and self._value == other._value

    def __hash__(self):
        return hash(self._value)


class Wallet:
    all_notes = {}
    used_notes = {}
    note_values = [5, 10, 20, 50, 100]
    notes = [Note(value) for value in note_values]

    def __init__(self) -> None:
        for note in self.notes:
            self.all_notes[note] = 10
            self.used_notes[note] = 0

    def is_sufficient(self, price):
        myTotal = sum(self.note_values) * 10
        return myTotal >= price

    def pay(self, price):
        note_values = self.note_values
        note_values.reverse()
        for value in note_values:
            num_of_notes = price // value
            if num_of_notes <= 10:
                price = price % value
            else:
                num_of_notes = 10
                price = price - value * num_of_notes
            self.used_notes[Note(value)] = num_of_notes

        if price > 0:
            self.used_notes[Note(5)] = self.used_notes.get(Note(5), 0) + 1

    def show(self):
        for note in self.used_notes:
            print("- used " + str(self.used_notes[note]) + " note of $" + str(note.get_value()))


my_wallet = Wallet()
my_wallet.show()
price = int(input("Price: $"))
if my_wallet.is_sufficient(price):
    my_wallet.pay(price)
    my_wallet.show()
else:
    print("Insufficient funds!")