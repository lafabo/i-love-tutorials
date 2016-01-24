from app import app
from flask import render_template, flash, redirect
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Babangida'}
	posts = [
		{
			'author': {'nickname': 'Jo'},
			'body': "Let's dance polka!"
		},
		{
			'author': {'nickname': 'Booo'},
			'body': 'Like like',
		}
	]

	return render_template('index.html',
	                       title='Home',
	                       user=user,
	                       posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenId="' + form.openid.data + '" remember_me=' + str(form.remember_me.data))
		return redirect('/index')

	return render_template('login.html',
	                       title='Sing In',
	                       form=form,
	                       providers=app.config['OPENID_PROVIDERS'])
