DROP TABLE frequent_trades;
DROP TABLE transactions; 
DROP TABLE direct_debits;
DROP TABLE debts;
DROP TABLE merchants;
DROP TABLE tags;
DROP TABLE users;


CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    surname VARCHAR(255),
    age INT,
    budget INT,
    dark_mode BOOLEAN
);

CREATE TABLE merchants(
    id SERIAL PRIMARY KEY,
    merchant_name VARCHAR(255),
    website VARCHAR(255)
);

CREATE TABLE tags(
    id SERIAL PRIMARY KEY,
    tag_name VARCHAR(255),
    adult_rating BOOLEAN,
    user_id INT REFERENCES users(id) 
);

CREATE TABLE transactions(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    date VARCHAR(255),
    value INT,
    description VARCHAR(255),
    merchant_id INT REFERENCES merchants(id) ON DELETE SET NULL,
    priority VARCHAR(255),
    tag_id INT REFERENCES tags(id) ON DELETE SET NULL
);

CREATE TABLE direct_debits(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    date VARCHAR(255),
    value INT,
    description VARCHAR(255),
    merchant_id INT REFERENCES merchants(id) ON DELETE SET NULL,
    priority VARCHAR(255),
    tag_id INT REFERENCES tags(id) ON DELETE SET NULL,
    reoccurence_frequency_amount INT,
    reoccurence_frequency_type VARCHAR(255)
);

CREATE TABLE debts(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    date VARCHAR(255),
    value INT,
    description VARCHAR(255),
    merchant_id INT REFERENCES merchants(id) ON DELETE SET NULL,
    priority VARCHAR(255),
    tag_id INT REFERENCES tags(id) ON DELETE SET NULL,
    reoccurence_frequency_amount INT,
    reoccurence_frequency_type VARCHAR(255),
    late_payment_fine INT,
    pay_off_date VARCHAR(255)
);

CREATE TABLE frequent_trades(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    merchant_id INT REFERENCES merchants(id) ON DELETE SET NULL
);

