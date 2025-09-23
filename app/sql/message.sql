CREATE TABLE message (
    message_id BIGINT PRIMARY KEY,
    content TEXT NOT NULL,
    user_id BIGINT NOT NULL REFERENCES users(id),
    created_at TIMESTAMP NOT NULL,
    replied_message_id BIGINT REFERENCES message(message_id),
    is_deleted BOOLEAN,
    last_content TEXT,
    changed_at TIMESTAMP
);