import math


class SpaceSavingItem():
    def __init__(self, freq, error):
        self.freq = freq
        self.error = error

class SpaceSaving():
    def __init__(self, dim):
        self.dim = dim
        self.table = dict()

    def add(self, value):
        # value is monitored
        if value in self.table:
            self.table[value].freq += 1
        else:
            # if there is space add the element with freq 1 and error 0
            if len(self.table) < self.dim:
                self.table[value] = SpaceSavingItem(freq=1, error=0)
            else:
                # Search the minimum entry
                min = SpaceSavingItem(math.inf, 0)
                for (value, spaceSavingItem) in self.table.items():
                    if spaceSavingItem.freq < min.freq:
                        min = spaceSavingItem
                        minValue = value
                # Delete the minimum entry
                del self.table[minValue]
                # Insert the minimum entry
                self.table[value] = SpaceSavingItem(min.freq + 1, min.freq)

    def query(self, n):
        # get first n values sorted in decreasing order of frequency
        return list(
            map(
                lambda item: {
                    'value': item[0],
                    'frequency': str(item[1].freq),
                    'error': str(item[1].error)
                },
                sorted(self.table.items(),
                       key=lambda item: item[1].freq,
                       reverse=True)[0:n]))
