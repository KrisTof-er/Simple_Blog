from flask import Blueprint, render_template, request, redirect, url_for

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


@blog_router.route('/create_article', methods=["GET", "POST"])
def create_article():
    if request.method == "GET":
        return render_template('article_form.html')

    title = request.form.get("title")
    text = request.form.get("text")
    new_article = db.create(title, text)
    return redirect(location=url_for("blog.get_article", id_=new_article["id"]))


@blog_router.route('/update_article/<int:id_>', methods=["GET", "POST"])
def update_article(id_):
    if request.method == "GET":
        article = db.get_one(id_)
        return render_template('article_form.html', article=article)

    title = request.form.get("title")
    text = request.form.get("text")
    updated_article = db.update(id_, title, text)
    return redirect(location=url_for("blog.get_article", id_=updated_article["id"]))


@blog_router.route('/delete_article/<int:id_>')
def delete_article(id_):
    article = db.get_one(id_=id_)
    return render_template('article.html', article=article)
