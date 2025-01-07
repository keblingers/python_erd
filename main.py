import inquirer
import pandas as pd
from db_config import sqlalchemy_conn

if __name__ == '__main__':
    questions = [inquirer.List('pilihan',message='which config do you want to use?', choices=['Manual','Config File'],)]
    answer = inquirer.prompt(questions)
    print(answer)
