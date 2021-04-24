DROP TABLE frequent_trades;
DROP TABLE transaction_categories;
DROP TABLE users;
DROP TABLE merchants;
DROP TABLE tags;
DROP TABLE transactions; 
DROP TABLE direct_debits;
DROP TABLE debts;


CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    surname VARCHAR(255),
    age INT,
    Favourite_merchants VARCHAR(255),
    Budget INT,
    Transactions VARCHAR(255),
    direct_debits VARCHAR(255),
    Theme_preference BOOLEAN,
    Debts VARCHAR(255)
);

CREATE TABLE merchants(
    id SERIAL PRIMARY KEY,
    merchant_name VARCHAR(255),
    icon VARCHAR(255),
    website VARCHAR(255)
);

CREATE TABLE tags(
    id SERIAL PRIMARY KEY,
    tag_name VARCHAR(255),
    adult_rating BOOLEAN
);

CREATE TABLE transactions(
    id SERIAL PRIMARY KEY,
    value INT,
    description VARCHAR(255),
    merchant VARCHAR(255),
    tags VARCHAR(255),
    priority VARCHAR(255)
);

CREATE TABLE direct_debits(
    id SERIAL PRIMARY KEY,
    value INT,
    description VARCHAR(255),
    merchant VARCHAR(255),
    tags VARCHAR(255),
    priority VARCHAR(255),
    reoccurence_frequency_amount INT,

    -- missing type list as I don't think I need it
    reoccurence_frequency_type INT,
    reoccurence_frequency_type_amount INT,

    -- needs to be an image
    special_symbol VARCHAR(255)
);

CREATE TABLE debts(
    id SERIAL PRIMARY KEY,
    value INT,
    description VARCHAR(255),
    merchant VARCHAR(255),
    tags VARCHAR(255),
    priority VARCHAR(255),
    reoccurence_frequency_amount INT,

    -- missing type list as I don't think I need it
    reoccurence_frequency_type INT,
    reoccurence_frequency_type_amount INT,

    -- needs to be an image
    special_symbol VARCHAR(255),
    interest INT,
    late_payment_fine INT,
    -- technically a date
    pay_off_date VARCHAR(255)
);

CREATE TABLE frequent_trades(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE
);

CREATE TABLE transaction_categories(
    id SERIAL PRIMARY KEY,
    transaction_id INT REFERENCES transactions(id) ON DELETE CASCADE,
    direct_debit_id INT REFERENCES direct_debits(id) ON DELETE CASCADE,
    debt_id INT REFERENCES debts(id) ON DELETE CASCADE,
    tag_id INT REFERENCES tags(id) ON DELETE CASCADE
);