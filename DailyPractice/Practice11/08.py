# Create a class Counter with a class variable count that keep track of the number of objects created.
# Increment count each time an object is created and display the total number of object created.

class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    @classmethod
    def display_count(cls):
        print(f"Total number of objects created: {cls.count}")
# Create some objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
# Display the total count of objects created
Counter.display_count()
