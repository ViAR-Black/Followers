class UserAlreadyExists(Exception):
    def __init__(self, message: str = "User with this email already exists"):
        super().__init__(message)

class WeakPwd(Exception):
    def __init__(self, message: str = "Password is too weak"):
        super().__init__(message)

class ShortPwd(Exception):
    def __init__(self, message: str = "Password is too short"):
        super().__init__(message)

class LowercasePwd(Exception):
    def __init__(self, message: str = "Password must contain an uppercase letter"):
        super().__init__(message)

class UppercasePwd(Exception):
    def __init__(self, message: str = "Password must contain an lowercase letter"):
        super().__init__(message)

class WithoutPunctuationPwd(Exception):
    def __init__(self, message: str = "Password must contain a special character"):
        super().__init__(message)

class WithoutDigitsPwd(Exception):
    def __init__(self, message: str = "Password must contain a number"):
        super().__init__(message)

class InvalidCredentials(Exception):
    pass
