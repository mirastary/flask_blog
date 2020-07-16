from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Miroslav Stary',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 3, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 4, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

# with this condition we can run app by $python flaskblog.py
if __name__ == '__main__':
    app.run(debug=True)


# Ended here: https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=2
#   20:00