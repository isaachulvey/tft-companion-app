from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
import git

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Isaac'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in Portland!'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The Avengers movie was so cool!'
		},
		{
			'author': {'username': 'Isaac'},
			'body': 'I like turtles!'
		},
		{
			'author': {'username': 'Jenny'},
			'body': 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)

# Update this for deployment later.
# @app.route('/update_server', methods=['POST'])
# def webhook():
# 	if request.method == 'POST':
# 		repo = git.Repo('/path/to/git_repo')
# 		origin = repo.remotes.origin
	
# 	origin.pull()

# 	return 'Updated server successfully', 200
# 		else:
# 			return 'Wrong event type.', 400