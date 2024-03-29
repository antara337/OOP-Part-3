

class History(list):
    """Initialized the history object and calls the list super init"""
    def __init__(self, *args):
        super().__init__()
        for arg in args:
            self.append(arg)

    def get_last_result(self):
        return self[-1].get_result()

    def print_history(self):
        for calculation in self:
            print(calculation)
