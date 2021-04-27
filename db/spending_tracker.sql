DROP TABLE frequent_trades;
-- DROP TABLE transaction_categories;
DROP TABLE transactions; 
DROP TABLE direct_debits;
DROP TABLE debts;
DROP TABLE merchants;
DROP TABLE tags;
DROP TABLE users;


-- deleted Favourite_merchants because you can do it with function and many to many table 
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
    icon VARCHAR(255),
    website VARCHAR(255)
);

CREATE TABLE tags(
    id SERIAL PRIMARY KEY,
    tag_name VARCHAR(255),
    adult_rating BOOLEAN,
    user_id INT REFERENCES users(id) 
);

-- removed tags from all transactions as I think I'm just doing them in transaction categories table
CREATE TABLE transactions(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    -- needs to be date
    date VARCHAR(255),
    value INT,
    description VARCHAR(255),
    merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE,
    priority VARCHAR(255),
    tag_id INT REFERENCES tags(id) ON DELETE CASCADE
);

CREATE TABLE direct_debits(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    -- needs to be date
    date VARCHAR(255),
    value INT,
    description VARCHAR(255),
    merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE,
    priority VARCHAR(255),
    tag_id INT REFERENCES tags(id) ON DELETE CASCADE,
    reoccurence_frequency_amount INT,

    -- missing type list as I don't think I need it
    reoccurence_frequency_type VARCHAR(255),
    reoccurence_frequency_type_amount INT,

    -- needs to be an image
    icon VARCHAR(255)
);

CREATE TABLE debts(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    -- needs to be date
    date VARCHAR(255),
    value INT,
    description VARCHAR(255),
    merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE,
    priority VARCHAR(255),
    tag_id INT REFERENCES tags(id) ON DELETE CASCADE,
    reoccurence_frequency_amount INT,

    -- missing type list as I don't think I need it
    reoccurence_frequency_type VARCHAR(255),
    reoccurence_frequency_type_amount INT,

    -- needs to be an image
    icon VARCHAR(255),
    interest INT,
    late_payment_fine INT,
    -- technically a date
    pay_off_date VARCHAR(255)
);

CREATE TABLE frequent_trades(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE
);

-- CREATE TABLE transaction_categories(
--     id SERIAL PRIMARY KEY,
--     transaction_id INT REFERENCES transactions(id) ON DELETE CASCADE,
--     direct_debit_id INT REFERENCES direct_debits(id) ON DELETE CASCADE,
--     debt_id INT REFERENCES debts(id) ON DELETE CASCADE,
--     tag_id INT REFERENCES tags(id) ON DELETE CASCADE
-- );