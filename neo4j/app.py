from flask import Flask,render_template, flash, redirect, url_for, session, logging
from data import Articles


app= Flask(__name__)
Articles = Articles()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
