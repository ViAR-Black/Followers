begin;

CREATE TABLE "user" (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    description VARCHAR(150),
    email VARCHAR(75) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    age SMALLINT CHECK (age >= 0 AND age <= 100),
    created_at TIMESTAMP DEFAULT NOW(),
    last_online TIMESTAMP DEFAULT NOW(),
    last_update TIMESTAMP DEFAULT NOW(),
    is_active BOOLEAN NOT NULL DEFAULT true
);

CREATE TABLE room (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(40) NOT NULL,
    description VARCHAR(150),
    number_user INTEGER,
    password_hash VARCHAR(255),
    created_by BIGINT NOT NULL REFERENCES "user"(id),
    is_active BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE message (
    message_id BIGSERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    user_id BIGINT NOT NULL REFERENCES "user"(id),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    replied_message_id BIGINT REFERENCES message(message_id),
    is_deleted BOOLEAN NOT NULL DEFAULT false,
    last_content TEXT,
    changed_at TIMESTAMP
);

CREATE TABLE notifications (
    notification_id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES "user"(id),
    message_id BIGINT REFERENCES message(message_id),
    notification_type VARCHAR(20) DEFAULT 'new_message',
    content TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    is_read BOOLEAN NOT NULL DEFAULT false
);

commit;