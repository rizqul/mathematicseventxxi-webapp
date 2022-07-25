from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'risqull',
        'title': 'blog post content',
        'content': 'testing' 
    },
    {
        'author': 'random',
        'title': 'about',
        'content': 'tesss'
    }
]

@app.route('/')
def hello_world():
    return render_template('index.html', posts=posts)

@app.route('/about')
def aboutpage():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)