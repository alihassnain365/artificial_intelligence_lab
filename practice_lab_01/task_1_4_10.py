class Numbers:

    MULTIPLIER = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Instance method
    def add(self):
        return self.x + self.y

    # Class method
    @classmethod
    def multiply(cls, a):
        return a * cls.MULTIPLIER

    # Static method
    @staticmethod
    def subtract(b, c):
        return b - c

    # Instance method
    def value(self):
        return (self.x, self.y)


# Create object
numbers = Numbers(10, 20)

print(numbers.add())
print(numbers.multiply(5))
print(numbers.subtract(20, 5))
print(numbers.value())