create database etldemo;
use etldemo;
CREATE USER parth@192.168.29.198;
grant all on etldemo.* to parth@192.168.29.198;
SELECT * FROM imdb_movies LIMIT 10;