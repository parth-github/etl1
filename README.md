# ETL Pipeline from OLTP Mysql database into Google BigQuery Table using Pandas

## Introduction

## Objective

## Program Files

## How to run

## Result

## Project Setup

1. Local Git repo initialized with new working directory in local development PC.
2. Remote Git Repo is added as origin to this local Git repo.
3. MySQL Database `etldemo` is created in local network with `DBeaver Community Edition` and `MySQL Workbench` tool from local development machine.
4. `IMDB_MOVIES.csv` dataset is download from public repository and imported in `etldemo` database using `DBeaver` tool.
5. Python virtual environment is created with `pip` command.
6. Required Python packages are enlisted in `requirements.txt` file in the work directory.
7. DB Configuration parameters are enlisted in `.my.cnf` file in local working directory.
8. `mysql-connect.py` file created to check the DB Connection with configparser module.
9. `db_queries.py` file is created with SQL Select queries and tested in `mysql-query-check.py`.
10. 