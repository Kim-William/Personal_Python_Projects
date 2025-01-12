import pymysql

HOST = 'localhost'
CONN = pymysql.connect(
    host=HOST, 
    port=3306, 
    user='wkkim', 
    passwd='pwd', 
    db='blog_db', 
    charset='utf8'
    )

def conn_mysql():
    if not CONN.open:
        CONN.ping(reconnect=True)
        return CONN