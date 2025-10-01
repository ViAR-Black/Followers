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

CREATE TABLE notifications (
    notification_id BIGINT PRIMARY KEY,
    user_id BIGINT REFERENCES user(user_id),
    message_id BIGINT REFERENCES message(message_id),
    notification_type VARCHAR DEFAULT,
    content TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    is_read BOOLEAN
);

CREATE TABLE Users (
    id BIGINT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    description VARCHAR(150),
    email VARCHAR(75) NOT NULL,
    password VARCHAR(75) NOT NULL,
    age SMALLINT,
    created_at TIMESTAMP DEFAULT NOW(),
    last_online TIMESTAMP DEFAULT NOW(),
    last_update TIMESTAMP DEFAULT NOW(),
    is_active BOOLLEAN NOT NULL
);

CREATE TABLE Room (
    id BIGINT PRIMARY KEY,
    title VARCHAR(35) NOT NULL,
    description VARCHAR(75),
    users INTEGER,
    password VARCHAR(75),
    created_by BIGINT
    is_active BOOLLEAN NOT NULL
    created_at TIMESTAMP DEFAULT NOW(),

);
