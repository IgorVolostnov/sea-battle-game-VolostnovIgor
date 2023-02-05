class MyException(ValueError):
    def __init__(self, message, errors):
        self.message = message
        self.errors = errors

    def __str__(self):
        return str(self.message)
