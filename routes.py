from flask import Blueprint, render_template
from models import Productos

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/adios')
def adios():
    return "adios"

@main.route('/posts')
def posts():
    posts = Productos.query.all()
    return render_template('posts.html', posts=posts)

@main.route('/post/<int:post_id>', methods=['GET'])
def post(post_id):
    post = Productos.query.get or 404(post_id)
    return render_template('post.html', post=post)