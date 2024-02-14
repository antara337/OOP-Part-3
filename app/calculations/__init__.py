from app.operations import *


class Calculation:
    """my abstract base calculation class"""

    @classmethod
    def create(cls, val1, val2):
        return cls(val1, val2)

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def set_val1(self, val1):
        """Get the result of a calculation"""
        self.val1 = val1

    def set_val2(self, val2):
        """Get the result of a calculation"""
        self.val2 = val2

    def set_result(self, result):
        """Get the result of a calculation"""
        self.result = result

    def get_val1(self):
        """Get result of a calculation class"""
        return self.val1

    def get_val2(self):
        """Get result of a calculation class"""
        return self.val2

    def get_result(self):
        """Get the result of a calculation"""
        return self.result


class Addition(Calculation):
    """My Addition Calculation Class"""
    def get_result(self):
        return addition(self.val1, self.val2)


class Subtraction(Calculation):
    """My subtraction Calculation Class"""

    def get_result(self):
        return subtraction(self.val1, self.val2)

class Multiplication(Calculation):
    """My multiplication Calculation Class"""

    def get_result(self):
        return multiplication(self.val1, self.val2)


class Division(Calculation):
    """My division Calculation Class"""

    def get_result(self):
        return division(self.val1, self.val2)
