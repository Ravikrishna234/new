"""CLASSCOORDINATE"""
class Coordinate(object):
    """class"""
    def __init__(self, x_input, y_input):
        """initializes the method when object is created"""
        self.x_input = x_input
        self.y_input = y_input

    def getx_(self):
        """only takes first argument"""
        return self.x_input

    def gety_(self):
        """takes the second argument"""
        return self.y_input
    def __str__(self):
        return '<' + str(self.getx_()) + ',' + str(self.gety_()) + '>'
    def __eq__(self, other):
        """returns true if the parameters are same"""
        if self.getx_() == other.gety_():
            if self.getx_() == other.gety_():
                return True
        return False
    def __repr__(self):
        """represent the string in prescribed format"""
        return 'Coordinate(' + str(self.getx_()) + ',' + str(self.gety_()) + ')'
def main():
    """take input"""
    data = input()
    data = data.split()
    data = list(map(int, data))
    print(data)
    print(Coordinate(data[0], data[1]) == Coordinate(data[2], data[3]))
    print(Coordinate(data[4], data[5]).__repr__())

if __name__ == "__main__":
    main()
