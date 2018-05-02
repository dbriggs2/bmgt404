CREATE TABLE account (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER,
    task_name TEXT,
    task_description TEXT,
    date_time TEXT,
    FOREIGN KEY(account_id) REFERENCES account(id)
);