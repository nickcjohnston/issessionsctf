
CREATE DATABASE :DB_NAME;
CREATE USER :DB_USER;
ALTER USER :DB_USER WITH ENCRYPTED PASSWORD :'DB_PASS';
GRANT CONNECT ON DATABASE :DB_NAME TO :DB_USER;
GRANT ALL PRIVILEGES ON DATABASE :DB_NAME TO :DB_USER;
