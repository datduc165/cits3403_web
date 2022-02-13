from flask import Flask, render_template, url_for, request
from forms import SignUpForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Can_U_Guess'
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', author="Dat")

@app.route('/about')
def about():
    return 'The About Page'

@app.route('/blog')
def blog():
    return render_template('blog.html', author="Dat")

@app.route('/blog/<int:blog_id>')
def blogpost(blog_id):
    return 'This is blog post number' + str(blog_id)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result = result)
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run()
