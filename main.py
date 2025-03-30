from fastapi import FastAPI
import uvicorn
import os
import psycopg
import os
from user import User


app = FastAPI()

# def connect():
#     conn = psycopg.connect(f"host={os.environ['DB_HOST']} user={os.environ['DB_USER']} dbname={os.environ['DB_NAME']} password={os.environ['DB_PASSWORD']}")
#     return conn

@app.get("/")
def hello():
    return f"Hello {os.environ['CALL_MY_NAME']}"

@app.get("/read")
def read():
    with open("read.txt", "r") as f:
        return f.read()

# @app.post("/add/{id}")
# def add_or_update_user(id:int, user:User):
#     conn = connect()
#     curr = conn.cursor()
#     # Check user
#     sql = curr.execute("select * from mytable where id = %s", (id,))
#     if sql.fetchone():
#         sql = curr.execute("update mytable set username=%s where id = %s", (user.username, id))
        
#     else:
#         sql = curr.execute("insert into mytable (id, username) values (%s,%s)", (id, user.username))
#     sql = curr.execute("select * from mytable where id = %s", (id,))
#     result = sql.fetchone()
    
#     conn.commit()
#     return result
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)

