import bcrypt


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt(rounds=12)
    pass_bytes = password.encode()
    hashed = bcrypt.hashpw(password=pass_bytes, salt=salt)
    return hashed.decode()


def verify_password(password: str, hash_password: str) -> bool:
    pass_bytes = password.encode()
    hash_pass_bytes = hash_password.encode()
    return bcrypt.checkpw(password=pass_bytes, hashed_password=hash_pass_bytes)


