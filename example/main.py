from flask import Flask, render_template_string, redirect
from sqlalchemy import create_engine, MetaData
from flask_login import UserMixin, LoginManager, login_user, logout_user
from flask_blogging import SQLAStorage, BloggingEngine

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"  # for WTF-forms and login
app.config["BLOGGING_URL_PREFIX"] = "/blog"
app.config["BLOGGING_DISQUS_SITENAME"] = "test"
app.config["BLOGGING_SITEURL"] = "http://localhost:8000"
app.config["BLOGGING_SITENAME"] = "My Site"
app.config["BLOGGING_TWITTER_USERNAME"] = "@me"
app.config["FILEUPLOAD_LOCALSTORAGE_IMG_FOLDER"] = "fileupload"
app.config["FILEUPLOAD_PREFIX"] = "/fileupload"
app.config["FILEUPLOAD_ALLOWED_EXTENSIONS"] = ["png", "jpg", "jpeg", "gif"]

# extensions
engine = create_engine('sqlite:////tmp/blog.db')
meta = MetaData()
sql_storage = SQLAStorage(engine, metadata=meta)
blog_engine = BloggingEngine(app, sql_storage)
login_manager = LoginManager(app)
meta.create_all(bind=engine)


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

    def get_name(self):
        return "Paul Dirac"  # typically the user's name

@login_manager.user_loader
@blog_engine.user_loader
def load_user(user_id):
    return User(user_id)

index_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Inkflow</title>
    <style>
        body {
            font-family: Arial;
            background: #f6f7fb;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            text-align: center;
            width: 320px;
        }

        h1 {
            margin-bottom: 20px;
        }

        a {
            display: block;
            margin: 10px 0;
            padding: 10px;
            text-decoration: none;
            background: #4f46e5;
            color: white;
            border-radius: 8px;
        }

        a:hover {
            background: #3730a3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Inkflow</h1>

        {% if current_user.is_authenticated %}
            <a href="/logout/">Logout</a>
        {% else %}
            <a href="/login/">Login</a>
        {% endif %}

        <a href="/blog/">Blog</a>
        <a href="/blog/sitemap.xml">Sitemap</a>
        <a href="/blog/feeds/all.atom.xml">ATOM</a>
        <a href="/fileupload/">FileUpload</a>
    </div>
</body>
</html>
"""
@app.route("/")
def index():
    return render_template_string(index_template)

@app.route("/login/")
def login():
    user = User("testuser")
    login_user(user)
    return redirect("/blog")

@app.route("/logout/")
def logout():
    logout_user()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
