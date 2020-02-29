from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def principal():
    return render_template("index.html")


@app.route("/sobre")
def sobre():
    return render_template("about.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/blog/detalhes")
def blogDetalhes():
    return render_template("single-blog.html")


@app.route("/contato")
def contato():
    return render_template("contact.html")


@app.route("/industria")
def industria():
    return render_template("industries.html")


@app.route("/trabalho")
def trabalho():
    return render_template("work.html")