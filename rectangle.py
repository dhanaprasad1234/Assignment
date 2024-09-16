https://github.com/dhanaprasad1234/Assignment.git
# Topic: Custom Classes in Python
class Rectangle:
    def __init__(self, length: int, width: int):
        # Initialize the rectangle with length and width
        self.length = length
        self.width = width

    def __iter__(self):
        # Create an iterator that yields length and width in the specified format
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rect = Rectangle(10, 20)

# Iterating over the instance of Rectangle
for dimension in rect:
    print(dimension)
