class Square:
    def __init__(self, size=0):
        self.size = size;
        if !(type(self.size) == int):
            raise TypeError("size must be an integer")
        else if !(size < 0):
            raise ValueError("size must be >= 0")
    def area(self):
        return self.size * self.size
