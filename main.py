import inquirer
import pandas as pd
from db_config import sqlalchemy_conn
from eralchemy import render_er

def manual_process():
    questions = [
        inquirer.Text('uname',message="Username "),
        inquirer.Text('passwd',message="Password "),
        inquirer.Text('dbname',message="Database Name "),
        inquirer.Text('host',message="Hostname "),
        inquirer.Text('dtype',message="DB Type "),
        inquirer.Text('ddriver',message="DB Driver "),
    ]
    opt = inquirer.prompt(questions)
    render_er(f"{opt['ddriver']}://{opt['uname']}:{opt['passwd']}@{opt['host']}/{opt['dbname']}","test.png")

def config_process():
    conn = sqlalchemy_conn()
    render_er(conn, 'test.png')

if __name__ == '__main__':
    questions = [inquirer.List('pilihan',message='which config do you want to use?', choices=['Manual','Config_File'],)]
    answer = inquirer.prompt(questions)
    #print(answer['pilihan'])
    if answer['pilihan'] == "Manual":
        manual_process()
    elif answer['pilihan'] == "Config_File":
        config_process()
        #print('a')
        #config_process()
    #print(answer)
