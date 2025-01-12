import pymongo

username = ''
password = ''
host = 'localhost'
connection = pymongo.MongoClient()
connection = pymongo.MongoClient(f'mongodb://{host}')
# connection = pymongo.MongoClient(f'mongodb://{username}:{password}@{host}')
blog_session_db = connection.blog_session_db
blog_ab = blog_session_db.blog_ab

print('---------- server admin ----------')
print(connection.admin.command('ismaster'))

print('---------- server info ----------')
print(connection.server_info())


print('---------- query result ----------')
# # Insert
# print(blog_ab.insert_one({'emailid':'kim.woongkeol@gmail.com'}))

# Select All
blog_logs = blog_ab.find()
for log in blog_logs:
    print(log)

# # Select One
# print(blog_ab.find_one( {'emailid':'kim.woongkeol@gmail.com'} ))

# # Delte Ond
# print(blog_ab.delete_one( {'emailid':'kim.woongkeol@gmail.com'} ))
# blog_logs = blog_ab.delete_many({'session_ip': '127.0.0.1'})

