# server.py Example Code
from flask import Flask

# Import the blueprint
from view import blog  

app = Flask(__name__)

# Register the blueprint with a prefix
app.register_blueprint(blog.blog_ab, url_prefix='/kim')  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5555')