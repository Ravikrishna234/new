"""COORDINATSET"""
class Intset(object):
    """calls when object is created"""
    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []
    def insert(self, e_input):
        """Assumes e is an integer and inserts e into self"""
        if not e_input in self.vals:
            self.vals.append(e_input)
    def member(self, e_input):
        """Returns True if e is in self, and False otherwise"""
        return e_input in self.vals

    def remove(self, e_input):
        """Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e_input)
        except:
            raise ValueError(str(e_input) + ' not found')
    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e_input) for e_input in self.vals]) + '}'
    def intersect(self, other):
        """intersects the two strings"""
        values = Intset()
        for i in self.vals:
            if other.member(i):
                values.insert(i)
        return values
def main():
    """class"""
    set_a = Intset()
    set_b = Intset()
    data = input()
    data1 = input()
    split_ = data.split()
    split1_ = data1.split()
    for i in split_:
        set_a.insert(int(i))
    for j in split1_:
        set_b.insert(int(j))
    print(set_a.intersect(set_b))

if __name__ == "__main__":
    main()
