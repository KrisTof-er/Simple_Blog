from flask import Blueprint, render_template

from blog.db import ArticleDB

blog_router = Blueprint('blog', __name__)
db = ArticleDB()


@blog_router.route('/')
def index():
    return render_template('index.html')


@blog_router.route('/articles')
def get_articles():
    articles = db.get_all()
    return render_template('articles.html', articles=articles)


@blog_router.route('/article/<int:id_>')
def get_article(id_):
    article = db.get_one(id_=id_)
    return render_template('article.html', article=article)
