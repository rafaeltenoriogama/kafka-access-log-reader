CREATE TABLE logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ip VARCHAR(255),
    identd VARCHAR(255),
    userid VARCHAR(255),
    datetime VARCHAR(255),
    request VARCHAR(255),
    status_code INT,
    size VARCHAR(255),
    referer VARCHAR(255),
    user_agent VARCHAR(255)
);

