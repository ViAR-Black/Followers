import hashlib

class PasswordEncription:
    def __init__(self, password: str) -> None:
        self.password = password

    def hash_password(self) -> str:
        return hashlib.sha256(self.password.encode('utf-8')).hexdigest()
