from flask import Blueprint, request, render_template, redirect, url_for, session
from flask_login import login_user, current_user, logout_user
from control.user_control import User
from control.session_control import BlogSession
import datetime

blog_abtest = Blueprint('blog', __name__)


@blog_abtest.route('/set_email', methods=['GET', 'POST'])
def set_email():
    if request.method == 'GET':
        print('set_email', request.args.get('user_email'))
        return redirect(url_for('blog.blog_home'))
    else:
        user = User.create(request.form['user_email'], request.form['blog_id'])
        # https://docs.python.org/3/library/datetime.html#timedelta-objects
        login_user(user, remember=True, duration=datetime.timedelta(days=365))
        return redirect(url_for('blog.blog_home'))

@blog_abtest.route('/logout')
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for('blog.blog_home'))


@blog_abtest.route('/blog_home')
def blog_home():
    if current_user.is_authenticated:
        webpage_name = BlogSession.get_blog_page(current_user.blog_id)
        BlogSession.save_session_info(
            session['client_id'], current_user.user_email, webpage_name)
        return render_template(webpage_name, user_email=current_user.user_email)
    else:
        webpage_name = BlogSession.get_blog_page()
        BlogSession.save_session_info(
            session['client_id'], 'anonymous', webpage_name)
        return render_template(webpage_name)
