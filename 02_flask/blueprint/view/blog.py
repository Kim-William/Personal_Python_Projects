# blog.py Example Code
from flask import Blueprint

# Define the blueprint object
blog_ab = Blueprint('kim', __name__)  

# Example route: http://localhost:5555/kim/blog
@blog_ab.route('/blog')
def blog():
    return 'TEST BLUEPRINT'