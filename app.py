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