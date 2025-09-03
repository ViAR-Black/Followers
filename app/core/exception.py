from fastapi import HTTPException, status

email_password_not_correct = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="Password or email is not correct"
)

user_alreade_exist = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="User already exist"
)
