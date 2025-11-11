from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from RJ Barrett in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://post_gres_test_db_user:mBZJ7jeiM34hnqMrIj44LCnvux1Zolwh@dpg-d49chr9r0fns738gbem0-a/post_gres_test_db")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://post_gres_test_db_user:mBZJ7jeiM34hnqMrIj44LCnvux1Zolwh@dpg-d49chr9r0fns738gbem0-a/post_gres_test_db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        First varchar(255),
        Last varchar(255),
        City varchar(255), 
        Name varchar(255), 
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created" 
        
@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgresql://post_gres_test_db_user:mBZJ7jeiM34hnqMrIj44LCnvux1Zolwh@dpg-d49chr9r0fns738gbem0-a/post_gres_test_db")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0), 
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15), 
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgresql://post_gres_test_db_user:mBZJ7jeiM34hnqMrIj44LCnvux1Zolwh@dpg-d49chr9r0fns738gbem0-a/post_gres_test_db")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
        ''')
    contents = cur.fetchall()
    conn.close()
    response=""
    response=response+"<table>"
    for player in contents: 
        response = response +"<tr"
        for info in player:
            response = response + "<td>{}</td>".format(info)
        response = response + "</tr>"
    response = response+"</tasble>"
    return response

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgresql://post_gres_test_db_user:mBZJ7jeiM34hnqMrIj44LCnvux1Zolwh@dpg-d49chr9r0fns738gbem0-a/post_gres_test_db")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"


        
    
    