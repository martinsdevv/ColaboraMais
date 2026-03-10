CREATE TABLE tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,

    author_id INTEGER NOT NULL,
    department_target_id INTEGER NOT NULL,

    status TEXT NOT NULL DEFAULT 'OPEN',
    priority TEXT DEFAULT 'NORMAL',

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME,
    closed_at DATETIME,

    FOREIGN KEY (author_id) REFERENCES users(id),
    FOREIGN KEY (department_target_id) REFERENCES departments(id)
);