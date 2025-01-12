from model.mongodb import conn_mongodb
from datetime import datetime

class BlogSession():
    blog_page = {'A': 'blog_A.html', 'B': 'blog_B.html'}
    is_A_session = 0

    @staticmethod
    def save_session_info(session_ip, user_email, webpage_name):
        now = datetime.now()
        # https://strftime.org/
        now_time = now.strftime("%d/%m/%Y %H:%M:%S")  

        mongo_db = conn_mongodb()
        mongo_db.insert_one({
            'access_time': now_time,
            'page': webpage_name,
            'session_ip': session_ip,
            'user_email': user_email,
        })

    @staticmethod
    def get_blog_page(blog_id=None):
        if blog_id == None:
            if BlogSession.is_A_session:
                BlogSession.is_A_session = False
                return BlogSession.blog_page['A']
            else:
                BlogSession.is_A_session = True
                return BlogSession.blog_page['B']
        else:
            return BlogSession.blog_page[blog_id]
