"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        self.start = start
        self.next = start

    def __repr__(self):
        return f"SerialGenerator(start={self.start}, next={self.next})"

    def generate(self):
        """Captures and returns the current place in the sequence and then
        increments it forward by one."""
        current = self.next
        self.next += 1
        return current

    def reset(self):
        """Resets the SerialGenerator back to the value it was initialized with."""
        self.next = self.start
