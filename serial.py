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
        """Set up starting point."""
        self.start = self.next = start

    def __repr__(self):

        return f"<SerialGernerator start={self.start} next={self.next}>"

    def generate(self):
        """Get next serial number"""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset to start"""
        self.next = self.start
