import bcrypt

rounds = 12

@classmethod
def hash_password(cls, password: str) -> str:
    salt = bcrypt.gensalt(rounds=cls.rounds)
    pass_bytes = password.encode()
    hashed = bcrypt.hashpw(password=pass_bytes, salt=salt)
    return hashed.decode()

@classmethod
def verify_password(cls, password: str, hash_password: str) -> bool:
    pass_bytes = password.encode()
    hash_pass_bytes = hash_password.encode()
    return bcrypt.checkpw(password=pass_bytes, hashed_password=hash_pass_bytes)


