from app.operations import *


class Calculation:
    """my abstract base calculation class"""

    @classmethod
    def create(cls, val1, val2):
        return cls(val1, val2)

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
        self.result = None

    def __repr__(self):
        return f'Operation: {type(self)}, (val1={self.val1}, val2={self.val2}, result={self.get_result()})'

    def set_val1(self, val1):
        """Get the result of a calculation"""
        self.val1 = val1

    def set_val2(self, val2):
        """Get the result of a calculation"""
        self.val2 = val2

    def set_result(self, result):
        """Get the result of a calculation"""
        self.result = result

    def get_result(self):
        """Get the result of a calculation"""
        return self.result


class Addition(Calculation):
    """My Addition Calculation Class"""

    def __init__(self, val1, val2):
        """concrete class constructor"""
        super().__init__(val1, val2)
        self.set_result(addition(self.val1, self.val2))


class Subtraction(Calculation):
    """My subtraction Calculation Class"""

    def __init__(self, val1, val2):
        """concrete class constructor"""
        super().__init__(val1, val2)
        self.set_result(subtraction(self.val1, self.val2))


class Multiplication(Calculation):
    """My multiplication Calculation Class"""

    def __init__(self, val1, val2):
        """concrete class constructor"""
        super().__init__(val1, val2)
        self.set_result(multiplication(self.val1, self.val2))


class Division(Calculation):
    """My division Calculation Class"""

    def __init__(self, val1, val2):
        """concrete class constructor"""
        self.set_result(division(self.val1, self.val2))
        super().__init__(val1, val2)
