class ZeroError(Exception):
    def __init__(self, message="Must not be 0"):
        self.message = message
        super().__init__(self.message)