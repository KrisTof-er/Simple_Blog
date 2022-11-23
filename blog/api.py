from flask import Blueprint, render_template

blog_router = Blueprint('blog', __name__)


@blog_router.route('/')
def index():
    return render_template('index.html')
