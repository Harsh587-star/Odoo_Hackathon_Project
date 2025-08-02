CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password_hash VARCHAR(255),
    role ENUM('user', 'admin') DEFAULT 'user'
);

CREATE TABLE issues (
    issue_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(255),
    description TEXT,
    category VARCHAR(100),
    latitude VARCHAR(50),
    longitude VARCHAR(50),
    status VARCHAR(50),
    timestamp DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    issue_id INT,
    file_path VARCHAR(255),
    FOREIGN KEY (issue_id) REFERENCES issues(issue_id)
);
