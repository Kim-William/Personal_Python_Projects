import pymongo

HOST = 'localhost'
CONN = pymongo.MongoClient(f'mongodb://{HOST}')

def conn_mongodb():
    try:
        CONN.admin.command('ismaster')
    except:
        CONN = pymongo.MongoClient(f'mongodb://{HOST}')
    finally:
        blog_ab=CONN.session_db.blog_ab
    return blog_ab