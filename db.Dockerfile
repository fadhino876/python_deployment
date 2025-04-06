from postgres:latest
copy ./db/schema.sql /docker-entrypoint-initdb.d