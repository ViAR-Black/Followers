class UserAlreadyExists(Exception):
    def __init__(self, message: str = "User with this email already exists"):
        self.message = message
        super().__init__(self.message)

class WeakPwd(Exception):
    def __init__(self, message: str = "Password is too weak"):
        self.message = message
        super().__init__(self.message)

class ShortPwd(Exception):
    def __init__(self, message: str = "Password is too short"):
        self.message = message
        super().__init__(self.message)

class LowercasePwd(Exception):
    def __init__(self, message: str = "Password must contain an uppercase letter"):
        self.message = message
        super().__init__(self.message)

class UppercasePwd(Exception):
    def __init__(self, message: str = "Password must contain an lowercase letter"):
        self.message = message
        super().__init__(self.message)

class WithoutPunctuationPwd(Exception):
    def __init__(self, message: str = "Password must contain a special character"):
        self.message = message
        super().__init__(self.message)

class WithoutDigitsPwd(Exception):
    def __init__(self, message: str = "Password must contain a number"):
        self.message = message
        super().__init__(self.message)
