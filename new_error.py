class Zero(Exception):
    def __init__(self, message="Amount must be greater than 0"):
        self.message = message
        super().__init__(self.message)